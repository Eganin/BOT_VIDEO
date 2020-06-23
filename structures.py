from typing import NamedTuple


class MessageUploadVideo(NamedTuple):
    '''tuple для отправки сообщения с названием видеоролика'''
    title: str
