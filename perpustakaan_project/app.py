from flask import Flask, render_template, redirect, url_for, request
from database import connect

from absensi import absensi
from peminjaman import peminjaman
from pengembalian import pengembalian
from laporan import laporan
from qr_generator import daftar_siswa

app = Flask(__name__)


# ==========================
# Dashboard
# ==========================

@app.route("/")
def dashboard():

    conn = connect()
    cursor = conn.cursor()

    # Total siswa
    cursor.execute("SELECT COUNT(*) FROM siswa")
    siswa = cursor.fetchone()[0]

    # Total buku
    cursor.execute("SELECT COUNT(*) FROM buku")
    buku = cursor.fetchone()[0]

    # Buku dipinjam
    cursor.execute("""
        SELECT COUNT(*)
        FROM buku
        WHERE status='dipinjam'
    """)
    dipinjam = cursor.fetchone()[0]

    # Total kunjungan
    cursor.execute("""
        SELECT COUNT(*)
        FROM absensi
    """)
    kunjungan = cursor.fetchone()[0]

    conn.close()

    return render_template(
        "index.html",
        siswa=siswa,
        buku=buku,
        dipinjam=dipinjam,
        kunjungan=kunjungan
    )


# ==========================
# DATA SISWA
# ==========================

@app.route("/siswa")
def siswa():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            nama,
            kelas,
            barcode
        FROM siswa
        ORDER BY nama
    """)

    data = cursor.fetchall()

    conn.close()

    return render_template(
        "siswa.html",
        data=data
    )


@app.route("/tambah_siswa")
def tambah_siswa():

    daftar_siswa()

    return redirect(url_for("siswa"))


# ==========================
# DATA BUKU
# ==========================

@app.route("/buku")
def buku():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            judul,
            penulis,
            status
        FROM buku
        ORDER BY id
    """)

    data = cursor.fetchall()

    conn.close()

    return render_template(
        "buku.html",
        data=data
    )


# ==========================
# ABSENSI
# ==========================

@app.route("/absensi")
def buka_absensi():

    absensi()

    return redirect(url_for("dashboard"))


# ==========================
# PEMINJAMAN
# ==========================

@app.route("/peminjaman", methods=["GET", "POST"])
def buka_peminjaman():

    conn = connect()
    cursor = conn.cursor()

    if request.method == "POST":

        siswa = request.form["siswa"]
        buku = request.form["buku"]
        tanggal_pinjam = request.form["tanggal_pinjam"]
        tanggal_kembali = request.form["tanggal_kembali"]

        cursor.execute("""
            INSERT INTO peminjaman
            (siswa_id,buku_id,tanggal_pinjam,tanggal_kembali)

            VALUES (?,?,?,?)
        """,(siswa,buku,tanggal_pinjam,tanggal_kembali))

        cursor.execute("""
            UPDATE buku
            SET status='dipinjam'
            WHERE id=?
        """,(buku,))

        conn.commit()

        conn.close()

        return redirect(url_for("dashboard"))

    cursor.execute("""
        SELECT barcode,nama,kelas
        FROM siswa
        ORDER BY nama
    """)

    siswa_data = cursor.fetchall()

    cursor.execute("""
        SELECT id,judul
        FROM buku
        WHERE status='tersedia'
        ORDER BY judul
    """)

    buku_data = cursor.fetchall()

    conn.close()

    return render_template(
        "peminjaman.html",
        siswa_data=siswa_data,
        buku_data=buku_data
    )

# ==========================
# PENGEMBALIAN
# ==========================

@app.route("/pengembalian", methods=["GET", "POST"])
def buka_pengembalian():

    conn = connect()
    cursor = conn.cursor()

    if request.method == "POST":

        peminjaman_id = request.form["peminjaman_id"]

        cursor.execute("""
            SELECT buku_id
            FROM peminjaman
            WHERE id=?
        """,(peminjaman_id,))

        buku_id = cursor.fetchone()[0]

        cursor.execute("""
            DELETE FROM peminjaman
            WHERE id=?
        """,(peminjaman_id,))

        cursor.execute("""
            UPDATE buku
            SET status='tersedia'
            WHERE id=?
        """,(buku_id,))

        conn.commit()

        conn.close()

        return redirect(url_for("dashboard"))

    cursor.execute("""

        SELECT

            peminjaman.id,

            siswa.nama,

            buku.judul

        FROM peminjaman

        JOIN siswa

        ON peminjaman.siswa_id=siswa.barcode

        JOIN buku

        ON peminjaman.buku_id=buku.id

        ORDER BY siswa.nama

    """)

    data = cursor.fetchall()

    conn.close()

    return render_template(
        "pengembalian.html",
        data=data
    )

# ==========================
# LAPORAN
# ==========================

@app.route("/laporan")
def buka_laporan():

    conn = connect()

    cursor = conn.cursor()

    cursor.execute("""

        SELECT

            siswa.nama,

            siswa.kelas,

            buku.judul,

            buku.penulis,

            peminjaman.tanggal_pinjam,

            peminjaman.tanggal_kembali,

            buku.status

        FROM peminjaman

        JOIN siswa

        ON peminjaman.siswa_id=siswa.barcode

        JOIN buku

        ON peminjaman.buku_id=buku.id

        ORDER BY peminjaman.tanggal_pinjam DESC

    """)

    data = cursor.fetchall()

    conn.close()

    return render_template(

        "laporan.html",

        data=data

    )


# ==========================
# RUN
# ==========================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )