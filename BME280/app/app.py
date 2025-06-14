from flask import Flask, render_template, redirect, json, g #g allows for global variables
import BME280
import sqlite3

DATABASE = '../database/bme280-app.db'
app = Flask(__name__) # instance of flask application
temp, pressure, humidity = 0.0, 0.0, 0.0

# Database operations
def get_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT * FROM BME280")
    rows = c.fetchall() 
    conn.close()
    if rows == None:
        return None 
    return rows

def insert_db(conn, data):
    sql = '''INSERT INTO BME280 (temp, pressure, humidity, date)
    VALUES(?, ?, ?, DATETIME('now'))'''
    c = conn.cursor()
    c.execute(sql, data)
    conn.commit()
    conn.close()

# routes
@app.route("/")
def index():
    data = get_db()
    if data == []:
        generate_stats()
    
    if data == None:
        print("app.py: app.route(\"/\") data = None")

    else:
        lasttuple = data[len(data) - 1]
        temp, pressure, humidity, date = lasttuple[1], lasttuple[2], lasttuple[3], lasttuple[4]
    return render_template('index.html', temp = temp, pressure = pressure, humidity = humidity, date = date, data=data) 

@app.route("/update")
def generate_stats():
    conn = sqlite3.connect(DATABASE)
    dataArr = BME280.readSurrounding()
    data = (dataArr[0], dataArr[1], dataArr[2])
    insert_db(conn, data)
    return redirect("/")

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__main__':  
    app.run(debug=True)  