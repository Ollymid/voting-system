from flask import Flask, request, redirect
from werkzeug.contrib.cache import SimpleCache


app = Flask(__name__)
cache = SimpleCache()

@app.route('/')
def index():
	ideas = cache.get('ideas') or []
	return f"""{ideas}<br>
	  <form action=/submit method=post>
	  <input name=idea>
	  <input type=submit value=submit>
	  </form>
	  <a href="/first_round_voting">finish submitting proposals</a>
	"""


@app.route('/submit', methods=['POST'])
def submit_idea():
	ideas = cache.get('ideas') or []
	idea = request.form['idea']
	ideas.append(idea)
	cache.set('ideas', ideas, timeout=0)
	return redirect('/')


@app.route('/first_round_voting')
def voting():
	ideas = cache.get('ideas') or []
	links = []
	for i, idea in enumerate(ideas):
		link = f'<a href="/vote?index={i}">{idea}</a>'
		links.append(link)

	return f"<br>".join(links)




# @app.route('/second_round_voting')
# def hello():
# 	 return 'Hello, World'
