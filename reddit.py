import praw
import urllib.request
import cv2
import glob

def get_memes(channel, client_id, client_secret, user_agent):
    reddit = praw.Reddit(client_id=client_id, client_secret= client_secret, user_agent= user_agent)
    count=0
    for submission in reddit.subreddit(channel).hot(limit=50):
        url = submission.url
        if url.endswith(('.jpg', '.png', '.jpeg')) and "/" not in submission.title:
            title = submission.title
            urllib.request.urlretrieve(url, f"{title}.jpg")
            count+=1
        if count==10:
            break