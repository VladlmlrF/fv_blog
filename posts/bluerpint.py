from flask import Blueprint, render_template, request
from models import Post, Tag

posts = Blueprint('posts', __name__, template_folder='templates')


@posts.route('/')
def index():
    psts = Post.query.all()
    return render_template('posts.html', psts=psts)

