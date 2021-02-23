from flask import *

app = Flask(__name__)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/login', methods=['POST'])
def check():
    username = request.form['username']
    pwd = request.form['pwd']

    result = request.form
    # username = request.args.get('username')
    # pwd = request.args.get('pwd')

    if username == 'Abinavv' and pwd == 'blackieaka007':
        #return redirect(url_for('dashboard'))
        return render_template('dashboard.html', n=10)
    else:
        return 'Check Username and Password'


if __name__ == '__main__':
    app.run(debug=True)