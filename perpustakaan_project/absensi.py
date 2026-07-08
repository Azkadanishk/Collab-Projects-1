from scanner import scan_qr
from database import connect
from datetime import datetime

def absensi():

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
        print("Siswa tidak ditemukan!")
        conn.close()
        return

    siswa_id = siswa[0]
    nama = siswa[1]

    waktu = datetime.now().strftime("%H:%M")

    cursor.execute(
        """
        SELECT * FROM absensi
        WHERE siswa_id=?
        ORDER BY id DESC
        LIMIT 1
        """,
        (siswa_id,)
    )

    data = cursor.fetchone()

    if data is None or data[3] is not None:
        cursor.execute(
            """
            INSERT INTO absensi
            (siswa_id, jam_masuk)
            VALUES (?,?)
            """,
            (siswa_id, waktu)
        )

        print(
            f"{nama} masuk jam {waktu}"
        )
    
    else:

        cursor.execute(
            """
            UPDATE absensi
            SET jam_keluar=?,
            jumlah_kunjungan=1
            WHERE id=?
            """,
            (waktu, data[0])
        )

        print(
            f"{nama} keluar jam {waktu}"
        )
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    absensi()