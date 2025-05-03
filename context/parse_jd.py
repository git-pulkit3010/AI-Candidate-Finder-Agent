from transformers import pipeline

# Load summarization pipeline
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def extract_keywords(job_description: str) -> dict:
    # Use summarizer to condense JD into a search-friendly form
    summary = summarizer(job_description, max_length=60, min_length=30, do_sample=False)[0]['summary_text']

    # Basic keyword heuristics — refine later with real LLMs
    keywords = {
        "role": "Python Developer" if "python" in job_description.lower() else "Developer",
        "skills": [],
        "location": "India" if "india" in job_description.lower() else "Remote",
        "experience": "3+ years" if "3+" in job_description.lower() else "unspecified"
    }

    if "django" in job_description.lower(): keywords["skills"].append("Django")
    if "flask" in job_description.lower(): keywords["skills"].append("Flask")
    if "postgresql" in job_description.lower(): keywords["skills"].append("PostgreSQL")

    return keywords
