from pathlib import Path
from typing import List, Optional
from foxlator_lib.video import Video
from foxlator_lib.stt.whisper_stt import WhisperSTT, AudioTextSegment


def get_subtitles_for_movie(video: Video, model_size: str, lang: Optional[str] = None) -> List[AudioTextSegment]:
    audio = video.get_audio_path()
    return WhisperSTT(model=model_size, language=lang).audio_to_text(audio)


def gen_movie_with_subtitles(movie_path: Path, destination: Path, model_size: str, lang: Optional[str] = None) -> Path:
    video = Video(movie_path)
    subtitles = get_subtitles_for_movie(video, model_size, lang)
    return video.apply_subtitles(subtitles, destination)
