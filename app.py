from flask import Flask, render_template, request, redirect, url_for, flash


app = Flask(__name__)


@app .route('/')
def index():
    return render_template('public/index/index.html')

@app.route('/home')
def home():
    return render_template('public/home/home.html')



@app.route('/login')
def login():
    return render_template('admin/templates/users/templates/login.html')


@app.route('/register')
def register():
    return render_template('admin/templates/users/templates/register.html')