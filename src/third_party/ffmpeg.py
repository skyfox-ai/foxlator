from .utils.system import check_if_installed


def is_ffmpeg_installed():
    return check_if_installed("ffmpeg", "ffmpeg -version", True)
