from youtube_statistics import YTstats
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

channel_id = os.getenv("channel_id")
channel_id2 = os.getenv("channel_id2")
channel_id3 = os.getenv("channel_id3")

yt = YTstats(API_KEY, channel_id)
yt.get_channel_statistics()
yt.get_channel_video_data()
yt.dump()


yt = YTstats(API_KEY, channel_id2)
yt.get_channel_statistics()
yt.get_channel_video_data()
yt.dump()

yt = YTstats(API_KEY, channel_id3)
yt.get_channel_statistics()
yt.get_channel_video_data()
yt.dump()