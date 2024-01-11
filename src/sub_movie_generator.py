from pathlib import Path
from typing import List, Optional
from foxlator_lib.video import Video
from foxlator_lib.stt.whisper_stt import WhisperSTT, AudioTextSegment

from src.third_party.ffmpeg import check_ffmpeg_installed
from src.third_party.imagemagick import check_imagemagick_installed


class SubMovieGenerator:

    def __init__(self, movie_path: Path, model_size: str, lang: Optional[str] = None):
        if not check_ffmpeg_installed() or not check_imagemagick_installed():
            exit()
        self.video = Video(movie_path)
        self.lang = lang
        self._model_size = model_size
        self._whisper = WhisperSTT(model=self._model_size, language=lang)

    def get_subtitles_for_movie(self) -> List[AudioTextSegment]:
        audio = self.video.get_audio_path()
        return self._whisper.audio_to_text(audio)

    def gen_movie_with_subtitles(self, destination: Path) -> Path:
        subtitles = self.get_subtitles_for_movie()
        return self.video.apply_subtitles(subtitles, destination)
