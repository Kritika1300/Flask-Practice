from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/sign_form')
def sign_form():
    return render_template("signup.html")

@app.route('/thank_you')
def thank_you():
    first = request.args.get('first')
    last = request.args.get('last')
    return render_template("thankyou.html",first = first, last= last)

@app.errorhandler(404)
def error(e):
    return render_template("404.html"),404

app.run(port=5000,debug=True)