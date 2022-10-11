from flask import Flask, render_template
import requests
from datetime import date

npoint_url = 'https://api.npoint.io/a695600da11dfa61ec4f'
posts = requests.get(npoint_url).json()
app = Flask(__name__)


@app.route('/')
@app.route('/index.html')
def get_all_posts():
    """Landing Page."""
    return render_template('index.html', all_posts=posts, year=year, month=month)


@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post['id'] == index:
            requested_post = blog_post
    return render_template('post.html', post=requested_post, year=year)


@app.route('/about')
def about():
    """About Page."""
    return render_template('about.html', year=year)


@app.route('/contact')
def contact():
    """Contact Page."""
    return render_template('contact.html', year=year)


@app.route('/post')
def post():
    """Post Page"""
    return render_template('post.html')


if __name__ == '__main__':
    today = date.today()
    year = today.year
    month = today.month
    app.run(debug=True)
