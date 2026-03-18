import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_data(sector: str, data):
    model = genai.GenerativeModel("models/gemini-1.5-flash")

    context = "\n".join(data)

    prompt = f"""
    Create a detailed market analysis report for the {sector} sector in India.

    Data:
    {context}

    Format:

    # {sector.capitalize()} Market Analysis

    ## Market Trends
    - ...

    ## Opportunities
    - ...

    ## Risks
    - ...

    ## Final Insight
    - ...
    """

    return "# Technology Market Analysis\n\n## Market Trends\n- Growth observed\n\n## Opportunities\n- Startups rising\n\n## Risks\n- Competition\n\n## Final Insight\n- Positive outlook"

    return response.text
