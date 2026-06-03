from typing import TypedDict, Dict, Any, List


class StartupState(TypedDict):
    idea: str

    # shared memory layer
    context: Dict[str, Any]

    market: Dict[str, Any]
    competitors: Dict[str, Any]
    personas: List[Dict[str, Any]]

    swot: Dict[str, Any]
    viability: Dict[str, Any]
    revenue: Dict[str, Any]
    investor: Dict[str, Any]