from flask import Blueprint, render_template, redirect, url_for

views = Blueprint(__name__, "views")


@views.route("/")
def home_page():
    return render_template(
        "index.html"
    )


@views.route("/about")
def about_page():
    return render_template("about.html")


@views.route("/projects")
def projects_page():
    return render_template("projects.html")


@views.route("/work")
def work_page():
    return render_template("work.html")


@views.route("/test")
def test_page():
    return render_template("test.html")
