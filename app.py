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

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/index")
def index():
    """
    This is the index page,
    welcoming you to lilly's
    kitchen.
    """
    return render_template("index.html")


@app.route("/recipes")
def get_recipes():
    """
    Recipes page where anyone
    visiting the site can see
    recipes created by other users
    """
    recipes = list(mongo.db.recipes.find())
    return render_template("get_recipes.html", recipes=recipes)


@app.route("/search", methods=["GET", "POST"])
def search():
    """
    Allows you to search the db
    and will display recipes found in
    db
    """
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("get_recipes.html", recipes=recipes)


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Allows users to create new
    account. It will check db to see
    if user exists before registering
    user. If no account is found new
    user will be created on db
    """
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

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
    Log's in user after checking
    username and password. If username,
    password doesn't exist or incorrect
    will ask user to try log in again
    """
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(
                    url_for("profile", username=session["user"]))
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
    Display users profile and will let user
    know they have been logged into lilly's
    kitchen
    """
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    """
    Log's user out of session
    """
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    """
    Allows registered users to create
    and upload there own recipe to db
    and website if logged in
    """
    if request.method == "POST":
        recipes = {
            "recipe_name": request.form.get("recipe_name"),
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "serves": request.form.get("serves"),
            "ingredients": request.form.get("ingredients"),
            "recipe_description": request.form.get("recipe_description"),
            "image": request.form.get("image"),
            "method_1": request.form.get("method_1"),
            "method_2": request.form.get("method_2"),
            "method_3": request.form.get("method_3"),
            "method_4": request.form.get("method_4"),
            "method_5": request.form.get("method_5"),
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipes)
        flash("Recipe successfully added")
        return redirect(url_for("get_recipes"))

    return render_template("add_recipe.html")


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    """
    Allows registered users to edit
    recipes they've created themselves
    """
    if request.method == "POST":
        submit = {
            "recipe_name": request.form.get("recipe_name"),
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "serves": request.form.get("serves"),
            "ingredients": request.form.get("ingredients"),
            "recipe_description": request.form.get("recipe_description"),
            "image": request.form.get("image"),
            "method_1": request.form.get("method_1"),
            "method_2": request.form.get("method_2"),
            "method_3": request.form.get("method_3"),
            "method_4": request.form.get("method_4"),
            "method_5": request.form.get("method_5"),
            "created_by": session["user"]
        }
        mongo.db.recipes.replace_one({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe Successfully Updated")
        return redirect(url_for("get_recipes"))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("edit_recipe.html", recipe=recipe)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    """
    Allows registered users to delete
    recipes they've created themselves
    """
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("get_recipes"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
