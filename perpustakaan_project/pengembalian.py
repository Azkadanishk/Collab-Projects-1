from scanner import scan_once
from database import connect
from datetime import datetime

def proses_pengembalian(kode):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM siswa WHERE barcode=?",
        (kode,)
    )

    siswa = cursor.fetchone()

    if siswa is None:
        print("Siswa tidak ditemukan")
        conn.close()
        return
    
    siswa_id = siswa[0]
    nama = siswa[1]

    print("\nSiswa:", nama)

    cursor.execute(
        """
        SELECT
            peminjaman.id,
            buku.judul,
            buku.penulis
        FROM peminjaman
        JOIN buku
        ON peminjaman.buku_id = buku.id
        WHERE peminjaman.siswa_id=?
        AND buku.status='dipinjam'
        """,
        (siswa_id,)
    )

    buku = cursor.fetchall()

    if not buku:
        print("Tidak ada buku yang sedang dipinjam")
        conn.close()
        return
    
    print("\nBuku yang dipinjam:")

    for item in buku:
        print(
            item[0],
            "-",
            item[1],
            "oleh",
            item[2]
        )
    pilihan = int(
        input(
            "\nMasukkan ID peminjaman: "
        )
    )

    tanggal = datetime.now().strftime(
        "%d-%m-%Y"
    )

    cursor.execute(
        """
        SELECT buku_id
        FROM peminjaman
        WHERE id=?
        """,
        (pilihan,)
    )

    data = cursor.fetchone()

    if data is None:
        print("Data tidak ditemukan")
        conn.close()
        return
    buku_id = data[0]

    cursor.execute(
        """
        UPDATE buku
        SET status='tersedia'
        WHERE id=?
        """,
        (buku_id,)
    )

    cursor.execute(
        """
        UPDATE peminjaman
        SET tanggal_kembali=?
        WHERE id=?
        """,
        (
            tanggal,
            pilihan
        )
    )

    conn.commit()
    conn.close()

    print("\nPengembalian berhasil!")
    print("Tanggal:", tanggal)

def pengembalian():
    print("Pengembalian Buku")

    kode = scan_once()

    print("Kode diterima", kode)

    if kode:
        proses_pengembalian(kode)

if __name__ == "__name__":
    pengembalian()

                   