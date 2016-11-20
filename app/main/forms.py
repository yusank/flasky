#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
'''
 @Author:      yusank
 @Email:       yusankurban@gmail.com
 @DateTime:    2016-11-04 17:09:06
 @Description: app/main/forms.py 
'''
from flask_wtf import Form
from wtforms import StringField, SubmitField,TextAreaField, BooleanField, SelectField
from wtforms.validators import Required, Length, Regexp, Email
from wtforms import ValidationError
from ..models import User, Role
from flask_pagedown.fields import PageDownField

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')
class EditProfileForm(Form):
	name = StringField('Real name', validators = [Length(0,64)])
	location = StringField('Location', validators = [Length(0,64)])
	about_me = TextAreaField('About me')
	submit = SubmitField('Submit')
		
class EditProfileAdminForm(Form):
	email = StringField('Email', validators = [Required(), Length(1,64),Email()])
	username = StringField('Username', validators = [Required(), Length(1,64), Regexp('^[A-Za-z][A-Za-z0-p_.]*$',0,
																						'Username must have only letters,'
																						'numbers,dots or underscores')])
	confirmed = BooleanField('confirmed')
	role = SelectField('Role', coerce = int)
	name = StringField('Real name', validators = [Length(0,64)])
	location = StringField('Location', validators = [Length(0,64)])
	about_me = TextAreaField('About me')
	submit = SubmitField('Submit')

	def __init__(self, user, *args, **kwargs):
		super(EditProfileAdminForm,self).__init__(*args, **kwargs)
		self.role.choices = [(role.id, role.name) for role in Role.query.order_by(Role.name).all()]
		self.user = user

	def validate_email(self, field):
		if field.data != self.user.email and User.query.filter_by(email = field.data).first():
			raise ValidationError('Email already registered.')

	def validate_username(self, field):
		if field.data != self.user.username and user.query.filter_by(username = field.data).first():
			raise ValidationError('Username already in use.')

class PostForm(Form):
	body = PageDownField('what`s new recently?', validators = [Required()])
	submit = SubmitField('Submit')

class CommentForm(Form):
	body = StringField('', validators = [Required()])
	submit = SubmitField('Submit')