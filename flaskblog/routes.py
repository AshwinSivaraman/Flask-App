from flask import Flask, render_template, url_for, flash, redirect
from flaskblog.models import User, Post
from flaskblog.forms import LoginForm, RegistrationForm
from flaskblog import app, db, bcrypt

posts = [
    {
        'author': 'ashwin',
        'title': 'blog post 1',
        'content': 'This is my first blog',
        'date': '29 June, 2019'
    },
    {
        'author': 'shiv',
        'title': 'blog post 2',
        'content': 'This is my second blog',
        'date': '30 June, 2019'
    }
    ]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', posts=posts, title='about')

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8 ')
        user = User(username=form.username.data, email=form.email.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created! You can now log in', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Registration', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)