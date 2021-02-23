from flask import Flask, redirect, url_for
from flask.templating import render_template

app = Flask(__name__)

# Decorator
@app.route('/')
def home():
    return 'Welcome, buddy!'


@app.route('/products/<name>')
def products(name):
    return 'list of products will be shown here' + 'this product is: ' + name


@app.route('/about/<int:pagenum>')
def about(pagenum):
    return 'About page number is ' + str(pagenum)


@app.route('/contact')
def contact():
    return 'contact, buddy!'

0
@app.route('/pagenotfound')
def pagenotfound():
    return 'The page you are looking for is not found, buddy!'


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/samsung')
def samsung():
    return 'Samsung phones available here!'


@app.route('/apple')
def apple():
    return 'Apple phones available here!'


@app.route('/productname/<name>')
def productname(name):
    if name == 'samsung':
        return redirect(url_for('samsung'))
    if name == 'apple':
        return redirect(url_for('apple'))
    else:
        return redirect(url_for('pagenotfound'))
        

if __name__ == "__main__":
    app.run(debug = True)