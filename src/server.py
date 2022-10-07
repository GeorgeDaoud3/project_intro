from flask import Flask
server = Flask(__name__)
from flask import request
counter = 0
calls=0
@server.route("/")
def hello():
    global calls
    calls=calls+1
    return "Hello World!"

@server.route("/inc")
def inc():
    global counter,calls
    counter=counter+1
    calls=calls+1
    return "Done, counter = "+str(counter)

@server.route("/dec")
def dec():
    global counter,calls
    counter=counter-1
    calls=calls+1
    return "Done, counter = "+str(counter)

@server.route("/set")
def set():
    global calls
    calls=calls+1
    try:
        global counter
        v=int(request.args["v"])
        counter=v
        return "Done, counter = "+str(counter)
    except:
        return "failed"

from flask import jsonify

@server.route("/summary")
def summary():
    d = {'calls':calls,'counter':counter}
    return jsonify(d)

if __name__ == "__main__":
   server.run(host='0.0.0.0:5000')

