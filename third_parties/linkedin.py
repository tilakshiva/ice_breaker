import os
import requests
from dotenv import load_dotenv


load_dotenv()

def parseLinkedInUrlName(url:str):
    """
    Parse the LinkedIn URL to extract the profile ID.
    Args:
        url (str): The LinkedIn profile URL.
    Returns:
        str: The extracted profile ID.
    """
    if "linkedin.com/in/" in url:
        return url.split("linkedin.com/in/")[1].split("/")[0]
    else:
        raise ValueError("Invalid LinkedIn URL")



def scrape_linkedin_profile_info(linkedin_profile_url:str, mock:bool= False):
    """
    Scrape information from a LinkedIn profile page.
    Manually scrape the information from the LinkedIn Profile page.
    Args:
        linkedin_profile_url (str): The URL of the LinkedIn profile to scrape.
        mock (bool): If True, return mock data instead of scraping. Default is False."""
    
    if mock: 
        linkedin_profile_url = "https://gist.githubusercontent.com/tilakshiva/26b3e981a15d801b32aa2159b0712cd5/raw/7941ad18eb73359ceeed215d20308ebc9cde53f5/Shivajee-gupta-linkedin-scrapin.json"
        response = requests.get(
            linkedin_profile_url,
            timeout=10)
    else:
        scrapein_url="https://api.scrapingdog.com/linkedin"
        api_key = os.getenv('SCRAPE_API_KEY')
        profile_name= parseLinkedInUrlName(linkedin_profile_url)
        params = {
            "api_key": api_key,
            "type": "profile",
            "linkId": profile_name,
            "private": "false",
        }
  
        response = requests.get(scrapein_url, params=params)
        
    if response and response.status_code == 200:
        data = response.json()[0]
        data = {
            k: v
            for k, v in data.items()
            if v not in [[], "", ""]
            and k not in ["certifications", "skills", "languages"]
        }
        return data
    else:
        print(f"Request failed with status code: {response.status_code}")
        

if __name__ == "__main__":
    print(
        scrape_linkedin_profile_info(
            linkedin_profile_url="https://www.linkedin.com/in/shivajeegupta/", mock=True
        )
    )