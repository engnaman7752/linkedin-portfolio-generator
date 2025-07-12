
from flask import Flask, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_mock_linkedin_data(username):
    return {
        "name": "John Doe",
        "headline": "Software Developer at TechCorp",
        "location": "San Francisco, CA",
        "about": "Experienced developer passionate about building impactful software.",
        "skills": ["Python", "React", "Spring Boot"],
        "projects": [
            {"title": "Chat App", "desc": "A real-time chat app using WebSocket."},
            {"title": "Portfolio Generator", "desc": "Tool to create auto portfolios."}
        ]
    }

@app.route("/api/generate", methods=["POST"])
def generate():
    data = request.get_json()
    linkedin_id = data.get("linkedinId")
    user_data = get_mock_linkedin_data(linkedin_id)
    return render_template("portfolio.html", **user_data)

@app.route("/portfolio")
def view_portfolio():
    user_data = get_mock_linkedin_data("mock")
    return render_template("portfolio.html", **user_data)

@app.route("/")
def home():
    return "LinkedIn Portfolio Generator Backend"

if __name__ == "__main__":
    app.run(debug=True)
