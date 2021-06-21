import json
from flask import Flask, jsonify, request, make_response
from flask_jwt_extended import *
import jwt
import datetime
import bcrypt
from functools import wraps

app = Flask(__name__)

app.config['SECRET_KEY'] = 'playplay'

def token_req(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')

        if not token:
            return jsonify({'message' : 'Token is missing!'}), 403
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'message' : 'Token is invalid!'}), 403

        return f(*args, **kwargs)
    return decorated


@app.route('/unprotected')
def unprotected():
    return jsonify({'message' : 'Anyone can view this!'})

@app.route('/protected')
@token_req
def protected():
    return jsonify({'message' : 'This is only available for people'})

@app.route('/login')
def login():
    auth = request.authorization

    if auth and auth.password == 'password':
        token = jwt.encode({'user' : auth.username, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(seconds=60)}, app.config['SECRET_KEY'])
        return jsonify({'token' : token})

    return make_response('bad',401,{'WWW-Authenticate' : 'Basic realm="Login Required"'})

if __name__ == '__main__':
    app.run(debug = True, host="127.0.0.1", port="5000" )
