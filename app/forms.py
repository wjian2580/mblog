# -*- encoding: utf-8 -*-
from flask_wtf import Form
from wtforms import StringField,BooleanField
from wtforms.validators import DataRequired

# åå»ºç»éè¡¨åï¼éè¿openidæ ¡éªï¼
class LoginForm(Form):
	openid = StringField('openid',validators=[DataRequired()])
	remember_me = BooleanField('remember_me',default=False)
