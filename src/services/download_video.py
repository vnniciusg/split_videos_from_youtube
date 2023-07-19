import re
from pytube import YouTube


def download_video(url, save_path):
    yt = YouTube(url=url)

    video_title = yt.title

    video = (
        yt.streams.filter(progressive=True, file_extension="mp4")
        .order_by("resolution")
        .desc()
        .first()
    )

    filename = f"{video_title}.mp4"
    filename = re.sub(r"\|", "", filename)

    video.download(filename=filename, output_path=save_path)
