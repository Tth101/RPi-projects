# import flast module
from flask import Flask, render_template
import CPUStatpage

# instance of flask application
app = Flask(__name__)

# initialise the text file storing CPU stats
data = CPUStatpage.init_data()

# home route that returns below text when root url is accessed
@app.route("/")
def hello_world():
    return render_template('index.html', data = data)

if __name__ == '__main__':  
   app.run(debug=True)  