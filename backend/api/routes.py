from fastapi import APIRouter
from pydantic import BaseModel
from backend.pitch_deck_generator import create_pitch_deck
from vector_db.startup_rag import find_similar_startups


from backend.orchestrator import (
    analyze_startup
)
from vector_db.startup_rag import (
    find_similar_startups,
    get_all_records
)
router = APIRouter()

class StartupIdea(BaseModel):

    idea: str

@router.post("/analyze")
def analyze(data: dict):
    idea = data.get("idea", "")

    return {
        "startup": idea,

        "market_analysis": {
            "market_size": "₹1200 Cr",
            "growth_rate": "18% CAGR",
            "target_users": "College students, job seekers",
            "demand": "High demand due to AI adoption"
        },

        "competitors": [
            {
                "name": "PrepAI",
                "strength": "Mock interviews",
                "weakness": "No personalization"
            },
            {
                "name": "SkillVertex",
                "strength": "Course library",
                "weakness": "No real-time AI feedback"
            }
        ],

        "swot": {
            "strengths": ["AI automation", "Scalable platform"],
            "weaknesses": ["Early stage product"],
            "opportunities": ["Huge edtech growth"],
            "threats": ["Established players like Coursera"]
        }
    }
@router.get("/vector-records")
def vector_records():

    return get_all_records()
@router.get("/similar")
def similar_startups(
    query: str
):

    return find_similar_startups(
        query
    )
@router.post("/pitch-deck")
def pitch_deck(data: dict):

    report = analyze_startup(data["idea"])["data"]

    file_path = create_pitch_deck(report)

    return {
        "success": True,
        "file": file_path
    }

@router.post("/rag-search")
def rag_search(data: dict):

    query = data.get("query")

    if not query:
        return {
            "success": False,
            "error": "Query is required"
        }

    results = find_similar_startups(query)

    return {
        "success": True,
        "results": results
    }