from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return '<h1>Hello World! Home Page</h1>'

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form method="post" action="/signin">
   username: <input type="text" name="username"><br>
   password: <input type="password" name="password"><br>
   <p>   <input type="submit" value="Sign In">
    </form>
    
    
    '''
@app.route('/signin', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    return f'<h1>Welcome {username}!</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)


