#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
'''
 @Author:      yusank
 @Email:       yusankurban@gmail.com
 @DateTime:    2016-11-03 18:04:23
 @Description: app/models.py 
'''

import os
from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask_migrate import Migrate, MigrateCommand
from werkzeug.security import generate_password_hash, check_password_hash
from flask_script import Shell
from flask_login import UserMixin
from . import login_manager,db


class Permission:
    FOLLOW = 0x01
    COMMENT = 0x02
    WRITE_ARTICLES = 0x04
    MODERATE_COMMENTS = 0x08
    ADMINISTER = 0x80


class Role(db.Model):
	__tablename__ = 'roles'
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(64), unique = True)
	default = db.Column(db.Boolean, default = False, index = True)
	permissions = db.Column(db.Integer)
	users = db.relationship('User', backref='role', lazy='dynamic')

	@staticmethod
	def insert_roles():
		roles = {
			'User':(Permission.FOLLOW | Permission.COMMENT | Permission.WRITE_ARTICLES, True),
			'Moderator':(Permission.FOLLOW | Permission.COMMENT | Permission.WRITE_ARTICLES | Permission.MODERATE_COMMENTS, False),
			'Administrator':(0xff, False)
		}
		for r in roles:
			role = Role.query.filter_by(name = r).first()
			if role is None:
				role = Role(name = r)
			role.permissions = roles[r][0]
			role.default = roles[r][1]
			db.session.add(role)
		db.session.commit()

	def __repr__(self):
		return '<Role %r>' % self.name


class User(UserMixin,db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key = True)
	email = db.Column(db.String(64),unique = True, index = True)
	username = db.Column(db.String(64), unique = True, index = True)
	password_hash = db.Column(db.String(128))
	role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
	confirmed = db.Column(db.Boolean, default = False)

	@property
	def password(self):
		raise AttributeError('password is not readable attribute')

	@password.setter
	def password(self,password):
		self.password_hash = generate_password_hash(password)
	

	def verify_password(self,password):
		return check_password_hash(self.password_hash,password)

	def generate_confirmation_token(self, expiration = 3600):
		s = Serializer(current_app.config['SECRET_KEY'], expiration)
		return s.dumps({'confirm':self.id})

	def confirm(self,token):
		s = Serializer(current_app.config['SECRET_KEY'])
		try:
			data  = s.loads(token)
		except:
			return False
		if data.get('confirm') != self.id:
			return False
		self.confirmed = True
		db.session.add(self)
		return True

	def __init__(self,**kwargs):
		super(User, self).__init__(**kwargs)
		if self.role is None:
			if self.email == current_app.config['FLASKY_ADMIN']:
				self.role = Role.query.filter_by(permissions = 0xff).first()
			if self.role is None:
				self.role = Role.query.filter_by(default = True).first()

	def is_authenticated(self):
		return True

	def __repr__(self):
		return '<User %r>' % self.username

	@login_manager.user_loader
	def load_user(user_id):
		return User.query.get(int(user_id))

	def can(self, permissions):
		return self.role is not None and (self.role.permissions & permissions) == permissions
	def is_adminstrator(self):
		return self.can(Permission.ADMINISTER)

class AnonymousUser(AnonymousUserMixin):
	def can(self,permissions):
		return False

	def is_adminstrator(self):
		return False

login_manager.Anonymous_user = AnonymousUser