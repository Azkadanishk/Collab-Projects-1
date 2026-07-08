from absensi import absensi
from peminjaman import peminjaman


def menu():
    while True:
        print("===================")
        print("Perpustakaan System")
        print("===================")
        print("\n1. Absensi Masuk/Keluar")
        print("2. Peminjaman Buku")
        print("3. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            print("Masuk kedalam Absensi...")
            absensi()
        elif pilihan == "2":
            print("Masuk kedalam Peminjaman...")
            peminjaman()
        elif pilihan == "3":
            print("Program selesai..")
            break
    
        else:
            print("Pilihan tidak tersedia!")

if __name__ == "__main__":
    menu()