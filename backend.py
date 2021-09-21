import sqlite3

def connect():
    conn=sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book ("
                "id INTEGER PRIMARY KEY,"
                "title text,"
                "author text,"
                "year integer,"
                "isbm integer)")
    conn.commit()
    conn.close()

def insert(title, author, year, isbm):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)",
                (title, author, year, isbm))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title="", author="", year="", isbm=""):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbm=?",
                (title, author, year, isbm))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("DELETE from book where id=?", (id))
    rows = cur.fetchall()
    conn.close()
    return rows

def update(id, title, author, year, isbm):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbm=? WHERE id=?",
                (title, author, isbm, year, id))
    rows = cur.fetchall()
    conn.close()