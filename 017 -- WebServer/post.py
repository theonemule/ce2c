#Import the module
from flask import Flask
from flask import request

#__name__ refers to the current method, in this case "__main__"
app = Flask(__name__, static_url_path='', static_folder='')

#This is a decorator that defines a route, a portion of a URL.
#The following method handles the route.
@app.route("/") 
def root():
    return app.send_static_file("input.html")

#The following method handles the route "/name" as a POST request.
@app.route("/name", methods=['POST']) 
def name():
    first = request.form.get("first")
    last = request.form.get("last")
    return "Hello, " + first + " " + last + "!"

#Starts the "app".
if __name__ == '__main__':
    app.run()