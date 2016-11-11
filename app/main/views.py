#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
'''
 @Author:      yusank
 @Email:       yusankurban@gmail.com
 @DateTime:    2016-11-03 16:30:43
 @Description: app/main/views.py 
'''
from flask import render_template,abort
from . import main


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/user/<username>')
def user(username):
	user = User.query.filter_by(username = username).first_or_404()
	return render_template('user.html', user = user)