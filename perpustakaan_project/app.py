from flask import Flask, render_template
from database import connect
#Yang ini bebas kamu ubah Aida, rombak aja

app = Flask(__name__)

@app.route("/")
def dashboard():

    conn = connect()
    cursor = connect.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM siswa"
    )
    siswa = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM buku"
    )
    buku = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM peminjaman"
    )
    pinjam = cursor.fetchone()[0]

    conn.close()

    return render_template(
        "index.html",
        siswa=siswa,
        buku=buku,
        pinjam=pinjam
    )

if __name__ == "__main__":
    app.run(debug=True)