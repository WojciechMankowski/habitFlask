from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

user_page = Blueprint('users', __name__, template_folder='templates')


@user_page.route('/login')
def login():
    try:
        return render_template('login.html')
    except TemplateNotFound:
        abort(404)


@user_page.route('register')
def register():
    try:
        return render_template('register.html')
    except TemplateNotFound:
        abort(404)
