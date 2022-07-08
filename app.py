from flask import Flask, render_template, request, redirect, url_for, flash, session
from .forms import RegistrationForm, LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mambacita'


@app .route('/')
def index():
    return render_template('public/index/index.html')


@app.route('/home')
def home():
    return render_template('public/home/home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'edwin@lorisystems.com' and form.password.data == '123456':
            flash(f'{form.email.data} You have been logged successfully', category='success')
            return redirect(url_for('home'))
        else:
           flash(f'{form.email.data} login unsuccessful!', category='danger')
    return render_template('admin/templates/users/templates/login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'{form.username.data} You have been registered!', category='success')
        return redirect(url_for('login'))
    return render_template('admin/templates/users/templates/register.html', form=form)
