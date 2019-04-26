from flask import Flask, render_template, request, make_response
app = Flask(__name__)

@app.route('/cookie')
def index():
   return render_template('cookie_index.html')

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']

        #get response object from return value of a view function
        resp = make_response(render_template('readcookie.html',cook =user))
        #sets a Cookie name userID and form value.
        resp.set_cookie('userID', user)

        return resp

@app.route('/getcookie')
def getcookie():
   #reads back and displays the cookie value in browser
   name = request.cookies.get('userID')
   return '<h1>welcome '+name+'</h1>'

if __name__ == '__main__':
    app.run(debug=True)