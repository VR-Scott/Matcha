from flask import Flask, render_template, url_for, flash #import a class Flask,
from forms import RegistrationForm, LoginForm
#make var app = to new instance of the class Flask.
app = Flask(__name__) #__name__ is a special variable name of the module.
#what we type into browser to go to diff pages.

app.config['SECRET_KEY'] = '544f8b85f0bed827ec66b3ea5fe01777'

posts = [
    {
        'author': 'Vaughan Scott',
        'title': 'Blog Post 1', 
        'content': 'First post content',
        'date_posted': 'Nov 26 2019'
    },
    {
        'author': 'Bob Scott',
        'title': 'Blog Post 2', 
        'content': 'Second post content',
        'date_posted': 'Nov 27 2019'
    }
]

@app.route("/")#root page of site.
@app.route("/home")#home page of site.
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")#about page of site.
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])#register page of site.
def register():
    form = RegistrationForm()
    if form.validate_on_submit()
        flash(f'Account created for {form.username.data}!')
    return render_template('register.html', title='Register', form = form)

@app.route("/login")#login page of site.
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form = form)

#to run: $:export FLASK_APP=flaskblog.py (for mac)
#FLASK_DEBUG=1
#to run: $:set FLASK_APP=flaskblog.py (for windows)

if __name__ == '__main__':
    app.run(debug=True)

#run directly $:python3 flask_blog.py