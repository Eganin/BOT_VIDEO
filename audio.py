import moviepy.editor
import os
import random


class AudioDelimeter(object):
    def __init__(self, namevideo: str) -> None:
        self.filename = self.file_search()
        self.namevideo = namevideo

    def file_search(self) -> str:
        for root, dirs, files in os.walk("."):
            for file in files:
                if file.endswith('.mp4') and root == '.':
                    return str(file)

    def delimiter(self) -> moviepy.audio.io.AudioFileClip.AudioFileClip:
        video = moviepy.editor.VideoFileClip(self.filename)
        audio = video.audio
        return audio

    def save_audio(self, audio: moviepy.audio.io.AudioFileClip.AudioFileClip) -> None:
        audio.write_audiofile(self.namevideo + '.mp3')


def remove_files() -> None:
    pass


def open_mp3() -> str:
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith('.mp3') and root == '.':
                return str(file)

