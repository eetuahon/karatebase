from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
  
class LoginForm(FlaskForm):
    username = StringField("u")
    password = PasswordField("p")
  
    class Meta:
        csrf = False