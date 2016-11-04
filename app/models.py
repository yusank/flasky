#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
'''
 @Author:      yusank
 @Email:       yusankurban@gmail.com
 @DateTime:    2016-11-03 18:04:23
 @Description: Description 
'''
import os
from flask_migrate import Migrate, MigrateCommand
from werkzeug.security import generate_password_hash, check_password_hash
from flask_script import Shell
from flask_login import UserMixin
from . import login_manager,db

class Role(db.model):
	__tablename__ = 'roles'
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(64), unique = True)

	def __repr__(self):
		return '<Role %r>' % self.name

	users = db.relationship('User', backref = 'role')

class User(UserMixin,db.model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key = True)
	email = db.Column(db.String(64),unique = True, index = True)
	username = db.Column(db.String(64), unique = True, index = True)
	password_hash = db.Column(db.String(128))
	role_id = db.Column(db.Integer, db.Foreignkey('roles.id'))

	def __repr__(self):
		return '<User %r>' % self.username

	@property
	def password(self):
		raise AttributeError('password is not readable attribute')

	@password.setter
	def password(self,password):
		self.password_hash = generete_password_hash(password)
	def verify_password(self,password):
		return check_password_hash(self.password_hash,password)

	@login_manager.user_loader
	def load_user(user_id):
		return User.query.get(int(user_id))