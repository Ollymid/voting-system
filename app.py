from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/first_round_voting')
def hello():
    return 'Hello, World'

@app.route('/first_round_voting')
def hello():
    return 'Hello, World'