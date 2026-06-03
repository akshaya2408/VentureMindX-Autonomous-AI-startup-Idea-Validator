from services.gemini_service import ask_gemini

def swot_analysis(idea):

    prompt = f"""

    Startup Idea:
    {idea}

    Generate SWOT Analysis.

    Include:

    Strengths
    Weaknesses
    Opportunities
    Threats

    """

    return ask_gemini(prompt)