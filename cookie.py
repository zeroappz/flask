from flask import *

app = Flask(__name__)
app.secret_key = "anything"

@app.route('/')
def dashboard():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/success', methods=['POST','GET'])
def check():
    username = request.form['username']
    # pwd = request.form['pwd']
    # result = request.form

    # if username == 'Praveen' and pwd == 'test':
    session['username'] = request.form['username']
    return render_template('home.html')
    #response = make_response(render_template('home.html'))
    #response.set_cookie('name', username)
    #return response
    # else:
    #     return render_template('crash.html')


@app.route('/profile')
def profile():
    username = request.cookies.get('username')
    response = make_response(render_template('profile.html', username = username))
    return response

@app.route('/viewprofile')
def viewprofile():
    if "username" in session:
        username = session['username']
        return render_template('profile.html', username = username)
    else:
        return 'you have to login first'

@app.route('/logout')
def logout():
    if "username" in session:
        session.pop('username', None)
        return render_template('home.html')
    else:
        return 'you have to login first'
    

if __name__ == '__main__':
    app.run(debug=True)
