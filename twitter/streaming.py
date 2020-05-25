import sys
import string
import time
import json
from tweepy import Cursor
from tweepy import Stream
from tweepy.streaming import StreamListener
from twitter_client import get_twitter_auth
from twitter_client import get_twitter_client

def from_creator(status):
    if hasattr(status, 'retweeted_status'):
        return False
    elif status.in_reply_to_status_id != None:
        return False
    elif status.in_reply_to_screen_name != None:
        return False
    elif status.in_reply_to_user_id != None:
        return False
    else:
        return True

class CustomLsitener(StreamListener):

	def on_status(self, status):
		if from_creator(status):
			try:
				print(status.text)
				with open("test.txt", 'a') as file:
					file.write(status.text)
				return True
			except BaseException as e:
				sys.stderr.write("Error on_data: {}\n".format(e))
			time.sleep(5)
		return True

	def on_error(self, status):
		if status == 420:
			sys.stderr.write("Rate limit exceeded\n")
			return False
		else:
			sys.stderr.write("Error {}\n".fomat(status))
			return True

if __name__ == '__main__':
	
	auth = get_twitter_auth()
	client = get_twitter_client()

	follow_list = []

	for friend in Cursor(client.friends).items():
		follow_list.append(str(friend.id))

	myStreamListener = CustomLsitener()
	twitter_stream = Stream(auth=auth, listener=myStreamListener )
	twitter_stream.filter(follow=follow_list, is_async=True)