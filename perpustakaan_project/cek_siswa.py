from database import connect

conn = connect()
cursor = conn.cursor()

cursor.execute("SELECT * FROM siswa")

data = cursor.fetchall()

print(data)
conn.close()