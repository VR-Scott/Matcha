import re
from flask import Flask, render_template, url_for, flash, redirect, request #import a class Flask,
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
    errors = []
    val_username = re.match( '^[A-Za-z][A-Za-z0-9]{2,49}$', '')
    val_email = re.match( '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,100}$', '')
    # val_psw = re.match( '^?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d]{6,64}$', '')
    # password = re.match( '?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d]{6,64}$', '')
    details = {
        'username' : '',
        'firstname' : '',
        'lastname' : '',
        'email' : '',
        'psw' : '',
        'psw-repeat' : '',
        'sex': 'bi-sexual',
        'interests': [],
        'flirts' : [],
        'flirted' : [],
        'matched' : [],
        'image_name': 'default.png'
    }
    if request.method == 'POST':
        val_username = re.match( '^[A-Za-z][A-Za-z0-9]{2,49}$', request.form.get('username'))
        val_email = re.match( '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,100}$', request.form.get('email'))
        
        psw_cap = re.search( '[A-Z]', request.form.get('psw'))
        psw_low = re.search( '[a-z]', request.form.get('psw'))
        psw_dig = re.search( '[0-9]', request.form.get('psw'))
        val_psw = re.match( '^[A-Za-z\d]{6,64}$', request.form.get('psw'))
        details['username'] = request.form.get('username')
        # details['firstname'] = request.form.get(“firstname”)
        # details['lastname'] = request.form.get('lastname')
        details['email'] = request.form.get('email')
        details['psw'] = request.form.get('psw')
        details['psw-repeat'] = request.form.get('psw-repeat')
        if not details['username']:
            errors.append('The username cannot be empty')
        if not val_username:
            errors.append('Username must be alphanumeric beginning with a letter and 2-50 characters long.')
        if not details['email']:
            errors.append('The email cannot be empty')
        if not val_email:
            errors.append('Invalid email format')
        if details['psw']:
            if not val_psw:
                errors.append('Password must be alphanumeric and 6-64 characters long')
            if not psw_cap:
                errors.append('Password must contain: an Uppercase')
            if not psw_low:
                errors.append('Password must contain: a Lowercase')
            if not psw_dig:
                errors.append('Password must contain: a Digit')
        else:
            errors.append('The psw cannot be empty')
        if not details['psw-repeat']:
            errors.append('The psw-repeat cannot be empty')
        if details['psw-repeat'] != details['psw']:
            errors.append('The psw-repeat must be the same as psw')
        
        
        # if db.get_user({'username': details['username']}):
        #     errors.append('The username is already taken')
        # if db.get_user({'email' : details['email']}):
        #     errors.append('The email is already taken!')
        # if not errors:
    return render_template('register.html', title='register', details=details, username=val_username,  email=val_email, errors=errors)
            # db.register_user(details)
            # flash (“Successful registration”, 'success')
            # return redirect( url_for('login') )
        # for error in errors:
        #     flash(error, 'danger')
    return render_template('register.html', title='Register', details=details, username=username, email=email, errors=errors)
    #     flash(f'Account created for {form.username.data}!')
    # return render_template('register.html', title='Register', 
    # , form = form
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