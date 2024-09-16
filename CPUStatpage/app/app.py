from flask import Flask, render_template, g #g allows for global variables
import CPUStatpage
import sqlite3

DATABASE = '/path'

# instance of flask application
app = Flask(__name__)

# initialise variables
temp, mem = 0, 1

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_stats(temp, mem):
    temp = CPUStatpage.tempcheck()
    mem = CPUStatpage.memcheck()
    return temp, mem

def update_temperature(redis_connection):
    current_temperature = CPUStatpage.tempcheck()
    redis_connection.set("currentCPUTemperature", current_temperature)

# home route that returns below text when root url is accessed
@app.route("/")
def index():
    cur = get_db().cursor()
    return render_template('index.html', temp = init_stats().temp, mem = mem) 

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM cpustats")
    return cursor.fetchall()


if __name__ == '__main__':  
    app.run(debug=True)  