import sqlite3

def connect():
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS routine (Id INTEGER PRIMARY kEY, DueDate TEXT, Work1 TEXT, Work2 TEXT, Work3 TEXT)")
    conn.commit()
    conn.close()

def insert(DueDate, Work1, Work2, Work3):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO routine VALUES(NULL, ?,?,?,?)", (DueDate, Work1, Work2, Work3))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM routine WHERE id = ?", (id,))
    conn.commit()
    conn.close()

def search(DueDate = '', Work1 = '', Work2 = '', Work3 = ''):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine WHERE DueDate = ? or Work1 = ? or Work2 = ? or Work3 = ?", (DueDate, Work1, Work2, Work3))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

connect()