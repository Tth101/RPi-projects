from flask import Flask, render_template, g #g allows for global variables
import CPUStatpage
import sqlite3

DATABASE = '../database/cpu-stats-app.db'
app = Flask(__name__) # instance of flask application
temp, mem = 0, 1 

# Database operations
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM cpustats")
    return cursor.fetchall()

def update_db(conn, data):
    sql = ''' INSERT INTO cpustats (temp, mem, date)
    VALUES(?, ?, DATE(now))'''
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()
    return cur.lastrowid

# home route that returns below text when root url is accessed
@app.route("/")
def index():
    data = str(get_db())
    return render_template('index.html', temp = temp, mem = mem, data = data) 

@app.route("/update", methods=['POST'])
def generate_stats():
    try:
        with sqlite3.connect(DATABASE) as conn:
            data = (CPUStatpage.tempcheck(), CPUStatpage.memcheck())
            update_db(conn, data)
    except sqlite3.Error as e:
        print(e)

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__main__':  
    app.run(debug=True)  