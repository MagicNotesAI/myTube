import os
from pytubefix import YouTube
from pytubefix.cli import on_progress


def download_video(url):
    yt = YouTube(url, on_progress_callback = on_progress)
    print(yt.title)
     
    ys = yt.streams.get_highest_resolution()
    ys.download("./data")


if __name__ == "__main__":
    # video_url = 'https://www.youtube.com/watch?v=2lAe1cqCOXo'
    # video_url = 'https://www.youtube.com/watch?v=95ZtpMVHIQY'
    # video_url = 'https://www.youtube.com/watch?v=r3_41Whvr1I'
    # video_url = 'https://www.youtube.com/watch?v=0TNTlMZFTWw'
    # video_url = 'https://www.youtube.com/watch?v=LdUNaXODE7s'
    video_url = 'https://www.youtube.com/watch?v=qE5BWFRETdk'

    download_video(video_url)

    

