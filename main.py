from flask import Flask, render_template
import requests

npoint_url = 'https://api.npoint.io/a695600da11dfa61ec4f'
posts = requests.get(npoint_url).json()
app = Flask(__name__)


@app.route('/')
@app.route('/index.html')
def get_all_posts():
    """Landing Page."""
    return render_template('index.html', all_posts=posts)


@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post['id'] == index:
            requested_post = blog_post
    return render_template('post.html', post=requested_post)


@app.route('/about')
def about():
    """About Page."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Contact Page."""
    return render_template('contact.html')


@app.route('/post')
def post():
    """Post Page"""
    return render_template('post.html')


if __name__ == '__main__':
    app.run(debug=True)
