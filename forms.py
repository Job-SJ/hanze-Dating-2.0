from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo

class LoginForm(FlaskForm):
    email = EmailField('Email')
    password = PasswordField('Wachtwoord')
    submit = SubmitField('Inloggen', render_kw={"class":"btn btn-primary"})

class RegistratieForm(FlaskForm):
    email = EmailField('Email')
    password = PasswordField('Wachtwoord')
    confirm_password = PasswordField('Herhaal wachtwoord', validators=[EqualTo('password', message='Wachtwoorden moeten overeenkomen!')])
    submit = SubmitField('Registreren', render_kw={"class":"btn btn-success"})



