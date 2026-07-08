import sqlite3

DB_NAME = "database.db"

def connect():
    return sqlite3.connect(
        DB_NAME,
        timeout=10
    )

def create_tables():
    conn = connect()
    cursor = conn.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS siswa (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama TEXT NOT NULL,
        barcode TEXT UNIQUE NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS absensi (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        siswa_id INTEGER,
        jam_masuk TEXT,
        jam_keluar TEXT,
        jumlah_kunjungan INTEGER DEFAULT 0,
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS buku (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        judul TEXT NOT NULL,
        penulis TEXT,
        status TEXT DEFAULT 'tersedia'
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS peminjaman (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        siswa_id INTEGER,
        buku_id INTEGER,
        tanggal_pinjam TEXT,
        tanggal_kembali TEXT
    )
    """)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_tables()
    print("Database dah dibuat nih..")