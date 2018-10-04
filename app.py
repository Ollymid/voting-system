from flask import Flask, request
from werkzeug.contrib.cache import SimpleCache


app = Flask(__name__)
cache = SimpleCache()

@app.route('/')
def index():
	ideas = cache.get('ideas') or []
	ideas_list = ''
	return f"{ideas}<br><form action=/submit method=post><input name=idea></form>"	


@app.route('/submit', methods=['POST'])
def submit_idea():
	ideas = cache.get('ideas') or []
	idea = request.form['idea']
	ideas.append(idea)
	cache.set('ideas', ideas, timeout=0)
	return 'success'


# @app.route('/first_round_voting')
# def hello():
#     return 'Hello, World'

# @app.route('/second_round_voting')
# def hello():
#     return 'Hello, World'