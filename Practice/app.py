from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>hello!</h1>"

@app.route('/about')
def about():
    return "<h1>This is the about us page!</h1>"

@app.route('/some_page/<name>')
def user(name):
    return 'Hey {} !'.format(name)

app.run(port=5000,debug=True)