import subprocess
import logging


def check_imagemagick_installed():
    try:
        subprocess.run(["convert", "-version"], check=True,
                       stdout=subprocess.PIPE,)
        return True
    except FileNotFoundError:
        logging.error(
            'imagemagick is not installed. This tool is required.')
        logging.error(
            'imagemagick install ffmpeg manually: https://imagemagick.org/script/download.php')
        return False
