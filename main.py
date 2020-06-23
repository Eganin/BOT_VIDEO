import logging
import text_bot as tb
import os
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
from upload_video import UploadVideo
from audio import AudioDelimeter, remove_files, open_mp3
from database import SQLither
from handlers import handler_data_user


load_dotenv()  # download .env

TOKEN = str(os.getenv('TG_TOKEN'))  # Token BY BotherFather

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

database = SQLither('data')  # init to database


@dp.message_handler(commands=['start'])
async def start(message: types.Message) -> None:
    '''Функция отвечающая за приветствие бота'''
    await message.answer(tb.HELLO)


@dp.message_handler(commands=['help'])
async def help(message: types.Message) -> None:
    '''Функция отвечает за помощь пользователю'''
    await message.answer(tb.HELP)


@dp.message_handler(commands=['users'])
async def users_info(message: types.Message) -> None:
    '''Функция которая отдает информацию о пользователе'''
    try:
        data = handler_data_user(list(database.get_users()))
        if len(data) < 1:
            await message.answer(tb.CLEAR_DB)

        await message.answer(tb.DATA_USERS)
        for k, v in data.items():
            for result in v:
                await message.answer(f'user_id={k}:Видео={result}')
    except:
        await message.answer('Произошда ошибка во время обращения к базе данных')


@dp.message_handler(commands=['delete_data'])
async def delete_data_user(message: types.Message) -> None:
    '''Удаление юзера из базы данных по его же id'''
    try:
        user_id = message.from_user.id
        database.delete_all(user_id)
        await message.answer(tb.DELETE_COMPLETE)

    except:
        await message.answer('Произошда ошибка во время обращения к базе данных')


@dp.message_handler(regexp=r'((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)')
async def to_accept_url_user(message: types.Message) -> None:
    '''Функция обрабатывает ссылку пользователя'''
    user_id = str(message.from_user.id)  # user id
    await message.answer(tb.PROCESS)
    try:
        video = UploadVideo(str(message))  # init video class
        mess = video.download()  # download video
        await message.answer(mess.title)

    except:
        await message.answer('Ошибка обработки видео')

    try:
        database.add_user(user_id, mess.title)  # add user to database

    except:
        await message.answer('Произошла ошибка во время обращения к базе данных')

    try:
        audio = AudioDelimeter(mess.title)
        audio_road = audio.delimiter()  # split audio tray from video
        audio.save_audio(audio_road)  # save audio tray
        doc = open(str(open_mp3()), 'rb')  # open file
        await bot.send_document(message.from_user.id, doc)  # return file from messsage
        remove_files()  # removes files

    except:
        await message.answer('Ошибка обработки видео')


@dp.message_handler(lambda message: message)
async def delete_other(message: types.message):
    try:
        user_id = message.from_user.id
        text = message.text
        database.delete_user(user_id, text)
        await message.answer(tb.DELETE_COMPLETE)

    except:
        await message.answer('Произошда ошибка во время обращения к базе данных')


if __name__ == '__main__':
    database.check_init_database()  # check to init database
    executor.start_polling(dp, skip_updates=True)
