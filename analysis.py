# analysis.py
import google.generativeai as genai

# Configure Gemini API (Replace with your actual API Key)
genai.configure(api_key="AIzaSyCQJ3ql8J6LHPbuFyluESWW23h5oat_X5c")

def get_soca_analysis(user_responses):
    prompt = f"""
    You are an AI expert analyzing a student's JEE preparation.
    Based on these responses, generate a SOCA (Strengths, Opportunities, Challenges, Action Plan) report.

    Student Responses:
    {user_responses}

    Provide:
    - Strengths
    - Opportunities
    - Challenges
    - Action Plan
    """
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"
