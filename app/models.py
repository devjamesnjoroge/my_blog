from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Quote:

    def __init__(self, author, id, quote, permalink):

        self.author = author
        self.id = id
        self.quote = quote
        self.permalink = permalink

class User(UserMixin, db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    posts = db.relationship('Post', backref = 'user', lazy = 'dynamic')
    pass_secure = db.Column(db.String(255))
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure,password)

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'{self.username}'

class Post(db.Model):

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key = True)
    blog = db.Column(db.String(999999))
    title = db.Column(db.String(255))
    author = db.Column(db.String(255))
    time = db.Column(db.DateTime, default = datetime.now )
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    tags = db.Column(db.String(255))

    def save_post(self):
        db.session.add(self)
        db.session.commit()

    def del_post(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'{Post.id}'


