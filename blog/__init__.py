from flask import Flask, request, session, redirect, url_for, flash
from jinja2 import Environment
from flask_session import RedisSessionInterface
from redis import Redis
import functools
from common.common import common
from user.users import users
from article.articles import articles

app = Flask(__name__)
app.secret_key = '123'
conn = Redis(host='127.0.0.1', port=6379)
app.session_interface = RedisSessionInterface(conn, key_prefix='__')
app.register_blueprint(common)
app.register_blueprint(users)
app.register_blueprint(articles)


@app.before_request
def process_request(*args, **kwargs):

    if request.path == '/users/login' or request.path == '/users/register':
        return None
    print(request.path, 2222222222222222)
    user = session.get('login_user')
    if user:
        return None
    flash(request.path)
    return redirect(url_for('users.login', next=request.path))


@app.errorhandler(404)
def error_404(args):
    return '页面没有找到'


def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': reverse,

    })