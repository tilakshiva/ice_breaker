from langchain_community.tools.tavily_search import TavilySearchResults

def get_profile_url_tavily(name: str) -> str:
    """
    Get the LinkedIn or Twitter profile page of a person using Tavily search.
    
    Args:
        name (str): The full name of the person.
        
    Returns:
        str: The LinkedIn profile URL of the person.
    """
    
    search= TavilySearchResults()

    res= search.run(f"{name}")
    
    return res