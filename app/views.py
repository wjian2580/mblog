from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'name':'Jim'}
	posts = [
		{
			"author":{"name":"Sam"},
			"message":"hahahahah"
		},
		{
			"author":{"name":"Kik"},
			"message":"nnnsssssss"
		}
	]
	return render_template('index.html',
		user=user,
		posts=posts,
		title='title'
		)