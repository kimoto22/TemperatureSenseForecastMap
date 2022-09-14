import os
from dotenv import load_dotenv
import tweepy
import datetime


def convert_to_datetime(datetime_str):
    tweet_datetime = datetime.strptime(datetime_str,'%H:%M:%S')
    print(f"tweet_datetime:{tweet_datetime}")

    return (tweet_datetime)

def tweets(ido:float, keido:float):

    tweet_contents = {"tweet":[], "tweet_time":[]}

    #環境変数読み込み
    load_dotenv()
    bearer_token = os.environ['bearer_token']
    consumer_api_key = os.environ['consumer_api_key']
    consumer_api_secret_key = os.environ['consumer_api_secret_key']
    access_token = os.environ['access_token']
    access_token_secret = os.environ['access_token_secret']

    # Twitterオブジェクトの生成
    api = tweepy.Client(bearer_token, consumer_api_key, consumer_api_secret_key, access_token, access_token_secret,wait_on_rate_limit=True)

    # 検索パラメータ
    search = ['暑い']

    tweets = api.search_recent_tweets(query=search)

    # 投稿時間
    # tweet_datetime = convert_to_datetime(tweets['created_at'])

    #出力
    tweets_list = [tweet for tweet in tweets[0]]
    # tweet_contents["tweet_time"] = tweet_datetime
    [print("Tweet\n","="*20,"\n",_,"\n","="*20,"\n"*3) for _ in tweets_list]
    return tweets_list