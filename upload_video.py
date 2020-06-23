import pytube
import  structures
from collections import namedtuple


class UploadVideo(object):
    '''Класс отвечающий за загрузку видео'''
    def __init__(self, url: str = None) -> None:
        self.__url = url
        self.__session = pytube.YouTube(self.__url)

    def download(self) -> namedtuple:
        '''download youtube-video'''
        video = self.__session.streams.first()
        video.download()
        return structures.MessageUploadVideo(title=self.filename)

    def url(self) -> str:
        ''':return url'''
        return str(self.__url)

    def session(self) -> pytube.__main__.YouTube:
        ''':return sesion youtube'''
        return self.__session

    @property
    def filename(self) -> str:
        '''return filename video'''
        return self.__session.title


