from wtforms import Form, validators, widgets
from wtforms.fields import simple, html5, core


class RegisterForm(Form):
    username = simple.StringField(
        label='用户名',
        validators=[
            validators.DataRequired(message='用户名不能为空'),
            validators.Length(min=3, max=18, message='用户名长度必须大于%(min)d, 并且小于%(max)d'),
        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'form-control'}

    )
    pwd = simple.PasswordField(
        label='用户密码',
        validators=[
            validators.DataRequired(message='用户密码不能为空'),
            validators.Length(min=6, max=18, message='用户密码的长度必须大于6位字符并且小于18位字符'),
            validators.Regexp(regex='^(?=.*[a-zA-Z])(?=.*[0-9])(?=.*[_]){6,18}', message='用户密码至少包'
                                                                                          '含一个字母一个数字以及一个下划线')
        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'form-control'},
    )
    re_pwd = simple.PasswordField(
        label='重复密码',
        validators=[
            validators.DataRequired(message='重复密码不能为空'),
            validators. EqualTo('pwd', '两次密码输入不一致')
        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'control'},
    )
    email = html5.EmailField(
        label='邮箱',
        validators=[
            validators.DataRequired(message='邮箱不能为空'),
            validators.Email(message='邮箱格式错误')
        ],
        widget=widgets.TextInput(input_type='email'),
        render_kw={'class': 'form-control'},
    )

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

    def validate_pwd_confirm(self, field):
        if field.data != self.data['pwd']:
            # raise validators.ValidationError("密码不一致")  继续后续验证
            raise validators.StopValidation('密码不一致')  # 不再继续验证


class LoginForm(Form):
    username = simple.StringField(
        label='用户名',
        validators=[
            validators.DataRequired(message='用户名不能为空')
        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'control'}
    )
    password = simple.PasswordField(
        label='用户密码',
        validators=[
            validators.DataRequired(message='用户密码不能为空')
        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'control'}
    )


class UpdateInfoForm(Form):
    username = simple.StringField(
        label='用户名',
        validators=[
            validators.DataRequired(message='用户名不能为空'),
            validators.Length(min=3, max=18, message='用户名长度必须大于%(min)d, 并且小于%(max)d'),
        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'form-control'}

    )
    age = simple.StringField(
        label='用户年龄',
        widget=widgets.TextInput(),
        render_kw={'class': 'form-control'}
    )
    hometown = simple.StringField(
        label='用户居住城市',
        widget=widgets.TextInput(),
        render_kw={'class': 'form-control'}
    )