from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, DateField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length

class ContactForm(FlaskForm):
    fname = StringField('Your First Name', validators=[DataRequired()])
    lname = StringField('Your Last Name', validators=[DataRequired()])
    email = StringField('Your Email', validators=[DataRequired(), Email()])
    greeting = TextAreaField('Message', validators=[DataRequired(), Length(min=1, max=1500)])
    submit = SubmitField('Send Message')

        