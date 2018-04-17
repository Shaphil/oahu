from flask import render_template, request

from oahu import app, db
from oahu.models import Comment


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['username']
        comment_text = request.form['comment_text']
        comment = Comment(username=name, comment_text=comment_text)
        db.session.add(comment)
        db.session.commit()
    comments = Comment.query.all()
    return render_template('index.html', comments=comments)
