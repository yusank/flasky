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


@main.route('/')
def index():
    return render_template('index.html')
