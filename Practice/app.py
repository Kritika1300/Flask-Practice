from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>hello!</h1>"

@app.route('/index')
def index():
    my_list = [1,2,3,4,5]
    return render_template("index.html",my_list = my_list)

# @app.route('/about')
# def about():
#     return "<h1>This is the about us page!</h1>"

# @app.route('/some_page/<name>')
# def user(name):
#     l = len(name)
#     if(name[l-1] == 'y'):
#         name = name[0:l-1] + 'utiful'
#     else:
#         name = name + 'y'
#     return 'Hey {} !'.format(name.upper())

app.run(port=5000,debug=True)