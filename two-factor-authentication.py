from flask_login import LoginManager, login_user, logout_user, login_required, current_user
import os

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, role='user')
        user.set_password(form.password.data)
        user.otp_secret = pyotp.random_base32()
        db.session.add(user)
        db.session.commit()
        # Next: Implement 2FA setup or email verification here
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('two_factor'))
    return render_template('login.html', form=form)

@app.route('/two_factor', methods=['GET', 'POST'])
@login_required
def two_factor():
    form = TwoFactorForm()
    if form.validate_on_submit():
        user = current_user
        totp = pyotp.TOTP(user.otp_secret)
        if totp.verify(form.token.data):
            return redirect(url_for('index'))
        else:
            flash('Invalid 2FA token')
    return render_template('two_factor.html', form=form)

@app.route('/')
@login_required
def index():
    return 'Logged in as: ' + current_user.username
