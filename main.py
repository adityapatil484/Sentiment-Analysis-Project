from youtube_statistics import YTstats

API_KEY = "AIzaSyDcSKXYoV-bs7xr4F7ZtwGJZRgFu1p9Mh8"
channel_id = "UCUFgkRb0ZHc4Rpq15VRCICA"
channel_id2 = "UCZq427EjGqUbV6pZIjEKkgg"
channel_id3 = "UCuLUOxd7ezJ8c6NSLBNRRfg"

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