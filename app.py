from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

# App Key
app.config['SECRET_KEY'] = '199d90ba0aea5095c1a0fe03b5f70e96'

posts = [
    {
        "author": "Po'okela Moana",
        "title" : "Blog Post 1",
        "content": "First Post Content",
        "date_posted": "November 11, 2020"

    },
    {
        "author": "Petr",
        "title" : "Blog Post 2",
        "content": "First Post Content",
        "date_posted": "November 12, 2020",

    }
]


@app.route("/")
@app.route("/home")
def hello():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title='About')

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title='Login', form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template("register.html", title='Register', form=form)



if __name__ == "__main__":
    app.run(debug=True)