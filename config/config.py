import logging
from aiogram import Bot, Dispatcher
from dotenv import dotenv_values

config = dotenv_values("config/.env")
token_bot = config['API_TOKEN']
admin_bot = int(config['ADMIN_ID'])

logging.basicConfig(level=logging.INFO)

bot = Bot(token=token_bot)
dp = Dispatcher(bot)