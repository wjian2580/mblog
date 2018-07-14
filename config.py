import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

CSRF_ENABLED = True
SECRET_KEY = 'P@$$wr0d'

OPENID_PROVIDERS = [
    { 'name': 'StackExchange', 'url': 'https://openid.stackexchange.com' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]

# mail server settings
MAIL_SERVER = 'smtp.163.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'wjian2580@163.com'
MAIL_PASSWORD = ''

# administrator list
ADMINS = ['wjian2580@163.com','wangjian0414@rayootech.com','501260495@qq.com']

# 翻页：每页的博客数目
POSTS_PER_PAGE = 10
