from flask import Flask,render_template,redirect,url_for,flash
from flask_wtf import FlaskForm
from wtforms import (StringField,SubmitField)

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secretkey'

class InfoForm(FlaskForm):
    submit = SubmitField('Submit on click')


@app.route('/',methods = ['GET','POST'])
def index():

    form = InfoForm()
    if form.validate_on_submit():
        flash('You just clicked the Submit button !')
        flash('Also heyyy this is the use of flash!')
        return redirect(url_for('index'))
    
    return render_template('index.html',form = form)

if __name__ == "__main__":
    app.run(port = 5000,debug = True)
