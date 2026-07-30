import os
from datetime import datetime, date
from flask import Flask, render_template, redirect, url_for, request, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "secretkey")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DATABASE_URL", "sqlite:///todo.db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    todos = db.relationship("Todo", backref="user", lazy=True)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255), nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    @property
    def overdue(self):
        return self.due_date < datetime.utcnow().date()


with app.app_context():
    db.create_all()

week_days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def get_today_label():
    now = datetime.utcnow()
    week_day = week_days[now.weekday()]
    month_name = months[now.month - 1]
    return f"{now.day} {month_name} {now.year}, {week_day}"


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"]

        if not username or not password:
            return render_template(
                "signup.html", error="Username and password are required."
            )

        existing = User.query.filter_by(username=username).first()
        if existing:
            return render_template(
                "signup.html", error="Username already exists."
            )

        user = User(
            username=username, password=generate_password_hash(password)
        )
        db.session.add(user)
        db.session.commit()

        return redirect(url_for("login"))

    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"]

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session["user"] = user.username
            return redirect(url_for("home"))

        return render_template(
            "login.html", error="Invalid username or password."
        )

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.route("/", methods=["GET", "POST"])
def home():
    if "user" not in session:
        return redirect(url_for("login"))

    user = User.query.filter_by(username=session["user"]).first()
    if not user:
        session.clear()
        return redirect(url_for("login"))

    if request.method == "POST":
        new_item_content = request.form["newItem"].strip()
        new_item_duedate = request.form["duedate"]

        if new_item_content and new_item_duedate:
            year_value, month_value, day_value = map(
                int, new_item_duedate.split("-")
            )
            todo = Todo(
                content=new_item_content,
                due_date=date(year_value, month_value, day_value),
                user_id=user.id,
            )
            db.session.add(todo)
            db.session.commit()

        return redirect(url_for("home"))

    list_items = (
        Todo.query.filter_by(user_id=user.id).order_by(Todo.due_date).all()
    )
    return render_template(
        "index.html",
        list_items=list_items,
        today=get_today_label(),
        leng=len(list_items),
    )


@app.route("/delete-item", methods=["POST"])
def delete_item():
    if "user" not in session:
        return redirect(url_for("login"))

    todo_id = request.form.get("checkbox")
    if todo_id:
        todo = Todo.query.filter_by(id=int(todo_id)).first()
        if (
            todo
            and todo.user_id
            == User.query.filter_by(username=session["user"]).first().id
        ):
            db.session.delete(todo)
            db.session.commit()

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=(os.getenv("FLASK_ENV") == "development"))
