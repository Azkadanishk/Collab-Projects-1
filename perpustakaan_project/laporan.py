from database import connect

def laporan():
    conn = connect()
    cursor = conn.cursor()

    print("=== LAPORAN PERPUSTAKAAN ===")

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM absensi
        """
    )
    total_kunjungan = cursor.fetchone()[0]

    print("Total kunjungan:", total_kunjungan)

    print("\n--- DATA KUNJUNGAN ---")

    cursor.execute(
        """
        SELECT
            siswa.nama,
            siswa.kelas,
            absensi.jam_masuk,
            absensi.jam_keluar
        FROM absensi
        JOIN siswa
        ON absensi.siswa_id = siswa.id
        """
    )

    data_absensi = cursor.fetchall()

    if data_absensi:
        for data in data_absensi:
            print(
                f"""
Nama    : {data[0]}
Kelas   : {data[1]}
Masuk   : {data[2]}
Keluar  : {data[3]}
-------------------
                """
            )

    else:
        print("Belum ada data absensi")

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM buku
        """
    )
    total_buku = cursor.fetchone()[0]

    print(
        "\nTotal buku:",
        total_buku
    )

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM buku
        WHERE status='dipinjam'
        """
    )

    sedang_dipinjam = cursor.fetchone()[0]

    print(
        "Buku dipinjam:",
        sedang_dipinjam
    )

    print("\n--- RIWAYAT PEMINJAMAN ---")

    cursor.execute(
        """
        SELECT
            siswa.nama,
            siswa.kelas,
            buku.judul,
            buku.penulis,
            peminjaman.tanggal_pinjam,
            peminjaman.tanggal_kembali
        FROM peminjaman

        JOIN siswa
        ON peminjaman.siswa_id=siswa.id

        JOIN buku
        ON peminjaman.buku_id=buku.id
        """
    )
    riwayat = cursor.fetchall()

    for data in riwayat:
        print(
            f"""
Siswa   : {data[0]}
Kelas   : {data[1]}
Buku    : {data[2]}
Penulis : {data[3]}
Pinjam  : {data[4]}
Kembali : {data[5]}
-------------------
            """
        )
    
    conn.close()

if __name__ == "__main__":
    laporan()