import qrcode
from database import connect

def tambah_siswa(nama, kelas, barcode):
    
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO siswa (nama, kelas, barcode) 
        VALUES (?, ?, ?)
        """, 
        (nama, kelas, barcode)
    )
    conn.commit()
    conn.close()

def buat_qr(data):

    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )

    qr.add_data(data)
    qr.make(fit=True)

    gambar = qr.make_image()

    filename = f"qrcode/{data}.png"
    gambar.save(filename)

    print("QR dah dibuat: ", filename)

def daftar_siswa():

    nama = input("Nama siswa: ")
    kelas = input("Kelas: ")
    kode = input("Kode barcode: ")

    tambah_siswa(nama, kelas, kode)

    buat_qr(kode)

    print("Siswa berhasil ditambahkan")