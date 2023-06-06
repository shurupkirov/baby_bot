from aiogram import types
from config.config import dp, bot
from keyboards.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu

@dp.callback_query_handler(text='create_babysitter')
async def admin_panel_create_post_callback(callback_query: types.CallbackQuery):
    await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id)
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text=f"Укажите ID пользователя для добавления в няни",
                           reply_markup=admin_panel_keyboard_back_to_main_menu)

