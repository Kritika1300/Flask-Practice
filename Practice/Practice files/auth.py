# import os
# os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
# os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'

# from flask import Flask,render_template,redirect,url_for
# from flask_dance.contrib.google import make_google_blueprint,google

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'mysecretkey'

# blueprint = make_google_blueprint(client_id='914861453710-9b5shu4io8h67q4v4saho9f78opj8cdq.apps.googleusercontent.com',
# client_secret= '44sbp6wVCSH1sQWqLrsdPB3u',
# offline=True,scope=['profile','email'])

# app.register_blueprint(blueprint,url_prefix ='/login')

# @app.route('/')
# def index():
#     return render_template('home.html')

# @app.route('/welcome')
# def welcome():
#     #return internal server error if not logged in
#     resp = google.get('/oauth2/v2/userinfo')
#     assert resp.ok
#     email = resp.json()['email']
#     return render_template('welcome.html',email=email)

# @app.route('/login/google')
# def login():
#     if not google.authorized:
#         return render_template(url_for('google.login'))
#     resp = google.get('/oauth2/v2/userinfo')
#     assert resp.ok,resp.text
#     email = resp.json()['email']
#     return render_template('welcome.html',email=email)


# if __name__ == '__main__':
#     app.run(port=5000,debug=True)
