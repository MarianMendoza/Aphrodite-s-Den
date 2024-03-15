from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField,TextAreaField
from werkzeug.security import generate_password_hash
from wtforms.validators import InputRequired, EqualTo

class LoginForm(FlaskForm):
    user_id = StringField("Username:", validators = [InputRequired()])
    password = PasswordField("Password:", validators=[InputRequired()])
    submit = SubmitField("LOGIN")

class SignUpForm(FlaskForm):
    user_id = StringField("Username:", validators = [InputRequired()])
    password = PasswordField("Password:", validators=[InputRequired()])
    password2 = PasswordField("Verify password:", validators=[InputRequired(), EqualTo("password")])
    ForgotPassword = SubmitField("Forgot Your Password?")
    submit = SubmitField("SIGN UP")

class ReviewsForm(FlaskForm):
    review = TextAreaField("Leave a Review:")
    submit = SubmitField()

class FinaliseCart(FlaskForm):
    firstname = StringField("First Name:", validators=[InputRequired()])
    lastname = StringField("Last Name:", validators=[InputRequired()])
    addressline1 = StringField("Address Line 1:", validators=[InputRequired()])
    addressline2 = StringField("Address Line 2:")
    eircode = StringField("Eir Code:", validators=[InputRequired()])
    submit = SubmitField("Order Now")