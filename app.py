from flask import Flask
 
# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)
 

@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello Worldfrom ad-Chekk'
 
# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(host='0.0.0.0', port=5000)
