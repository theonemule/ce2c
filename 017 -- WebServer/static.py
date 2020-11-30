#Import the module
from flask import Flask

#__name__ refers to the current method, in this case "__main__"
app = Flask(__name__, static_url_path='', static_folder='')

#This is a decorator that defines a route, a portion of a URL.
#The following method handles the route.
@app.route('/') 
def root():
    return app.send_static_file('index.html')

#Starts the "app".
if __name__ == '__main__':
    app.run()
