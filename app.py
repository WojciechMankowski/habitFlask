from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from login_register import user_page

app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'sceretkey'
db = SQLAlchemy(app)
app.register_blueprint(user_page, url_prefix='/user')


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    nameUser = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    habits = db.relationship("Habit", back_populates="user")


class Habit(db.Model):
    __tablename__ = 'habit'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    frequency = db.Column(db.String(250), nullable=False)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User", back_populates="habits")
    entries = db.relationship("Entry", back_populates="habit")


class Entry(db.Model):
    __tablename__ = 'entry'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(250), nullable=False)
    time = db.Column(db.String(250), nullable=False)
    id_habit = db.Column(db.Integer, db.ForeignKey('habit.id'))
    habit = db.relationship("Habit", back_populates="entries")


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    icon = db.Column(db.String(250), nullable=False)


@app.route('/')
def hello_world():
    users = User.query.all()
    return render_template('index.html', users=users)


if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=True)
