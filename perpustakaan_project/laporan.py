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
Masuk   : {data[1]}
Keluar  : {data[2]}
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
Buku    : {data[1]}
Penulis : {data[2]}
Pinjam  : {data[3]}
Kembali : {data[4]}
-------------------
            """
        )
    
    conn.close()

if __name__ == "__main__":
    laporan()