from flask import Flask, render_template, redirect, json, g #g allows for global variables
import CPUStatpage
import sqlite3
import re

DATABASE = '../database/cpu-stats-app.db'
app = Flask(__name__) # instance of flask application
temp, mem = 0, 0

# Database operations
def get_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT * FROM cpustats")
    rows = c.fetchall() 
    conn.close()
    return rows

def insert_db(conn, data):
    sql = '''INSERT INTO cpustats (temp, mem, date)
    VALUES(?, ?, DATETIME('now'))'''
    c = conn.cursor()
    c.execute(sql, data)
    conn.commit()
    conn.close()

# home route that returns below text when root url is accessed
@app.route("/")
def index():
    data = get_db()
    if data == []:
        generate_stats()

    else:
        lasttuple = data[len(data) - 1]
        temp = lasttuple[1]
        print(lasttuple[2])
        mem = lasttuple[2].strip("'") # "Unstringing" list
        print(mem)
        date = lasttuple[3]
    return render_template('index.html', temp = temp, mem = mem, date = date, data = data) 

@app.route("/update")
def generate_stats():
    conn = sqlite3.connect(DATABASE)
    data = (CPUStatpage.tempcheck(), str(CPUStatpage.memcheck()))
    insert_db(conn, data)
    return redirect("/")

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__main__':  
    app.run(debug=True)  