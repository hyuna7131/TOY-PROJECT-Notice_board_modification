from flask import Blueprint, render_template, request, redirect, url_for
from app.models import create_post, update_post, delete_post, get_posts

main = Blueprint('main', __name__)

@main.route('/')
def index():
    posts = get_posts()
    return render_template('index.html', posts=posts)

@main.route('/post/<int:post_id>')
def view_post(post_id):
    posts = get_posts('id', post_id)
    return render_template('post.html', posts=posts, post_id=post_id)

@main.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        create_post(title, content)
        return redirect(url_for('main.index'))
    return render_template('create.html')

@main.route('/edit/<int:post_id>', methods=['GET', 'POST'])
def edit(post_id):
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        update_post(post_id, title, content)
        return redirect(url_for('main.view_post', post_id=post_id))
    posts = get_posts('id', post_id)
    return render_template('edit.html', posts=posts, post_id=post_id)

@main.route('/delete/<int:post_id>', methods=['POST'])
def delete(post_id):
    delete_post(post_id)
    return redirect(url_for('main.index', post_id=post_id))

@main.route('/search', methods=['GET'])
def search():
    search_type = request.args.get('type')
    keyword = request.args.get('keyword')
    posts = get_posts(search_type, keyword)
    return render_template('search.html', posts=posts)