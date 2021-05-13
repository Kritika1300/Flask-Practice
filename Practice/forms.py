from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField

class AddForm(FlaskForm):
    name = StringField('Name of the puppy :')
    submit = SubmitField('Submit')

class DelForm(FlaskForm):
    id = IntegerField('Id of the puppy you want to remove :')
    submit = SubmitField('Submit')

class AddOwnerForm(FlaskForm):
    name = StringField('Name of the Owner :')
    pup_id = IntegerField('Id of the Puppy :')
    submit = SubmitField('Add Owner')

