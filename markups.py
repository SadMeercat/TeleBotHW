from telebot import types

start_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
start_markup_btn1 = types.KeyboardButton('/start')
start_markup.add(start_markup_btn1)

source_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
source_markup_btn1 = types.KeyboardButton('Список контактов')
source_markup_btn2 = types.KeyboardButton('Расписание дел')
source_markup.add(source_markup_btn1,source_markup_btn2)

contacts_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
tmp_list = ['Посмотреть контакты','Добавить контакт',
'Удалить контакт', 'Найти по имени', 'Найти по номеру', 'Экспорт',
'Импорт']

for i in tmp_list:
    tmp_btn = types.KeyboardButton(i)
    contacts_markup.add(tmp_btn)
