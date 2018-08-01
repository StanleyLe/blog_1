from wtforms import widgets, validators, Form
from wtforms.fields import simple, IntegerField, StringField


class ArticlePublicForm(Form):

    title = simple.StringField(
        label='文章标题',
        validators=[
            validators.DataRequired(message='文章标题不能为空'),
        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'control'},
    )
    content = simple.TextAreaField(
        label='文章内容',
        validators=[
            validators.DataRequired(message='文章内容不能为空'),
            validators.length(min=20, message='文章字数不能少于20字'),
        ],
        widget=widgets.TextArea(),
        render_kw={'class': 'control'},
    )