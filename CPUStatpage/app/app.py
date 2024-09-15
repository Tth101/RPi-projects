from flask import Flask, render_template
import CPUStatpage
import redis

# instance of flask application
app = Flask(__name__)

# initialise variables
temp, mem = 0, 1

def init_stats(temp, mem):
    temp = CPUStatpage.tempcheck()
    mem = CPUStatpage.memcheck()
    return temp, mem

def update_temperature(redis_connection):
    current_temperature = CPUStatpage.tempcheck()
    redis_connection.set("currentCPUTemperature", current_temperature)

# home route that returns below text when root url is accessed
@app.route("/")
def hello_world():
    return render_template('index.html', temp = init_stats().temp, mem = mem) 

if __name__ == '__main__':  
    redis_connection = redis.StrictRedis(host='redis', port=6379, db=0)
    app.run(debug=True)  