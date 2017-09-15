# -*- encoding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,TextAreaField
from wtforms.validators import DataRequired,length

class LoginForm(FlaskForm):
	openid = StringField('openid',validators=[DataRequired()])
	remember_me = BooleanField('remember_me',default=False)
class EditForm(FlaskForm):
	nickname = StringField('nickname',validators=[DataRequired()])		
	about_me = TextAreaField('about_me',validators=[length(min=0,max=140)])
