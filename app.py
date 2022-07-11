from datetime import date
from unittest import result
from flask import Flask, render_template, request, redirect, url_for, flash, session
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager, login_user, login_required, logout_user, current_user ,UserMixin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root@localhost/raising"
app.config['SECRET_KEY'] = 'mambacita'


#db initialization
db = SQLAlchemy(app)

#admin route
Admin = Admin(app)


LoginManager = LoginManager()
LoginManager.init_app(app)
LoginManager.login_view = 'login'





class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))


#db.create_all()

class Client(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))
    date_created = db.Column(db.DateTime, default=date.today())
    
#db.create_all()




#routes


@LoginManager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



@app .route('/')
def index():
    return render_template('public/index/index.html')


@app.route('/home')
def home():
    return render_template('public/home/home.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST':
            
        #grab the data from the form
        
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        #save user data to database
        
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        db.session.close()
        
        flash('You have successfully registered! You may now login.', 'success')
        return redirect(url_for('login'))
    else:
        flash('Please fill all the fields', 'danger')
        return render_template('admin/templates/users/templates/register.html', form=form)
        
        
   
    #return render_template('admin/templates/users/templates/register.html', form=form)

@app.route('/process', methods=['POST'])
def process():
        email = request.form['email']
        password = request.form['password']
        #return("email: " + email + " password: " + password)
        email = User.query.filter_by(email=email).first()
        if email == email:
            if email.password == password:
                return redirect(url_for('home'))
            else:
                flash('Password is incorrect', 'danger')
                return redirect(url_for('login'))
            
        



@app.route('/login', methods=['GET', 'POST'])
def login():
    form=LoginForm()
    return render_template('admin/templates/users/templates/login.html', form=form)


@app.route('/logout')
def logout():
    session.clear()
    flash('You were logged out')
    return render_template('public/index/index.html')

#client routes

@app.route('/client')
def client():
    return render_template('admin/templates/customer/templates/customer.html')


@app.route('/client/register', methods=['GET', 'POST'])
def register_client():
    form = RegistrationForm()
    return render_template('admin/templates/customer/templates/Customer_Register.html', form=form)
        

    
@app.route('/client/login', methods=['GET', 'POST'])
def login_client():
    form=LoginForm()
    return render_template('admin/templates/customer/templates/Customer_login.html', form=form)




if __name__ == '__main__':
    app.run(debug=True)
