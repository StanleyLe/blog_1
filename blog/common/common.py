from flask import Blueprint, request, render_template

common = Blueprint('common', __name__, template_folder='temp')


@common.route('/', methods=['GET'])
def index():
    return render_template('index.html')