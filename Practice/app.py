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
    l = len(name)
    if(name[l-1] == 'y'):
        name = name[0:l-1] + 'utiful'
    else:
        name = name + 'y'
    return 'Hey {} !'.format(name.upper())

app.run(port=5000,debug=True)