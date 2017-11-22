# -*- coding: utf-8 -*-

import re, time, json, logging, hashlib, base64, asyncio

import markdown2

from aiohttp import web

from coroweb import get, post
from apis import Page,APIValueError, APIResourceNotFoundError

from models import User, Comment, Blog, next_id
from config import configs


# 博客页
@get('/blog/{id}')
async def get_blog(id):
    blog = await Blog.find(id)
    comments = await Comment.findAll('blog_id=?', [id], orderBy='created_at desc')
    for c in comments:
        c.html_content = text2html(c.content)
    blog.html_content = markdown2.markdown(blog.content)
    return {
        '__template__': 'blog.html',
        'blog': blog,
        'comments': comments
    }

# 博客列表页
@get('/manage/blogs')
async def manage_blogs(*, page='1'):
    return {
        '__template__': 'manage_blogs.html',
        'page_index': get_page_index(page)
    }

# 创建博客页
@get('/manage/blogs/create')
async def manage_create_blog():
    return {
        '__template__': 'manage_blog_edit.html',
        'id': '',
        'action': '/api/blogs'
    }

# 修改博客页
@get('/manage/blogs/update/{id}')
async def manage_update_blog():
    blog = await Blog.find(id)
    return {
        '__template__': 'manage_blog_edit.html',
        'id': blog.id,
        'action': '/api/blogs',
        'blog':blog
    }

# 评论列表页
@get('/manage/comments')
async def manage_comments(*, page='1'):
    return {
        '__template__': 'manage_comments.html',
        'page_index': get_page_index(page)
    }

# 用户列表页
@get('/manage/users')
async def manage_users(*, page='1'):
    return {
        '__template__': 'manage_users.html',
        'page_index': get_page_index(page)
    }
