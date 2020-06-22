import logging
import os.path
import text_bot as tb
import os
from aiogram import Bot, Dispatcher, executor, types
import asyncio
from dotenv import load_dotenv
from upload_video import UploadVideo
from audio import AudioDelimeter, remove_files, open_mp3
from database import SQLither

load_dotenv()

TOKEN = str(os.getenv('TG_TOKEN'))

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

database = SQLither('data')


@dp.message_handler(commands=['start'])
async def start(message: types.Message) -> None:
    await message.answer(tb.HELLO)


@dp.message_handler(commands=['help'])
async def help(message: types.Message) -> None:
    await message.answer(tb.HELP)


@dp.message_handler(regexp=r'((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)')
async def to_accept_url_user(message: types.Message):
    user_id = str(message.from_user.id)
    await message.answer(tb.PROCESS)
    video = UploadVideo(str(message))
    mess = video.download()
    await message.answer(mess.title)
    database.add_user(user_id, mess.title)
    audio = AudioDelimeter(mess.title)
    audio_road = audio.delimiter()
    audio.save_audio(audio_road)
    doc = open(str(open_mp3()), 'rb')
    await bot.send_document(message.from_user.id, doc)
    remove_files()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
