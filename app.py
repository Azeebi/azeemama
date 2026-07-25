"""Flask application serving Oyeleke Azeezat Bisola's portfolio."""

import os
from datetime import datetime

from flask import Flask, render_template, request, redirect, url_for, flash

from data import get_context

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "change-this-secret-key-in-production")


@app.context_processor
def inject_globals():
    """Make the current year available to every template."""
    return {"current_year": datetime.now().year}


@app.route("/")
def index():
    return render_template("index.html", **get_context())


@app.route("/cv")
def cv():
    return render_template("cv.html", **get_context())


@app.route("/contact", methods=["POST"])
def contact():
    """Handle the contact form submission."""
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not email or not message:
        flash("Please fill in all fields.", "error")
    else:
        # In production, send an email or persist the message here.
        app.logger.info("Contact message from %s <%s>: %s", name, email, message)
        flash("Thank you! Your message has been received.", "success")

    return redirect(url_for("index") + "#contact")


if __name__ == "__main__":
    # Render (and most hosts) provide the port via the PORT env var and require
    # binding to 0.0.0.0 so the service is reachable. Locally it defaults to 5000.
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_DEBUG", "0") == "1"
    app.run(host="0.0.0.0", port=port, debug=debug)
