# -*- coding: utf-8 -*-

import re, time, json, logging, hashlib, base64, asyncio

import markdown2

from aiohttp import web

from coroweb import get, post
from apis import Page,APIValueError, APIResourceNotFoundError

from models import User, Comment, Blog, next_id
from config import configs


COOKIE_NAME = 'awesession'
_COOKIE_KEY = configs.session.secret

# 首页
@get('/')
async def index(request):
    summary = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
    # todo 以后将这里的信息替换为从数据库中取
    blogs = await Blog.findAll()
    resultList = []
    for blog in blogs:
        resultList.append(Blog(id=blog.id, name=blog.name, summary=blog.summary, created_at=blog.created_at))
    return {
        '__template__': 'blogs.html',
        'blogs': resultList
    }

# 注册信息页
@get('/register')
def register():
    return {
        '__template__': 'register.html'
    }

# 登录页
@get('/signin')
def signin():
    return {
        '__template__': 'signin.html'
    }

# 登出
@get('/signout')
def signout(request):
    referer = request.headers.get('Referer')
    r = web.HTTPFound(referer or '/')
    r.set_cookie(COOKIE_NAME, '-deleted-', max_age=0, httponly=True)
    logging.info('user signed out.')
    return r
