from flask import Blueprint, render_template

views = Blueprint(__name__, "views")


@views.route("/")
def home_page():
    return render_template(
        "index.html", name="Aaron Barratt", tag_line="Full Stack Developer"
    )
