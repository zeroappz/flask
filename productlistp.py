from flask import *

app = Flask(__name__)

@app.route('/list',methods=['POST'])
def list():
    return render_template('product_list1.html')




if __name__ == '__main__':
    app.run(debug=True)