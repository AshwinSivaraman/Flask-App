from flask import Flask, render_template, url_for, flash, redirect
from forms import LoginForm, RegistrationForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'b09a0aacb8df24c6717e11a91f3d7814 '

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
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Registration', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)
     
if __name__ == '__main__':
    app.run(debug=True)