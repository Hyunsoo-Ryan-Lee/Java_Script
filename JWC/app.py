from flask import Flask, request, jsonify, make_response, render_template,session
import jwt
import datetime
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'encore'

def token_req(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request.args.get('token')

        if not token:
            return jsonify({'message' : 'Token is missing!'})
        try:
            payload = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'message' : 'Token is invalid!'})
    return decorated

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return '현재 로그인 되어 있습니다.'

@app.route('/unprotected')
def unprotected():
    return jsonify({'message' : 'Anyone can view this!'})

@app.route('/protected')
@token_req
def protected():
    return 'JWT is verified. Welcome!'


@app.route('/login', methods=['POST'])
def login():
    if request.form['username'] and request.form['password'] == 'password':
        session['logged_in'] = True
        token = jwt.encode({
            'user' : request.form['username'],
            'experation' : str(datetime.datetime.utcnow() + datetime.timedelta(seconds=120))
        },app.config['SECRET_KEY'])

        return ({'token' : token})
    
    else:
        return make_response('Unable to verify', 403, {'WWW-Authenticate' : 'Basic realm="Login Required"'})

if __name__ == '__main__':
    app.run(debug = True)