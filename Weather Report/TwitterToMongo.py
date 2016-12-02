from twython import TwythonStreamer
from pymongo import MongoClient
client = MongoClient()
db = client.twitter
tweets = db.twitterdata

tweeter = []
class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if data ['lang'] == 'en':
            tweeter.append(data)
            tweets.insert(data)
            print 'recieved tweet #', len(tweeter)

        if len(tweeter)>= 3000:
            self.disconnect()
    def on_error(self,status_code, data):
        print status_code, data
        self.disconnect()

stream = MyStreamer('eAL497dT5hjs2bHLh1mRoR3cj', 'HUuqoidPWbT04QPpZfFHwpqvLvq6IxOU1kOa2eRRZf8Rh5XmtE',
                        '775365291555651584-hhpeCLC8VY2ccOoeWxXge6cWbamKhBG',
                        'zzlkNqY4eaxCZ738GXhcTPmQf2L9RkO6uZot93a2ZJoF7')
stream.statuses.filter(track='london avalanche\
,london balmy\
,london black ice\
,london blizzard\
,london blustery\
,london breeze\
,london cloud\
,london cloudy\
,london cold\
,london condensation\
,london dew\
,london downburst\
,london downpour\
,london drizzle\
,london drought\
,london dry\
,london flood\
,london fog\
,london forecast\
,london freeze\
,london freezing\
,london frost\
,london gale\
,london gust\
,london gustnado\
,london hail\
,london haze\
,london heat\
,london heatwave\
,london humid\
,london humidity\
,london hurricane\
,london ice\
,london icicle\
,london lightning\
,london mist\
,london muggy\
,london overcast\
,london permafrost\
,london rain\
,london rainbands\
,london rainbow\
,london sandstorm\
,london sleet\
,london slush\
,london smog\
,london snow\
,london snowstorm\
,london storm\
,london summer\
,london sunrise\
,london sunset\
,london temperature\
,london thaw\
,london thunder\
,london thunderstorm\
,london tropical\
,london visibility\
,london warm\
,london weather\
,london wind\
,london winter')

#tweets.insert_many(tweeter)


