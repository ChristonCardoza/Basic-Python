from flask import Flask, render_template
app = Flask(__name__)

#It sends the user value to hello.html's variable i.e. value is replace {{ name }} here.
@app.route('/hello/<user>')
def hello_name(user):
   return render_template('hello.html', name = user)

@app.route('/hello/<int:score>')
def hello_score(score):
   return render_template('hello.html', marks = score)

@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('result.html', result = dict)

#static files like css and javascript should save under static folder
@app.route("/static")
def index():
   return render_template("index.html")

if __name__ == '__main__':
   app.run(debug = True)