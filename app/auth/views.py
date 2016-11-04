#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
'''
 @Author:      yusank
 @Email:       yusankurban@gmail.com
 @DateTime:    2016-11-04 11:02:43
 @Description: Description 
'''
from flask_login import login_user, logout_user, login_required
from flask import render_template, redirect, request, url_for, falsh
from . import auth
from ..models import User
from .forms import LoginForm

@auth.route('/login', methods = ['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validata_on_submit():
		user = User.query.filter_by(email = form.email.data).first()
		if user is not None and user.varify_password(form.password.data):
			login_user(user,form.remember_me.data)
			return redirect(request.args.get('next') or url_for('main.index'))
		falsh('Invalid username or password.')
	return render_template('auth/login.html', form = form)

@auth.route('/register', methods = ['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validata_on_submit():
		user = User(email = form.email.data,username = form.username.data, password = form.password.data)
		db.session.add(user)
		flash('you can now login .')
		render_template(url_for('auth.login'))
	return render_template('auth/register.html', form = form)

@auth.route('/logout')
@login_required
def logout():
	logout_user()
	flash('You have been logged out.')
	return redirect(url_for('main.index'))