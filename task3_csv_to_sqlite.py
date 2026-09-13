import csv
import sqlite3
connection=sqlite3.connect('user.db')
cursor=connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT)""")
cursor.execute("DELETE FROM users")
with open("users.csv", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        name = row["name"]
        email = row["email"]

        cursor.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            (name, email)
        )


connection.commit()

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print(row)

connection.close()