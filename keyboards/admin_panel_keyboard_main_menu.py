from aiogram import types

#Создаем клавиатуру админпанели
admin_panel_keyboard_main_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)

#Создаем кнопку клавиатуры добавления няни
ap_btn_cb = types.KeyboardButton('Добавить няню', callback_data='create_babysitter')

#Создаем кнопку клавиатуры удаления поста
ap_btn_db = types.KeyboardButton('Удалить няню', callback_data='delete_babysitter')

#Создаем кнопку запроса информации за последний час
ap_btn_eh = types.KeyboardButton('События за последний час', callback_data='event_last_hour')

#Создаем кнопку запроса информации за текущий день
ap_btn_cd = types.KeyboardButton('События за день', callback_data='event_current_day')

#Добавляем кнопку в клаву
admin_panel_keyboard_main_menu.row(ap_btn_cb, ap_btn_db, ap_btn_eh, ap_btn_cd)