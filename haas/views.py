"""Views."""
from flask import jsonify
from flask import render_template
from flask import request

from haas import app
from haas.generator import generate_hex


@app.get("/")
def home():
    """Show home page."""
    return render_template("index.html", title="Home")


@app.get("/api")
def api():
    """Return a random 6 hexagram reading as a JSON object."""
    return jsonify(generate_hex(6))


@app.route("/analytics", methods=["GET", "POST"])
def analytics():
    """Render a hexagram reading with the submitted number of hexagrams."""
    ga_version = request.args.get("type", default="ga4")
    container_id = {
        "ua": "GTM-5S9XWS6",
        "ga4": "GTM-NBCMVLT",
    }[ga_version]

    if request.method == "POST":
        input = request.form["hex_count"] or "6"
        num = int(input)
    else:
        num = 6

    return render_template(
        "reading.html",
        container_id=container_id,
        title="Hexagrams",
        hexagrams=generate_hex(num),
    )


@app.get("/cookies")
def cookies():
    """Render the cookies page."""
    return render_template("cookies.html")
