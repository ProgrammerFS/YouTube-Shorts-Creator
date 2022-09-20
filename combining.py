from reddit import get_memes
from resize import resize
from vid import make_video
import glob
from upload import upload

client_id = "Paste client id from reddit app"
client_secret = "Paste client secret from reddit app"
user_agent = "Paste user agent from reddit app"

def generate_and_upload(l):
    for i in l:
        # we start off by getting memes
        get_memes(i, client_id, client_secret, user_agent)

        # resize them
        for filename in glob.glob('./*.jpg'):
            resize(filename)

        # make a video
        make_video()

        # upload the video
        upload()

