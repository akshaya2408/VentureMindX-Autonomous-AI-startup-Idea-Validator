import json
import google.generativeai as genai
from google.api_core.exceptions import ResourceExhausted

from backend.config import settings

genai.configure(api_key=settings.GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def ask_gemini_json(prompt):

    try:
        response = model.generate_content(prompt)

        text = response.text.strip()

        # clean markdown garbage
        text = text.replace("```json", "")
        text = text.replace("```", "")
        text = text.strip()

        return {
            "success": True,
            "data": json.loads(text)
        }

    except json.JSONDecodeError:

        return {
            "success": False,
            "error": "Gemini returned invalid JSON",
            "raw_output": text if "text" in locals() else None
        }

    except ResourceExhausted:

        return {
            "success": False,
            "error": "Gemini quota exceeded (429)"
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }