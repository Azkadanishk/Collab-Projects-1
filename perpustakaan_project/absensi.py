from scanner import scan_qr_realtime
from database import connect
from datetime import datetime
import keyboard

def proses_absensi(kode):

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

    waktu = datetime.now().strftime("%H:%M:%S")

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
            (siswa_id, jam_masuk, jam_keluar, jumlah_kunjungan)
            VALUES (?, ?, ?, ?)
            """,
            (
                siswa_id,
                waktu,
                None,
                0
            )
        )
        print(
            f"[MASUK] {nama} - {waktu}"
        )

    else:

        cursor.execute(
            """
            UPDATE absensi
            SET jam_keluar=?,
            jumlah_kunjungan=1
            WHERE id=?
            """,
            (
                waktu,
                data[0]
            )
        )
        print(
            f"[Keluar] {nama} - {waktu}"
        )
    
    conn.commit()
    conn.close()
    
def absensi():
    print("Tekan 'Q' untuk keluar\n")
    scan_qr_realtime(
        proses_absensi
    )
if __name__ == "__main__":
    absensi()