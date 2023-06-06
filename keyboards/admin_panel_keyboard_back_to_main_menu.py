from aiogram import types

#Создаем клавиатуру админпанели
admin_panel_keyboard_back_to_main_menu = types.InlineKeyboardMarkup()

#Создаем кнопку клавиатуры основного меню
ap_btn_mm = types.InlineKeyboardButton('Вернуться в главное меню', callback_data='main_menu')

#Добавляем кнопку в клаву
admin_panel_keyboard_back_to_main_menu.row(ap_btn_mm)