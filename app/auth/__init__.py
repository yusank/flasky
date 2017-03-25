#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
'''
 @Author:      yusank
 @Email:       yusankurban@gmail.com
 @DateTime:    2016-11-04 10:59:19
 @Description: app/auth/__init__.py 
'''
from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views