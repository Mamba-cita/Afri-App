from unittest import result
from flask import Flask, render_template, request, redirect, url_for, flash, session
from forms import RegistrationForm, LoginForm
from flask_mysqldb import MySQL


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mambacita'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///afri.db'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'afri'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


mysql = MySQL(app)


# db = SQLAlchemy(app)


@app .route('/')
def index():
    return render_template('public/index/index.html')


@app.route('/home')
def home():
    return render_template('public/home/home.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO user_reg(username, email, password) VALUES(%s, %s, %s)", (username, email, password))
        mysql.connection.commit()
        cur.close()
        flash(f'{form.username.data} You have been registered!', category='success')
        return redirect(url_for('login'))
    return render_template('admin/templates/users/templates/register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'{form.email.data} You have been logged successfully', category='success')
        return redirect(url_for('home'))
    else:
        flash(f'{form.email.data} login unsuccessful!', category='danger')
    return render_template('admin/templates/users/templates/login.html', form=form)


@app.route('/logout')
def logout():
    return render_template('public/index/index.html')


@app.route('/db')
def db():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM users''')
    results = cur.fetchall()
    print(results)
    return "Hello World!"
