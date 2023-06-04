from aiogram import types
from config.config import dp, bot, admin_bot
from keyboards.admin_panel_keybord_main_menu import admin_panel_keybord_main_menu

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_id = message.from_user.id
    if user_id == admin_bot:
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"Ваш ID: {message.from_user.id}",
                               reply_markup=admin_panel_keybord_main_menu)
    else:
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"Ваш ID: {message.from_user.id}")

