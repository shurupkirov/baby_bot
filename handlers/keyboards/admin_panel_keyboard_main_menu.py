from aiogram import types

#Создаем клавиатуру админпанели
admin_panel_keyboard_main_menu = types.InlineKeyboardMarkup()

#Создаем кнопку клавиатуры создания поста
ap_btn_cp = types.InlineKeyboardButton('Создать пост', callback_data='create_post')

#Создаем кнопку клавиатуры удаления поста
ap_btn_dp = types.InlineKeyboardButton('Удалить пост', callback_data='delete_post')

#Добавляем кнопку в клаву
admin_panel_keyboard_main_menu.row(ap_btn_cp, ap_btn_dp)