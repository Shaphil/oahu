from datetime import datetime

from oahu import db


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False)
    comment_text = db.Column(db.String(8192), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'{self.username}: {self.comment_text}'
