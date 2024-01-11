
from .utils.system import check_if_installed


def is_imagemagick_installed():
    return check_if_installed("imagemagick", "convert -version", True)
