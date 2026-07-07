import yt_dlp

def download_video(url: str):
    ydl_opts = {
        "quiet": True,
        "skip_download": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

    return {
        "title": info.get("title"),
        "duration": info.get("duration"),
        "channel": info.get("uploader"),
        "thumbnail": info.get("thumbnail"),
    }