#created by shivendra singh on 21 august 2017

import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener



#my OAuth creditionals

# please use your personal keys or ask me
consumer_key =''
consumer_secret =''
access_token =''
access_secret =''

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)


def keywordsearch():
    keyword = raw_input("\nEnter your keyword  : ")

    listtweet = tweepy.Cursor(api.search, keyword).items(20)

    for tweet in listtweet:
          print tweet.text
    raw_input("\n********press any key to go to main menu************")



# function for real tym streaming
def  realtimesearch():
    keyword = raw_input("\nEnter your keyword to close streaming stop the program : ")
    class MyListener(StreamListener):

        def on_data(self, data):
            try:
                with open('Fedsir.json', 'a') as f:
                    f.write(data)
                    return True
            except BaseException as e:
                print("Error on_data: %s" % str(e))
            return True

        def on_error(self, status):
            print(status)
            return True

    twitter_stream = Stream(auth, MyListener())
    twitter_stream.filter(track=[keyword])


i=1
# driving menu
while i!=0:
    print("***********************************Main Menu**********************************\n\n")
    print("         1. Keyword wise search\n")
    print("         2. Realtime tweet search\n(warning need to quit Asap to avoid large dump of tweets)\n\n")
    print("******************************************************************************\n\n")

    i=int(input("Enter your option 0 to exit"))

    if i==1:
        keywordsearch()
    if i==2:
        realtimesearch()
    if i==0:
        exit()










