🧠 AI Candidate Finder Agent

A complete AI-powered agent that parses job descriptions, scrapes candidate data, and provides an elegant web interface for recruiters.

Please make an .env file with your API key from https://serpapi.com/. Also within the .env file, add MONGO_URI=mongodb://localhost:27017 (since using mongodb locally on a Docker container)

✨ Features

🔍 Parse job descriptions using LLMs
🌐 Scrape web profiles matching the JD
💾 Store results in MongoDB
🖥️ View results in a beautiful dark-mode Flask UI
🧠 Easily switch LLMs (OpenAI, HuggingFace, or local)


🛠 Tech Stack

Python 3.10
Flask
MongoDB (via Docker)
Jinja2 (HTML templates)
OpenAI or HuggingFace APIs (LLM)

1. Start MongoDB
docker run -d --name mongodb \
  -p 27017:27017 \
  -v ~/mongo-data:/data/db \
  mongo:5

2. Virtual Env Activation and Installation
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

3. Run Flask App
python main.py


📂 Project Structure

ai_agent_mcp/
├── agents/                # Candidate scraping logic
├── context/               # JD parsing / keyword extraction
├── db/
│   └── store.py           # MongoDB connection
├── outputs/               # Output formatting logic
├── templates/             # HTML UI
├── main.py                # Flask app entry point
├── Dockerfile             # Container config
├── docker-compose.yml     # App + Mongo
└── requirements.txt
