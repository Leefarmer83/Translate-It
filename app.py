import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


"""
Environment variables SECRET and MONGO_URI set in Heroku dashboard
in production
"""


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)
""" alot of the code below was inspired by code institute mini project """
""" allows catagories to show on the home page """


@app.route("/")
@app.route("/home")
def home():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("index.html", categories=categories)


@app.route('/pronunciation')
def pronunciation():
    return render_template("pronunciation.html")


@app.route("/word_cat/<category_id>", methods=["GET", "POST"])
def word_cat(category_id):
    """
    push category and id for category with words in category
    """
    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    words = list(mongo.db.words.find())
    return render_template("word_cat.html",
                           category=category, words=words, categories=category)


@app.route("/get_words")
def get_words():
    """
    Show all words
    """
    words = list(mongo.db.words.find().sort("eng_word", 1))
    return render_template("words.html", words=words)


@app.route("/search", methods=["GET", "POST"])
def search():
    """
    Search section in words.html
    """
    query = request.form.get("query")
    words = list(mongo.db.words.find({"$text": {"$search": query}}))
    return render_template("words.html", words=words)


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Register user, if existing or succesful state. code taken from Mini
    project from code institute
    """
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        # state user exists
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Taken from mini project, log user in
    """
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(existing_user[
                    "password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome to Translate It, {}".format(
                        request.form.get("username")))
                return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """
    user profile page with words created
    """
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    # grab the session user's words
    if session["user"]:
        words = list(mongo.db.words.find())
        return render_template("profile.html", username=username, words=words)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    """
    log user out, code inspired by mini project
    """
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_words", methods=["GET", "POST"])
def add_words():
    """
    add words to words, code inspired by code institute mini project
    """
    # grab sections for words to be added
    if request.method == "POST":
        word = {
            "eng_word": request.form.get("eng_word"),
            "lt_word": request.form.get("lt_word"),
            "helpful_info": request.form.get("helpful_info"),
            "used_in_sentence": request.form.get("used_in_sentence"),
            "category_name": request.form.get("category_name"),
            "created_by": session["user"]
        }
        mongo.db.words.insert_one(word)
        flash("Word Successfully Added")
        return redirect(url_for("get_words"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_words.html", categories=categories)


@app.route("/edit_words/<words_id>", methods=["GET", "POST"])
def edit_words(words_id):
    """
    edit words to words, code inspired by code institute mini project
    """
    # grab words from words collection
    if request.method == "POST":
        word = {
            "eng_word": request.form.get("eng_word"),
            "lt_word": request.form.get("lt_word"),
            "helpful_info": request.form.get("helpful_info"),
            "used_in_sentence": request.form.get("used_in_sentence"),
            "category_name": request.form.get("category_name"),
            "created_by": session["user"]
        }
        mongo.db.words.update({"_id": ObjectId(words_id)}, word)
        flash("Word Successfully Updated")
        return redirect(url_for("get_words"))

    words = mongo.db.words.find_one({"_id": ObjectId(words_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
            "edit_words.html", words=words, categories=categories)


@app.route("/delete_words/<words_id>")
def delete_words(words_id):
    """
    delete words, code inspired by code institute mini project
    """
    mongo.db.words.remove({"_id": ObjectId(words_id)})
    flash("Words Successfully Deleted")
    return redirect(url_for("get_words"))


@app.route("/get_categories")
def get_categories():
    """
    pass category
    """
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("manage_categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    """
    adding category function
    """
    # grab category
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    """
    editing category
    """
    # grab category and ID
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Category Successfully Updated")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    """
    delete category
    """
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("get_categories"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
