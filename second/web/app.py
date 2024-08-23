from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')
    
    

@app.route('/signin', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    return render_template('result.html',username=username,password=password)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)


