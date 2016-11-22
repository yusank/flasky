#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
'''
 @Author:      yusank
 @Email:       yusankurban@gmail.com
 @DateTime:    2016-11-21 15:10:48
 @Description: app/api_1_0/comments.py 
'''
from flask import jsonify, request, g, url_for, current_app
from .. import db
from ..models import Post, Permission, Comment
from . import api
from .decorators import permission_required

@api.route('/comments/')
def get_comments():
	page = request.args.get('page', 1, type = int)
	pagination = Comment.query.order_by(Comment.timestamp.desc()).paginate(
		page, per_page = current_app.config['FLASKY_COMMENTS_PER_PAGE'],
		error_out = False)
	comments = pagination.items
	prev = None
	if pagination.has_prev:
		prev = url_for('api.get_comments', page = page - 1, _external = True)
	next = None
	if pagination.has_next:
		next = url_for('api.get_comments', page = page + 1, _external = True)
	return jsonify({
		'comments': [comment.to_json() for comment in comments],
		'prev': prev,
		'next': next,
		'count': pagination.total
		})

@api.route('/comments/<int:id>')
def get_comment(id):
	comment = Comment.query.get_or_404(id)
	return jsonify(comment.to_json())

@api.route('/posts/<int:id>/comments')
def get_post_comments(id):
	post = Post.query.get_or_404(id)
	page = request.args.get('page', 1, type = int)
	pagination =post.comments.order_by(Comment.timestamp.asc()).paginate(
		page, per_page = current_app.config['FLASKY_COMMENTS_PER_PAGE'],
		error_out = False)
	comments = pagination.items
	prev = None
	if pagination.has_prev:
		prev = url_for('api.get_post_comments', page = page - 1, _external = True)
	next = None
	if pagination.has_next:
		next = url_for('api.get_post_comments', page = page + 1, _external = True)
	return jsonify({
		'comments': [comment.to_json() for comment in comments],
		'prev': prev,
		'next': next,
		'count': pagination.total
		})