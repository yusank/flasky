#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
'''
 @Author:      yusank
 @Email:       yusankurban@gmail.com
 @DateTime:    2016-11-04 10:45:46
 @Description: Description 
'''
import unittest
from app.models import User

class UserModelTestCase(unittest.TestCase):
	def test_password_setter(self):
		u = User(password = 'abc')
		self.assertTrue(u.password_hash is not None)

	def test_no_password_getter(self):
		u = User(password = 'abc')
		with self.assertRaises(AttributeError):
			u.password

	def test_password_verification(self):
		u = User(password = 'abc')
		self.assertTrue(u.verify_password('abc'))
		self.assertFalse(u.verify_password('efg'))

	def test_password_salts_are_random(self):
		u = User(password = 'abc')
		u2 = User(password = 'abc')
		self.assertTrue(u.password_hash != u2.password_hash)