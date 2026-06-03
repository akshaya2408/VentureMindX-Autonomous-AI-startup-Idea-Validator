from services.gemini_service import ask_gemini

def generate_personas(idea):

    prompt = f"""

    Startup Idea:
    {idea}

    Generate 3 customer personas.

    For each persona include:

    Name
    Age
    Occupation
    Pain Points
    Goals
    Buying Behaviour

    """

    return ask_gemini(prompt)