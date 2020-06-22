import pytube
import  structures
from collections import namedtuple


class UploadVideo(object):
    def __init__(self, url: str = None) -> None:
        self.__url = url
        self.__session = pytube.YouTube(self.__url)

    def download(self) -> namedtuple:
        video = self.__session.streams.first()
        video.download()
        return structures.MessageUploadVideo(title=self.filename)

    def url(self) -> str:
        return str(self.__url)

    def session(self) -> pytube.__main__.YouTube:
        return self.__session

    @property
    def filename(self) -> str:
        return self.__session.title


