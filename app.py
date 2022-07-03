from flask import Flask, render_template, request, redirect, url_for, flash


app = Flask(__name__)


@app .route('/')
def index():
    return render_template('public/index/index.html')

@app.route('/home')
def home():
    return render_template('public/home/home.html')




@app.route('/admin')
def admin():
    return render_template('admin/admin.html')





if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='
    
    