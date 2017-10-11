# -*- encoding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,TextAreaField
from wtforms.validators import DataRequired,length

class LoginForm(FlaskForm):
	openid = StringField('openid',validators=[DataRequired()])
	remember_me = BooleanField('remember_me',default=False)

from app.models import User

class EditForm(FlaskForm):
    nickname = StringField('nickname', validators=[DataRequired()])
    about_me = TextAreaField('about_me', validators=[length(min=0, max=140)])

    def __init__(self, original_nickname, *args, **kwargs):
        FlaskForm.__init__(self, *args, **kwargs)
        self.original_nickname = original_nickname

    def validate(self):
        if not FlaskForm.validate(self):
            return False
        if self.nickname.data == self.original_nickname:
            return True
        user = User.query.filter_by(nickname=self.nickname.data).first()
        if user != None:
            self.nickname.errors.append('昵称存在了哦，换一个试试吧~')
            return False
        return True
