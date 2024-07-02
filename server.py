from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/services")
def services():

    message_variable = "These are our services."

    services_list = [
        {
            "name": "Website Development",
            "Description": "We provide excellenet website development",
        },
        {
            "name": "Logo Creation",
            "Description": "We provide excellenet  Logo Creation.",
        },
    ]

    is_available = False

    return render_template(
        "services.html",
        message_template=message_variable,
        services_list=services_list,
        is_available=is_available,
    )


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
