from services.database import db

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    description = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        return '<Author %r>' % self.name