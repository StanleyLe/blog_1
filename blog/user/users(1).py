from flask import Blueprint, request, render_template, redirect, session, url_for, get_flashed_messages
from werkzeug.security import generate_password_hash, check_password_hash
from .forms import RegisterForm, LoginForm
from .models import OperationDB, Users

users = Blueprint('users', __name__, url_prefix='/users', template_folder='temp')


@users.route('/register', methods=['GET', 'POST'], strict_slashes=False)
def register():
    if request.method == 'GET':
        form = RegisterForm()
        return render_template('register.html', form=form)
    elif request.method == 'POST':
        form = RegisterForm(formdata=request.form)
        if form.validate():
            user = OperationDB()
            param = Users(username=form.username.data, password=generate_password_hash(form.pwd.data), email=form.email.data)
            user.add_one(param)
            return render_template('login.html', message='注册成功, 赶快尝试登陆吧!')
        return render_template('register.html', form=form)


@users.route('/login', methods=['GET', 'POST'], strict_slashes=False, endpoint='login')
def login():
    if request.method == 'GET':
        next = request.args.get('next', None)
        form = LoginForm()
        if not next:
            next = '/'
            return render_template('login.html', form=form, next=next)
        return render_template('login.html', form=form, next=next)
    elif request.method == 'POST':
        form = LoginForm(formdata=request.form)
        next = request.form.get('next')
        if form.validate:
            user = OperationDB()
            username = form.username.data
            user_list = user.query_all(Users, param=Users.username == username)
            # 判断列表是否为空
            if user_list:
                # 判断两次密码是否一致
                if check_password_hash(user_list[0].password, form.password.data):
                    print()
                    session['login_user'] = user_list[0]
                    print(333333333333333233333, next)
                    return redirect(next)
        return render_template('login.html', form=form, next=next, message='账户或密码不正确, 请重新输入')


@users.route('/', methods=['GET'], strict_slashes=False, endpoint='index')
def index():
    return render_template('index.html')


@users.route('/info', methods=['GET', 'POST'], strict_slashes=False, endpoint='info')
def info():
    if request.method == 'GET':
        user = session['login_user']
        return render_template('info.html', user=user)


@users.route('/update_info', methods=['GET', 'POST'], strict_slashes=False, endpoint='update_info')
def update_info():
    if request.method == 'GET':
        user = session['login_user']
        return render_template('update_info.html', user=user)
    elif request.method == 'POST':
        pass


@users.route('/logout', methods=['GET', 'POST'], strict_slashes=False)
def logout():
    if request.method == 'GET':
        del session['login_user']
        return redirect('/')

