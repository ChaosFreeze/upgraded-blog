from flask import Flask, render_template, request
import requests
import smtplib
from datetime import date

npoint_url = 'https://api.npoint.io/a695600da11dfa61ec4f'
OWN_EMAIL = 'YOUR EMAIL'
OWN_PASSWORD = 'YOUR PASSWORD'
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


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact Page."""
    if request.method == 'POST':
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template('contact.html', year=year, msg_sent=True)
    return render_template('contact.html', year=year, msg_sent=False)


@app.route('/post')
def post():
    """Post Page"""
    return render_template('post.html')


def send_email(name, email, phone, message):
    # if you get UnicodeEncodeError
    # try {message}".encode("utf-8")
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)


if __name__ == '__main__':
    today = date.today()
    year = today.year
    month = today.month
    app.run(debug=True)
