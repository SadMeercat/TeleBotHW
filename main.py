import telebot
import markups as m
from Task import Task
from GroupHW_Python_ContactBook import controller as cont_control

token = open("token", 'r').read()
bot = telebot.TeleBot(token)
task = Task()
global command


@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    if not task.isRunning:
        chat_id = message.chat.id
        bot.send_message(chat_id, 'Привет')
        msg = bot.send_message(chat_id, 'Выбери команду', 
        reply_markup=m.source_markup)
        bot.register_next_step_handler(msg, askAction)

def askAction(message):
    chat_id = message.chat.id
    text = message.text.lower()
    if text in task.names[0]:
        msg = bot.send_message(chat_id, "Открываю...", reply_markup=m.contacts_markup)
        bot.register_next_step_handler(msg, contacts)
    # elif text in task.names[1]:
    #     img = open(RI.GetRndImage(), 'rb')
    #     msg = bot.send_photo(chat_id, photo=img)
    #     bot.register_next_step_handler(msg, askAction)
    
def contacts(message):
    global command
    chat_id = message.chat.id
    text = message.text.lower()
    if text == task.command_contacts[0]:
        msg = bot.send_message(chat_id, cont_control.show_contacts())
        bot.register_next_step_handler(msg, contacts)
    elif text == task.command_contacts[1]:
        command = "add"
        msg = bot.send_message(chat_id, """Введите ФИО, номер и описание
        Пример:
        Иванов
        Иван
        Иванович
        +79876543210
        Был Иваном и остался Иваном""", reply_markup=None)
        bot.register_next_step_handler(msg,contacts_work)
    elif text == task.command_contacts[2]:
        command = "del"
        msg = bot.send_message(chat_id, "Введите id контакта", reply_markup=None)
        bot.register_next_step_handler(msg, contacts_work)
    elif text == task.command_contacts[3]:
        command = "upd"
        msg = bot.send_message(chat_id, '''Введите новые ФИО, номер и описание
        Пример:
        Иванов
        Иван
        Иванович
        +79876543210
        Был Иваном и остался Иваном
        (если изменения чего-либо не нужно, оставить строку пустой)
        ''', reply_markup=None)
        bot.register_next_step_handler(msg, contacts_work)
        return

def contacts_work(message):
    global command
    chat_id = message.chat.id
    text = message.text
    if command == "add":
        msg = bot.send_message(chat_id, cont_control.change_book('a', text), reply_markup=m.contacts_markup)
        bot.register_next_step_handler(msg, contacts)
    elif command == "del":
        msg = bot.send_message(chat_id,cont_control.change_book("d", text), reply_markup=m.contacts_markup)
    elif command == "upd":
        msg = bot.send_message(chat_id,cont_control.change_book("u", text), reply_markup=m.contacts_markup)

bot.polling()