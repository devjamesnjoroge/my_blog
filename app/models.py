from . import db

class Quote:

    def __init__(self, author, id, quote, permalink):

        self.author = author
        self.id = id
        self.quote = quote
        self.permalink = permalink

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))

    def __repr__(self):
        return f'{self.username}'

