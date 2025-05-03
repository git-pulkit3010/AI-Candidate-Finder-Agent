import os
from dotenv import load_dotenv
import requests

load_dotenv()

def search_candidates(criteria: dict) -> list:
    query = f"{criteria['role']} {' '.join(criteria['skills'])} site:linkedin.com/in"
    api_key = os.getenv("SERPAPI_KEY")
    url = "https://serpapi.com/search"

    params = {
        "engine": "google",
        "q": query,
        "api_key": api_key,
        "num": "5"
    }

    response = requests.get(url, params=params)
    data = response.json()

    results = data.get("organic_results", [])
    candidates = []

    for result in results:
        candidates.append({
            "name": result.get("title", "Unknown"),
            "profile_url": result.get("link", ""),
            "title": criteria["role"],
            "skills": criteria["skills"],
            "location": criteria.get("location", "Unspecified")
        })

    return candidates
