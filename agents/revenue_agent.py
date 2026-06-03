from services.gemini_service import (
    ask_gemini_json
)


def revenue_forecast(idea):

    prompt = f"""
    Startup Idea:
    {idea}

    Generate a realistic startup revenue forecast.

    Return ONLY JSON.

    {{
        "year_1": "",
        "year_2": "",
        "year_3": "",
        "assumptions": [
            ""
        ]
    }}
    """

    result = ask_gemini_json(
        prompt
    )

    if not result["success"]:

        return {
            "status": "failed",
            "reason": result["error"]
        }

    return result["data"]