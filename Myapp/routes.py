# Myapp/routes.py
from flask import render_template, redirect, url_for,request,session
from Myapp import app 
from . import utils

@app.route("/")
def index():
    """Home page route."""
    return render_template("index.html", title="Home")

@app.route("/register", methods=['GET', 'POST'])
def register():
    """Registration page route."""
    if request.method=='POST':
        username=request.form.get('username')
        email=request.form.get('email')
        password=request.form.get('password')
        confirmpassword=request.form.get('confirmpassword')
        users=utils.get_users()
        if users:
            if username in users:
                utils.flash_overwrite('UserName alrady exists!', 'error')
                return render_template('register.html', title='Register')
            for userdetails in users.values():
                if userdetails['email']==email:
                    utils.flash_overwrite('Email alrady exists!', 'error')
                    return render_template('register.html', title='Register')
            if password != confirmpassword:
                utils.flash_overwrite('Password Missmatch!', 'error')
                return render_template('register.html', title='Register')
        user={
            username:{
                "email":email,
                "password":password
            }
        }
        utils.put_user(user)
        utils.flash_overwrite('Congratulations, you are now a registered user!', 'success')
        return render_template('login.html',title='Login')
    
    return render_template('register.html', title='Register')

@app.route('/login',methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        username=request.form.get('username')
        password=request.form.get('password')
        users=utils.get_users()
        if users:
            if username not in users:
                utils.flash_overwrite('UserName or password missmatch!', 'error')
                return render_template('login.html',title='Login')
            else:
                if users[username]['password']!=password:
                    utils.flash_overwrite('UserName or password missmatch!', 'error')
                    return render_template('login.html',title='Login')
        session["user"]=username
        utils.flash_overwrite('Successfully Logedin', 'success')
        return render_template('home.html',title='Home')
    return render_template('login.html',title='Login')
