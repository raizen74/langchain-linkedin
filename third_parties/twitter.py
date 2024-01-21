import os
import logging
import tweepy
from dotenv import load_dotenv
load_dotenv()

logger = logging.getLogger("twitter")

auth = tweepy.OAuthHandler(os.environ.get('TWITTER_API_KEY'), os.environ.get('TWITTER_API_SECRET'))
auth.set_access_token(os.environ.get('TWITTER_ACCESS_TOKEN'), os.environ.get('TWITTER_ACCESS_SECRET'))
api= tweepy.API(auth)

api.user_timeline(screen_name="O", count=1)
twitter_client.get_user(username="hwchase17")
# user_id = twitter_client.get_user(username="@elonmusk").data.id
# tweets = twitter_client.get_users_tweets(
#     id=user_id, max_results=num_tweets, exclude=["retweets", "replies"]
# )

# def scrape_user_tweets(username, num_tweets=5):
#     """
#     Scrapes a Twitter user's original tweets (i.e., not retweets or replies) and returns them as a list of dictionaries.
#     Each dictionary has three fields: "time_posted" (relative to now), "text", and "url".
#     """
#     user_id = twitter_client.get_user(username=username).data.id
#     tweets = twitter_client.get_users_tweets(
#         id=user_id, max_results=num_tweets, exclude=["retweets", "replies"]
#     )

#     tweet_list = []
#     for tweet in tweets.data:
#         tweet_dict = {}
#         tweet_dict["text"] = tweet["text"]
#         tweet_dict["url"] = f"https://twitter.com/{username}/status/{tweet.id}"
#         tweet_list.append(tweet_dict)

#     return tweet_list


# if __name__ == "__main__":
#     print(scrape_user_tweets(username="hwchase17"))