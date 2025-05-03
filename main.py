from flask import Flask, request, jsonify
from context.parse_jd import extract_keywords
from agents.candidate_scraper import search_candidates
from outputs.result_handler import format_output

app = Flask(__name__)

@app.route('/run-agent', methods=['POST'])
def run_agent():
    data = request.json
    job_description = data.get("job_description")

    if not job_description:
        return jsonify({"error": "Job description is required"}), 400

    criteria = extract_keywords(job_description)
    candidates = search_candidates(criteria)
    response = format_output(candidates)

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
