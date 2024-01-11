import subprocess
import logging


def is_ffmpeg_installed():
    try:
        subprocess.run(["ffmpeg", "-version"], check=True,
                       stdout=subprocess.PIPE,)
        return True
    except FileNotFoundError:
        logging.error(
            'ffmpeg is not installed. This tool is required.')
        logging.error(
            'Please install ffmpeg manually: https://ffmpeg.org/download.html')
        return False
