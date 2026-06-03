from services.gemini_service import ask_gemini

def viability_score(idea):

    prompt = f"""

    Startup Idea:
    {idea}

    Rate out of 10:

    Market Need
    Competition
    Monetization
    Scalability
    AI Advantage

    Then calculate

    Startup Viability Score
    out of 100.

    Give explanation.

    """

    return ask_gemini(prompt)