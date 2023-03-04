from flask import Blueprint, render_template, redirect, url_for

views = Blueprint(__name__, "views")


@views.route("/")
def home_page():
    return render_template("index.html", name="Aaron")


# this is how to redirect
@views.route("go-home")
def go_home():
    return redirect(url_for("views.home"))
