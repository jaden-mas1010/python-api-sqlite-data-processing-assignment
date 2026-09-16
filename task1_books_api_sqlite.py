import requests
import sqlite3
url ='https://openlibrary.org/search.json?q=python'
try:
    response = requests.get(url,timeout=10)
    response.raise_for_status()
except requests.exceptions.RequestException:
    print("API request failed")
    exit()

data=response.json() 
connection=sqlite3.connect('book.db')
cursor=connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, author TEXT,year INTEGER)""")
cursor.execute("DELETE FROM books")
for book in data["docs"]:
    title=book.get("title","Unknown Title")
    author= book.get("author_name",["Unknown Author"])
    author=", ".join(author)
    year=book.get("first_publish_year")

    cursor.execute("INSERT INTO books (title,author,year) VALUES (?,?,?)",(title,author,year))

connection.commit()
cursor.execute("SELECT * FROM books")
rows=cursor.fetchall()
for row in rows:
    print(row)
connection.close()
