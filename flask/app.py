#!/usr/bin/env python3
"""
My first Flask app
"""
# Importera relevanta moduler
from flask import Flask, render_template
from person import Person


jennifer = Person("Jen", "Lee", 33)
jon = Person("John", "Doe", 100)


app = Flask(__name__)

@app.route("/")
def main():
    """ Main route """
    return render_template("index.html")

@app.route("/about")
def about():
    """ About route """
    img = jennifer.get_img_path_jpg()
    return render_template("about.html", name=jennifer.name, \
        sir=jennifer.sir, img=img)

@app.route("/redovisning")
def report():
    """ Report route """
    return render_template("report.html", name=jennifer.name, \
    sir=jennifer.sir, age=jennifer.age)

@app.route("/jd")
def aboutjon():
    """ About jon """
    return render_template("jd.html", name=jon.name, sir=jon.sir, age=jon.age)

@app.errorhandler(404)
def page_not_found(e):
    """
    Handler for page not found 404
    """
    #pylint: disable=unused-argument
    return "Flask 404 here, but not the page you requested."

@app.errorhandler(500)
def internal_server_error(e):
    """
    Handler for internal server error 500
    """
    #pylint: disable=unused-argument
    import traceback
    return "<p>Flask 500<pre>" + traceback.format_exc()

if __name__ == "__main__":
    app.run(debug=True) #används endast i utvecklingsläge!
