from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""

    # return "<html><body>This is the homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    return render_template("index.html")


@app.route("/application-form")
def application_form():
    """Application form with input fields, has post method to send results to next page"""

    return render_template("application-form.html")


@app.route("/application", methods=["POST"])
def application():
    """Gets the results of the application form and displays the output"""

    first_name = request.form["first-name"]
    last_name = request.form["last-name"]
    salary = int(request.form["salary"])
    position = request.form["position"]

    return render_template("application-response.html", first_name=first_name, last_name=last_name, salary=salary, position=position)




if __name__ == "__main__":
    app.run(debug=True)
