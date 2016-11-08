#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
'''
 @Author:      yusank
 @Email:       yusankurban@gmail.com
 @DateTime:    2016-11-03 16:30:43
 @Description: app/main/views.py 
'''
from flask import render_template
from . import main
from decorators import admin_required, permission_required
from .models import Permission


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/admin')
@login_required
@admin_required
def for_admin_only():
	return "For Admistrator!!!"

@main.route('/moderator')
@login_required
@permission_required(Permission.MODERATE_COMMIT)
def for_moderators_only():
	return "For comment moderators!"