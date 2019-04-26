from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/hello') #http://127.0.0.1:5000/hello
def hello_world():
   return 'Hello World'

#url binds with String
@app.route('/hello/<name>')#http://127.0.0.1:5000/hello/Christon
def hello_name(name):
   return 'Hello %s!' % name

#url binds with Integer
@app.route('/blog/<int:postID>')#http://127.0.0.1:5000/blog/11
def show_blog(postID):
   return 'Blog Number %d' % postID

#url binds with Float
@app.route('/rev/<float:revNo>')#http://127.0.0.1:5000/rev/1.1
def revision(revNo):
   return 'Revision Number %f' % revNo

#Function useful for dynamically building a URL for a specific function ,accepts the name of a function as first argument, and one or more keyword arguments, each corresponding to the variable part of URL.
@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_world'))
   else:
      return redirect(url_for('hello_name',name = name))

if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug = True)   