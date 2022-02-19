from ast import Str
import re
from flask import Flask,jsonify,abort, render_template
from flask import make_response, request, url_for


app = Flask(__name__)
#app.url_map.strict_slashes = False

@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('index.html')


@app.route('/calc', methods=["GET","POST"])
def calc():
    n1 = request.form['firstn']
    n2 = request.form['secondn']
    op = request.form['op']
    
    if op == 'soma':
        result = int(n1) + int(n2)
    
    print(n1)
    return str(result)

if __name__ == '__main__':
   app.run(debug=True, host='localhost', port=5000)

