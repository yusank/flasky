#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
'''
 @Author:      yusank
 @Email:       yusankurban@gmail.com
 @DateTime:    2016-11-03 16:26:28
 @Description: Description 
'''
from flask import render_template
from . import main

@main.app_errorhandler(404)
def page_not_found(e):
	return render_template('404.html'),404

@main.app_errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'),500