import yt_dlp
import os
from pathlib import Path

def download_as_mp3(url, output_dir):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'postprocessor_args': [
            '-id3v2_version', '3'
        ],
        'prefer_ffmpeg': True,
        'ffmpeg_location': r'C:\Users\coold\ffmpeg\ffmpeg-8.0-essentials_build\bin',
        'noplaylist': True,
        'quiet': False
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading -> {url}")
            ydl.download([url])
            print("✅ Done!")
            return True
    except Exception as e:
        print(f"❌ Error downloading {url}: {e}")
        return False

def main():
    youtube_urls = [
        "https://youtu.be/cmE1yMO-PI4?si=1lC6U5pV8FFhv2iz",
        "https://youtu.be/HVGi0HeulZA?si=vNSbZ3Sjz5E_iGCz",
        "https://youtu.be/46zOfERr2g0?si=g06bpC7zanh8UFNO"
    ]

    download_dir = r"C:\Users\coold\Downloads\YouTubeMP3s"
    Path(download_dir).mkdir(parents=True, exist_ok=True)

    success = 0
    fail = 0

    for url in youtube_urls:
        if download_as_mp3(url, download_dir):
            success += 1
        else:
            fail += 1

    print("\n📌 Summary:")
    print(f"✅ Successful: {success}")
    print(f"❌ Failed: {fail}")

if __name__ == "__main__":
    main()

# command -> " python youtube_em_pee_three_scraper.py "