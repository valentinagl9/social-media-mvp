import sqlite3

from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from werkzeug.security import check_password_hash, generate_password_hash

from app.db import get_db

main = Blueprint("main", __name__)


@main.route("/")
def index():
    if session.get("user_id"):
        return redirect(url_for("main.home"))
    return redirect(url_for("main.login"))


@main.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        if not username or not password:
            flash("Username and password are required.", "error")
            return render_template("register.html"), 400

        if len(username) > 50:
            flash("Username must be 50 characters or fewer.", "error")
            return render_template("register.html"), 400

        if len(password) < 8:
            flash("Password must be at least 8 characters.", "error")
            return render_template("register.html"), 400

        db = get_db()

        try:
            db.execute(
                "INSERT INTO users (username, password_hash) VALUES (?, ?)",
                (username, generate_password_hash(password)),
            )
            db.commit()
        except sqlite3.IntegrityError:
            flash("That username is already taken.", "error")
            return render_template("register.html"), 409

        flash("Account created successfully. You can now log in.", "success")
        return redirect(url_for("main.login"))

    return render_template("register.html")


@main.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        user = get_db().execute(
            "SELECT id, username, password_hash FROM users WHERE username = ?",
            (username,),
        ).fetchone()

        if user is None or not check_password_hash(user["password_hash"], password):
            flash("Invalid username or password.", "error")
            return render_template("login.html"), 401

        session.clear()
        session["user_id"] = user["id"]
        session["username"] = user["username"]
        return redirect(url_for("main.home"))

    return render_template("login.html")


@main.route("/home")
def home():
    if not session.get("user_id"):
        flash("Please log in to continue.", "error")
        return redirect(url_for("main.login"))

    db = get_db()
    posts = db.execute(
        """
        SELECT posts.content, posts.created_at, users.username
        FROM posts
        JOIN users ON posts.user_id = users.id
        ORDER BY posts.id DESC
        """
    ).fetchall()

    return render_template(
        "home.html",
        username=session["username"],
        posts=posts,
    )
    

@main.route("/feed")
def feed():
    posts = get_db().execute(
        """
        SELECT posts.content, posts.created_at, users.username
        FROM posts
        JOIN users ON posts.user_id = users.id
        ORDER BY posts.id DESC
        """
    ).fetchall()

    return render_template("feed.html", posts=posts)


@main.route("/logout", methods=["POST"])
def logout():
    session.clear()
    flash("You have been logged out.", "success")
    return redirect(url_for("main.login"))
    

@main.route("/posts/create", methods=["POST"])
def create_post():
    from flask import flash, redirect, request, session, url_for
    from app.db import get_db

    if "user_id" not in session:
        return redirect(url_for("main.login"))

    content = request.form.get("content", "").strip()

    if not content:
        flash("Post content cannot be empty.")
        return redirect(url_for("main.home"))

    db = get_db()
    db.execute(
        "INSERT INTO posts (user_id, content) VALUES (?, ?)",
        (session["user_id"], content),
    )
    db.commit()

    flash("Post created successfully.")
    return redirect(url_for("main.home"))

