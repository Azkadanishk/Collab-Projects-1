from scanner import scan_once
from database import connect
from datetime import datetime

def proses_peminjaman(kode):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM siswa WHERE barcode=?",
        (kode,)
    )

    siswa = cursor.fetchone()

    if siswa is None:
        print("Siswa tidak ditemukan:", kode)
        conn.close()
        return
    
    siswa_id = siswa[0]
    nama = siswa[1]
    kelas = siswa[2]

    print("\nSiswa:", nama)

    judul = input("Judul buku: ")
    penulis = input("Penulis: ")
    tanggal_kembali = input(
        "Tanggal kembali (DD-MM-YYYY): "
    )

    tanggal_pinjam = datetime.now().strftime(
        "%d-%m-%Y"
    )

    cursor.execute(
        """
        INSERT INTO buku
        (judul, penulis, status)
        VALUES (?, ?, ?)
        """,
        (
            judul,
            penulis,
            "dipinjam"
        )
    )

    buku_id = cursor.lastrowid

    cursor.execute(
        """
        INSERT INTO peminjaman
        (siswa_id, buku_id, tanggal_pinjam, tanggal_kembali)
        VALUES (?,?,?,?)
        """,
        (
            siswa_id,
            buku_id,
            tanggal_pinjam,
            tanggal_kembali
        )
    )

    conn.commit()
    conn.close()

    print("\nPeminjaman Berhasil!")
    print("======================")
    print("Nama:", nama)
    print("Kelas:", kelas)
    print("Buku:", judul)
    print("Kembali:", tanggal_kembali)

def peminjaman():
    print("Peminjaman buku")

    kode = scan_once()

    if kode:
        proses_peminjaman(kode)
if __name__ == "__main__":
    peminjaman()