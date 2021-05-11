from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>hello!</h1>"

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/contact/<user>')
def contact(user):
    return render_template("contact.html", user = user)


app.run(port=5000,debug=True)