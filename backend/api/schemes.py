from pydantic import BaseModel
from typing import List


class Competitor(BaseModel):
    name: str
    pricing: str
    strength: str
    weakness: str


class Persona(BaseModel):
    name: str
    age: str
    occupation: str
    goals: List[str]
    pain_points: List[str]


class StartupRequest(BaseModel):
    idea: str