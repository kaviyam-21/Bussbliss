from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    role = SelectField('Role', choices=[('crew', 'Crew Member'), ('passenger', 'Passenger')])
    region = SelectField('Region', choices=[('north', 'North'), ('south', 'South')])
    submit = SubmitField('Login')
