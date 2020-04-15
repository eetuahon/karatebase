from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("u", [validators.Length(min=5, max=15)])
    password = PasswordField("p", [validators.Length(min=5, max=45)])
  
    class Meta:
        csrf = False

class ChangeForm(FlaskForm):
    old = PasswordField("Current pw", [validators.Length(min=5, max=30)])
    new1 = PasswordField("New pw", [validators.Length(min=8, max=64)])
    new2 = PasswordField("Retype new pw", [validators.Length(min=8, max=64)])

    class Meta:
        csrf = False