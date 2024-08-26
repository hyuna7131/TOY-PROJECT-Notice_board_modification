from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import create_post, update_post, delete_post, get_posts
from pymysql import OperationalError

main = Blueprint('main', __name__)

@main.route('/')
def index():
    try:
        posts = get_posts()
        return render_template('index.html', posts=posts)
    except Exception as e:
        print(f"Error fetching posts: {e}")
        flash('An error occurred while fetching posts. Please try again later.', 'error')
        return render_template('index.html', posts=[])

@main.route('/post/<int:post_id>')
def view_post(post_id):
    try:
        posts = get_posts('id', post_id)
        if not posts:
            flash('Post not found.', 'warning')
            return redirect(url_for('main.index'))
        return render_template('post.html', posts=posts, post_id=post_id)
    except Exception as e:
        print(f"Error fetching post: {e}")
        flash('An error occurred while fetching the post. Please try again later.', 'error')
        return redirect(url_for('main.index'))

@main.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        try:
            title = request.form['title']
            content = request.form['content']
            create_post(title, content)
            flash('Post created successfully!', 'success')
            return redirect(url_for('main.index'))
        except OperationalError as e:
            print(f"Database error: {e}")
            flash('An error occurred while creating the post. Please try again later.', 'error')
        except Exception as e:
            print(f"Unexpected error: {e}")
            flash('An unexpected error occurred. Please try again later.', 'error')
    return render_template('create.html')

@main.route('/edit/<int:post_id>', methods=['GET', 'POST'])
def edit(post_id):
    if request.method == 'POST':
        try:
            title = request.form['title']
            content = request.form['content']
            update_post(post_id, title, content)
            flash('Post updated successfully!', 'success')
            return redirect(url_for('main.view_post', post_id=post_id))
        except OperationalError as e:
            print(f"Database error: {e}")
            flash('An error occurred while updating the post. Please try again later.', 'error')
        except Exception as e:
            print(f"Unexpected error: {e}")
            flash('An unexpected error occurred. Please try again later.', 'error')

    try:
        posts = get_posts('id', post_id)
        if not posts:
            flash('Post not found.', 'warning')
            return redirect(url_for('main.index'))
        return render_template('edit.html', posts=posts, post_id=post_id)
    except Exception as e:
        print(f"Error fetching post for edit: {e}")
        flash('An error occurred while fetching the post for editing. Please try again later.', 'error')
        return redirect(url_for('main.index'))

@main.route('/delete/<int:post_id>', methods=['POST'])
def delete(post_id):
    try:
        delete_post(post_id)
        flash('Post deleted successfully!', 'success')
    except OperationalError as e:
        print(f"Database error: {e}")
        flash('An error occurred while deleting the post. Please try again later.', 'error')
    except Exception as e:
        print(f"Unexpected error: {e}")
        flash('An unexpected error occurred. Please try again later.', 'error')
    return redirect(url_for('main.index'))

@main.route('/search', methods=['GET'])
def search():
    search_type = request.args.get('type')
    keyword = request.args.get('keyword')
    try:
        posts = get_posts(search_type, keyword)
        return render_template('search.html', posts=posts)
    except Exception as e:
        print(f"Error during search: {e}")
        flash('An error occurred while performing the search. Please try again later.', 'error')
        return render_template('search.html', posts=[])