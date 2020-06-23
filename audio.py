import moviepy.editor
import os


class AudioDelimeter(object):
    '''Класс отвечающий за обработку видео'''

    def __init__(self, namevideo: str) -> None:
        self.filename = self.file_search()
        self.namevideo = namevideo

    def delimiter(self) -> moviepy.audio.io.AudioFileClip.AudioFileClip:
        '''Разделение видео на аудио-дорожку'''
        video = moviepy.editor.VideoFileClip(self.filename)
        audio = video.audio
        return audio

    def save_audio(self, audio: moviepy.audio.io.AudioFileClip.AudioFileClip) -> None:
        '''Save to audio road'''
        audio.write_audiofile(self.namevideo + '.mp3')

    @staticmethod
    def file_search() -> str:
        '''return video download'''
        for root, dirs, files in os.walk("."):
            for file in files:
                if file.endswith('.mp4') and root == '.':
                    return str(file)


def remove_files() -> None:
    '''remove to download files'''
    for root, dirs, files in os.walk('.'):
        for file in files:
            if (file.endswith('.mp3') and root == '.') or (file.endswith('.mp4') and root == '.'):
                os.remove(file)


def open_mp3() -> str:
    '''return audio road'''
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith('.mp3') and root == '.':
                return str(file)
