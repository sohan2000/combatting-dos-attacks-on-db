from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo
import pyotp
import uuid


app = Flask(__name__)
app.config['SECRET_KEY'] = uuid.uuid4().hex # Generates random secret key. Something like '3d6f45a5fc12445dbac2f59c3b6c7cb1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)

# User model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(10), nullable=False)
    otp_secret = db.Column(db.String(16))  # for 2FA

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_totp_uri(self):
        return pyotp.totp.TOTP(self.otp_secret).provisioning_uri(self.username, issuer_name="app")

# Registration form
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[
        DataRequired(), Length(min=8), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField('Register')

# Login form
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

# 2FA form
class TwoFactorForm(FlaskForm):
    token = StringField('Token', validators=[DataRequired(), Length(6, 6)])
    submit = SubmitField('Verify')
