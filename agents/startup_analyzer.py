from services.gemini_service import ask_gemini_json


def startup_analysis(idea):

    prompt = f"""
You are an expert startup VC analyst.

Analyze the startup idea and return ONLY valid JSON.

Startup Idea:
{idea}

Return structure:

{{
  "market_analysis": {{
    "tam": "",
    "sam": "",
    "som": "",
    "trends": [],
    "opportunities": []
  }},

  "competitor_analysis": {{
    "competitors": [
      {{
        "name": "",
        "pricing": "",
        "strength": "",
        "weakness": ""
      }}
    ],
    "market_gap": ""
  }},

  "personas": [
    {{
      "name": "",
      "role": "",
      "pain_points": []
    }}
  ],

  "swot": {{
    "strengths": [],
    "weaknesses": [],
    "opportunities": [],
    "threats": []
  }},

  "viability": {{
    "score": 0,
    "reason": ""
  }},

  "revenue_forecast": {{
    "year_1": "",
    "year_2": "",
    "year_3": "",
    "assumptions": []
  }},

  "investor_readiness": {{
    "vc_score": 0,
    "scalability": 0,
    "moat": 0,
    "defensibility": 0,
    "market_fit": 0,
    "summary": ""
  }}
}}

Rules:
- Return ONLY JSON
- No markdown
- No explanations
- Be realistic and data-driven
"""

    result = ask_gemini_json(prompt)

    if not result["success"]:

        return {
            "success": False,
            "error": result["error"]
        }

    return result["data"]