"""
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
token_bot = ""
bot = Bot(token=token_bot)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(msg: types.Message):
    await msg.reply_to_message(f'Я бот. Приятно познакомиться, {msg.from_user.first_name}')

@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.Message):
    if msg.text.lower() == 'привет':
        await msg.answer('Привет!')
    else:
        await msg.answer('Не понимаю, что это значит.')
"""

import logging
from aiogram import Bot, Dispatcher, executor, types
from dotenv import dotenv_values

config = dotenv_values(".env")
token_bot = config['API_TOKEN']

logging.basicConfig(level=logging.INFO)

bot = Bot(token=token_bot)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help', 'stop'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Это бот")

@dp.message_handler()
async def echo_text(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
   executor.start_polling(dp)