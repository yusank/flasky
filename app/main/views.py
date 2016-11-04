#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
'''
 @Author:      yusank
 @Email:       yusankurban@gmail.com
 @DateTime:    2016-11-03 16:30:43
 @Description: app/main/views.py 
'''
from datetime import datetime
from flask import render_template, session, redirect, url_for

from . import main
from .forms import NameForm
from .. import db
from ..models import User

@main.route('/', methods = ['GET','POST'])
def index():
	form = NameForm()
	if form.validata_on_subnit():
		#...
		return redirect(url_for('.index'))
	return render_template('index.html',
							form = form,
							name = session.get('name'),
							known = session.get('known',False),
							current_time = datetime.utcnow())