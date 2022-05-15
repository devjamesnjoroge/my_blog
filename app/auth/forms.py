from ..models import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, BooleanField, SubmitField
from wtforms.validators import email, DataRequired, EqualTo, ValidationError, Length

class RegistrationForm(FlaskForm):
    email = EmailField('Enter your email : ', validators=[DataRequired(), email()])
    username = StringField('Enter Username : ', validators=[DataRequired(), Length(min=3, max=20)])
    password = PasswordField('Enter Password : ', validators=[DataRequired()])
    confirm_password = PasswordField('confirm Password :', validators=[DataRequired(), EqualTo(password , message='Passwords must match')])
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
        if User.query.filter_by(email =data_field.data).first():
            raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')

class LoginForm(FlaskForm):

    email = EmailField('Enter your email : ', validators=[DataRequired(), email()])
    password = PasswordField('Enter Password : ', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')
    
    
