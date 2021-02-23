from flask import *
from flaskext.mysql import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'class'

mysql = MySQL(app)

@app.route('/', methods=['POST'])
def check():
    username = request.form['username']
    pwd = request.form['pwd']

    #result = request.form
    # username = request.args.get('username')
    # pwd = request.args.get('pwd')

    if username == 'Abinavv' and pwd == 'blackieaka007':
        return render_template('dashboard.html', n=10)
    else:
        return 'Check Username and Password'


if __name__ == '__main__':
    app.run(debug=True)