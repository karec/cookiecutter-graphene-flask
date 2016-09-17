from {{cookiecutter.app_name}}.extensions import db
from {{cookiecutter.app_name}}.models import User


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship(User, backref=db.backref('articles', uselist=True))

    def __repr__(self):
        return '<Article %s>' % self.title
