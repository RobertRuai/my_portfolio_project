#!/usr/bin/python3
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, InputRequired, Length, EqualTo
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from models.base_model import CrimeRecord
from config import SECRET_KEY
from flask_bcrypt import Bcrypt
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy()
bcrypt = Bcrypt(app)
app.config['SECRET_KEY'] = SECRET_KEY
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql:///{}:{}@{}/{}'.format(MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_DB)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crime_report.db'

# Configure database
db.init_app(app)
# Configure login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@app.before_request
def create_tables():
    db.create_all()


#another example of user class db
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)

#added registration
class RegisterForm(FlaskForm):
    username = StringField(
                           validators=[InputRequired(),
                           Length(min=4, max=20)],
                           render_kw={"placeholder": "Username"})

    password = PasswordField(
                             validators=[InputRequired(),
                             Length(min=8, max=20)],
                             render_kw={"placeholder": "Password"})

    submit = SubmitField('Register')

#added validation
    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
                                                      username=username.data).first()
        if existing_user_username:
            raise ValidationError(
                                  'That username already exists.Please choose a different one.')

class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(),
                           Length(min=4, max=20)],
                           render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[InputRequired(),
                             Length(min=8, max=20)],
                             render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')

@login_manager.user_loader
def load_user(user_id):
    user = User()
    user.id = user_id
    return user

#class CrimeRecordForm(FlaskForm):
    #title = StringField('Title', validators=[DataRequired()])
    #description = TextAreaField('Description', validators=[DataRequired()])

@app.route('/')
@login_required
def home():
    return render_template('./user/home.html')
    #crime_records = CrimeRecord.query.all()
    #return render_template('index.html', crime_records=crime_records)

#@app.route('/add', methods=['GET', 'POST'])
#@login_required
#def add_record():
    #form = CrimeRecordForm()
    #if form.validate_on_submit():
        #new_record = CrimeRecord(title=form.title.data, description=form.description.data)
        #db.session.add(new_record)
        #db.session.commit()
        #return redirect(url_for('home'))
    #return render_template('add_record.html', form=form)

#@app.route('/edit/<int:record_id>', methods=['GET', 'POST'])
#@login_required
#def edit_record(record_id):
    #record = CrimeRecord.query.get(record_id)
    #form = CrimeRecordForm(obj=record)
    #if form.validate_on_submit():
        #record.title = form.title.data
        #record.description = form.description.data
        #db.session.commit()
        #return redirect(url_for('home'))
    #return render_template('edit_record.html', form=form, record_id=record_id)

#@app.route('/delete/<int:record_id>')
#@login_required
#def delete_record(record_id):
    #record = CrimeRecord.query.get(record_id)
    #db.session.delete(record)
    #db.session.commit()
    #return redirect(url_for('home'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('dashboard'))
    return render_template('./user/login.html', form=form)


@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('./user/layout.html')


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@ app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('./user/register.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
