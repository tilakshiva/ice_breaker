import os
import requests
import tweepy
from dotenv import load_dotenv
import re
load_dotenv()

twitter_client = tweepy.Client(
    bearer_token=os.getenv("TWITTER_BEARER_TOKEN"), 
    consumer_key=os.getenv("TWITTER_API_KEY"), 
    consumer_secret=os.getenv("TWITTER_API_SECRET_KEY"), 
    access_token=os.getenv("TWITTER_ACCESS_TOKEN"), 
    access_token_secret=os.getenv("TWITTER_ACCESS_TOKEN_SECRET") 
)

#https://gist.github.com/tilakshiva/67cb528a9222ee10a04058b03d431898

def scrape_twitter_profile_info(username:str, num_tweets:int=5, mock:bool=False):
    """
    Scraps a tweeter user's original tweets (i.e. not retweets or replies) and returns them as a list of dictionaries.
    Each ductionary has three fields: "time_posted" (relative to now), "text" and "url"
    """

    tweet_list = []

    if mock:
        # Mock data for testing purposes
        twitter_profile_url= "https://gist.githubusercontent.com/tilakshiva/67cb528a9222ee10a04058b03d431898/raw/774f90702dc28ab6966e73d5b7d44cd5bd53c1d2/gistfile1.txt"
        tweets = requests.get(
            twitter_profile_url,
            timeout=5              
        ).json()

    else:
        if re.match("^[a-zA-Z0-9_.-]+$", username) is not None:
            user_id=twitter_client.get_user(username=username).data.id
            tweets = twitter_client.get_users_tweets(
                id=user_id,
                max_results=num_tweets,
                exclude=["retweets", "replies"]
            )

    if tweets is not None:
        all_tweets = []
        if mock:
            all_tweets = tweets
        else:
            all_tweets = tweets.data
        
        for tweet in all_tweets:
            tweet_dict={}
            tweet_dict["text"] = tweet["text"]
            tweet_dict["url"]= f"https://twitter.com/{username}/status/{tweet['id']}"
            tweet_list.append(tweet_dict)

    
    
    return tweet_list



    
    # Actual scraping logic would go here
    # For example, using Tweepy or another library to fetch tweets from Twitter API
    # This is just a placeholder for the actual implementation
    return []




if __name__=="__main__":
    # Test the function with a sample username
    username = "elonmusk"
    tweets = scrape_twitter_profile_info(username=username, num_tweets=5, mock=True)
    print(tweets)
    
    