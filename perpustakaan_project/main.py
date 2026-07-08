from absensi import absensi
from peminjaman import peminjaman
from pengembalian import pengembalian
from laporan import laporan
from qr_generator import daftar_siswa


def menu():
    while True:
        print("===================")
        print("SISTEM PERPUSTAKAAN")
        print("===================")
        print("\n1. Absensi Masuk/Keluar")
        print("2. Peminjaman Buku")
        print("3. Pengembalian Buku")
        print("4. Laporan Perpustakaan")
        print("5. Pendaftaran Siswa Perpustakaan")
        print("6. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            print("Masuk kedalam Absensi...")
            absensi()
        elif pilihan == "2":
            print("Masuk kedalam Peminjaman...")
            peminjaman()
        elif pilihan == "3":
            print("Masuk kedalam Pengembalian...")
            pengembalian()
        elif pilihan == "4":
            print("Masuk kedalam Laporan Perpustakaan...")
            laporan()
        elif pilihan == "5":
            print("Masuk kedalam Pendaftaran Siswa Perpustakaan...")
            daftar_siswa()
        elif pilihan == "6":
            print("Program selesai..")
            break
    
        else:
            print("Pilihan tidak tersedia!")

if __name__ == "__main__":
    menu()