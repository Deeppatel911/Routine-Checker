import sqlite3

def connect():
    conn=sqlite3.connect('routine.db')
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS routine(ID INTEGER PRIMARY KEY, Date TEXT, Expenditure INTEGER, Exercise TEXT, Study TEXT, Diet TEXT, Coding TEXT)")
    conn.commit()
    conn.close()

def insert(date,expenditure,exercise,study,diet,coding):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO routine VALUES(NULL,?,?,?,?,?,?)", (date, expenditure, exercise, study, diet, coding))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine")
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM routine WHERE ID=?",(id,))
    conn.commit()
    conn.close()

def search(date='',expenditure='',exercise='',study='',diet='',coding=''):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine WHERE Date=? OR Expenditure=? OR Exercise=? OR Study=? OR Diet=? OR Coding=?",(date,expenditure,exercise,study,diet,coding))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

connect()