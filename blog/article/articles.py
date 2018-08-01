from flask import Blueprint, request, render_template, url_for, redirect
from .forms import ArticlePublicForm

articles = Blueprint('articles', __name__, template_folder='temp', url_prefix='/article')


@articles.route('/public', methods=['GET', 'POST'], strict_slashes=False, endpoint='public')
def public():
    if request.method == 'GET':
        form = ArticlePublicForm()
        return render_template('public.html', form=form)
    elif request.method == 'POST':
        pass