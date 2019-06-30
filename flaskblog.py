from flask import Flask, render_template, url_for
app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)