"""
has view function to route to welcome pages
"""
from flask import render_template


def welcome_routes(app):
    """
    has view functions
    """
    @app.route("/")
    @app.route("/home")
    def index() -> str:
        return render_template("index.html")

    @app.route("/about")
    def about() -> str:
        return render_template("about.html")

    @app.route("/contact")
    def contact() -> str:
        return render_template("contact.html")

    @app.route("/menu")
    def menu() -> str:
        return render_template("menu.html")
