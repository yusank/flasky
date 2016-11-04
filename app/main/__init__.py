#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
'''
 @Author:      yusank
 @Email:       yusankurban@gmail.com
 @DateTime:    2016-11-03 16:22:33
 @Description: app/main/__init__.py 
'''
from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors