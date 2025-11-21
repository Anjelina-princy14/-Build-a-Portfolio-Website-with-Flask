from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def home():
    projects = [
        {
            "title": "Sales Data Analysis",
            "description": "Analyzed sales data using Python, Pandas, and Matplotlib.",
            "link": "https://github.com/your-username/sales-data-analysis"
        },
        {
            "title": "Flask REST API",
            "description": "Built a REST API with Flask for user management.",
            "link": "https://github.com/your-username/flask-rest-api"
        }
    ]

    return render_template(
        "index.html",
        name="Anjelina Princy A",
        role="Aspiring Data Analyst & Python Developer",
        projects=projects
    )


@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    print("New contact form submission:")
    print("Name:", name)
    print("Email:", email)
    print("Message:", message)

    return redirect(url_for("contact_success"))


@app.route("/contact-success")
def contact_success():
    return render_template("contact_success.html")


if __name__ == "__main__":
    app.run(debug=True)
