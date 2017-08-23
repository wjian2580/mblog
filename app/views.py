'''
from flask import render_template
from app import app
@app.route('/')
@app.route('/index')
def index():
    user = {'name':'Jim'}
    title = 'myblog'
    posts = [
	{
	    "author":{"name":"Sam"},
	    "message":"hahahahah"
	},
	{
	    "author":{"name":"Jam"},
	    "message":"nnnsssssss"
	}
    ]
    return render_template('index.html',
        user=user,
	posts=posts,
	title=title
	)
'''
from flask import render_template
from app import app
from .forms import LoginForm

@app.route('/login',methods = ['get','post'])
def login():
	form = LoginForm()
	return render_template('login.html',
		title = 'login in',
		form = form)
