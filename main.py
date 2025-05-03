from flask import Flask, request, render_template, redirect, url_for
from context.parse_jd import extract_keywords
from agents.candidate_scraper import search_candidates
from outputs.result_handler import format_output
from db.store import save_candidates, collection

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        jd = request.form.get("job_description")
        if not jd:
            return render_template("index.html", error="Please enter a job description.")

        criteria = extract_keywords(jd)
        candidates = search_candidates(criteria)

        if candidates:  # Only save if results are found
            save_candidates(candidates, criteria)
            return render_template("results.html", candidates=candidates)
        else:
            return render_template("index.html", error="No candidates found. Try a different JD.")

    return render_template("index.html")

@app.route("/view-all")
def view_all():
    docs = list(collection.find({"candidates": {"$ne": []}}, {"_id": 0}))  # Exclude entries with no candidates
    return render_template("history.html", results=docs)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
