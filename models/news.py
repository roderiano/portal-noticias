from services.database import db
from sqlalchemy.orm import backref

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(150), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id', ondelete='CASCADE'), nullable=False)
    author = db.relationship('Author', backref=backref('news'))

    def __repr__(self):
        return '<News %r>' % self.name