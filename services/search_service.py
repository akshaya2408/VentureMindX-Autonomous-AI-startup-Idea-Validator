from services.tavily_service import search_web

def get_market_data(idea):

    query = f"""
    Market size and trends for:
    {idea}
    """

    return search_web(query)


def get_competitor_data(idea):

    query = f"""
    Competitors for:
    {idea}
    """

    return search_web(query)