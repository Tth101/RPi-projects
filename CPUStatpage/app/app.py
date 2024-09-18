from flask import Flask, render_template, redirect, g #g allows for global variables
import CPUStatpage
import sqlite3

DATABASE = '../database/cpu-stats-app.db'
app = Flask(__name__) # instance of flask application
temp, mem = 0, 1 

# Database operations
def get_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT * FROM cpustats")
    rows = c.fetchall()
    conn.close()
    print(rows)
    return rows

def insert_db(conn, data):
    sql = '''INSERT INTO cpustats (temp, mem, date)
    VALUES(?, ?, 'now')'''
    c = conn.cursor()
    c.execute(sql, data)
    conn.commit()
    conn.close()

# home route that returns below text when root url is accessed
@app.route("/")
def index():
    data = str(get_db())
    return render_template('index.html', temp = temp, mem = mem, data = data) 

@app.route("/update")
def generate_stats():
    conn = sqlite3.connect(DATABASE)
    data = (CPUStatpage.tempcheck(), CPUStatpage.memcheck())
    insert_db(conn, data)
    return data

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__main__':  
    app.run(debug=True)  