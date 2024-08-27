# import flast module
from flask import Flask, render_template
import CPUStatpage

# instance of flask application
app = Flask(__name__)

# initialise variables
temp = CPUStatpage.tempcheck()
mem = CPUStatpage.memcheck()

# home route that returns below text when root url is accessed
@app.route("/")
def hello_world():
    return render_template('index.html', temp = temp, mem = mem) 

if __name__ == '__main__':  
   app.run(debug=True)  