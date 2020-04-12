from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("u", [validators.Length(min=3, max=15)])
    password = PasswordField("p", [validators.Length(min=3, max=30)])
  
    class Meta:
        csrf = False