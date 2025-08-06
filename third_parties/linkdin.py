import os
import requests
from dotenv import load_dotenv

load_dotenv()


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """
    Scrapes LinkedIn profile data from a given URL.
    
    Args:
        linkedin_profile_url: The LinkedIn profile URL to scrape
        mock: Whether to use mock data for testing
    
    Returns:
        Dictionary containing profile data
    """
    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/SDugtal/cde75dce09cf144278c44b395ddfe82c/raw/0d6d209e4770e622dfbf9fbd1e68bce16c025a50/sd-scraping.json"
        response = requests.get(
            linkedin_profile_url,
            timeout=10
        )
    else:
        api_endpoint = "https://api.scrapin.io/enrichment/profile"
        api_key = os.environ.get("SCRAPIN_API_KEY")
        
        if not api_key:
            raise ValueError("SCRAPIN_API_KEY not found in environment variables")
        
        params = {
            "apikey": api_key,
            "linkedInUrl": linkedin_profile_url,
        }
        response = requests.get(
            api_endpoint,
            params=params,
            timeout=10,
        )

    try:
        data = response.json()
        person_data = data.get("person", {})
        
        # Clean the data by removing empty values and unwanted fields
        cleaned_data = {
            k: v
            for k, v in person_data.items()
            if v not in ([], "", None) and k not in ["certifications"]
        }
        
        return cleaned_data
    
    except Exception as e:
        return {"error": f"Failed to scrape profile: {str(e)}"}


if __name__ == "__main__":
    try:
        result = scrape_linkedin_profile(
            linkedin_profile_url="https://www.linkedin.com/in/shirshak-dugtal-164b0b297/",
            mock=True
        )
        print(result)
    except Exception as e:
        print(f"Error: {e}")
