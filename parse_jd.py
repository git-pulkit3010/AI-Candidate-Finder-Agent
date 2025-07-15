from transformers import pipeline

# Load a question-answering pipeline for keyword extraction
qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

def extract_keywords(job_description: str) -> dict:
    # Function to ask a question and get an answer from the JD
    def ask_question(question):
        result = qa_pipeline(question=question, context=job_description)
        return result['answer']

    role = ask_question("What is the job role?")
    skills_raw = ask_question("What are the required skills?")
    location = ask_question("What is the job location?")
    experience = ask_question("What is the required experience?")

    # Simple split for skills, can be refined with more advanced NLP if needed
    skills = [s.strip() for s in skills_raw.split(',') if s.strip()]

    return {
        "role": role,
        "skills": skills,
        "location": location,
        "experience": experience
    }
