from flask import Flask, render_template, redirect, json, g #g allows for global variables
import CPUStatpage, sqlite3, logging

logger = logging.getLogger(__name__)
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
    if rows == None:
        return None 
    logger.info("get_db() rows: %s", rows)   
    return rows

def insert_db(conn, data):
    sql = '''INSERT INTO cpustats (temp, mem, date)
    VALUES(?, ?, DATETIME('now'))'''
    c = conn.cursor()
    c.execute(sql, data)
    conn.commit()
    conn.close()
    logger.info("insert_db() data: %s", data)

# routes
@app.route("/")
def index():
    data = get_db()
    if data == []:
        generate_stats()

    if data == None:
        print("app.py: app.route(\"/\") data: %s", data)

    else:
        lasttuple = data[len(data) - 1]
        temp, mem, date = lasttuple[1], lasttuple[2], lasttuple[3]

    logger.info("app.route(\"/\") data: " + data)
    return render_template('index.html', temp = temp, mem = mem, date = date, data = data) 

@app.route("/update")
def generate_stats():
    conn = sqlite3.connect(DATABASE)
    data = (CPUStatpage.tempcheck(), str(CPUStatpage.memcheck()))
    logger.info("app.route(\"/update\") data: %s", data)
    insert_db(conn, data)
    return redirect("/")

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__main__':  
    app.run(debug=True)  