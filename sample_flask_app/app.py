from urllib import request
from flask import Flask, render_template, url_for
from flask import Flask, flash, redirect, render_template, request, session

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import requests

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(200),nullable =False)
    date_created = db.Column(db.DateTime,default = datetime.utcnow)

    def __repr__(self):
        return "<Task %r>" % self.id


@app.route("/", methods=["POST","GET"]) # what is a route
def index():
    if request.method == "POST":
        task_content = request.form["content"]
        new_task = Todo(content =task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect("/")
        except:
            return "There was an error"

    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template("index.html", tasks = tasks)
    #return "hello world"

@app.route("/delete/<int:id>")
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect("/")
    except:
        return "There was an error in deleting"


@app.route("/update/<int:id>", methods = ["POST","GET"])
def update(id):
    if request.method == "POST":
        pass 
    else:
        render_template("update.html")

if __name__ == "__main__":
    app.run(debug = True)

