from services.search_service import get_competitor_data
from services.gemini_service import ask_gemini
import json

def competitor_analysis(idea):

    data = get_competitor_data(idea)

    prompt = f"""

    Startup:
    {idea}

    Research:
    {data}

    Return ONLY JSON.

    {{
      "competitors":[
        {{
          "name":"",
          "pricing":"",
          "strength":"",
          "weakness":""
        }}
      ],
      "market_gap":""
    }}

    """

    response = ask_gemini(prompt)

    return json.loads(response)