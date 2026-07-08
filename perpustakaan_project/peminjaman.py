from scanner import scan_qr
from database import connect
from datetime import datetime

def peminjaman():

    kode = scan_qr()

    if kode is None:
        print("QR tidak terbaca") 
        return
    
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

    print(f"\nSiswa: {nama}")

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
        (judul, penulis)
        VALUES (?,?)
        """,
        (judul, penulis)
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
    print("Buku:", judul)
    print("Kembali:", tanggal_kembali)

if __name__ == "__main__":
    peminjaman()