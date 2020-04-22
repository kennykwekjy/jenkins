from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
@app.route('/tbank/')
def hello_world():
    return jsonify(
        status = "success",
        data = "tBank API is up and running."
    ), 200
#djjdj
@app.route('/tbank/<username>') # dynamic route
def hello_user(username):
    return jsonify(
        status = "success",
        data = "User " + username + " is currently active. 123"
    ), 200

  
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
