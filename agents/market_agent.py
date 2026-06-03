from services.search_service import (
    get_market_data
)

from services.gemini_service import (
    ask_gemini_json
)


def market_analysis(idea):

    web_data = get_market_data(
        idea
    )

    prompt = f"""

    Startup Idea:
    {idea}

    Research Data:
    {web_data}

    Return ONLY JSON.

    {{
        "tam": "",
        "sam": "",
        "som": "",
        "trends": [],
        "opportunities": []
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