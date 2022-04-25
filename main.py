import telebot
from To_Do_Tg_Bot.secret import TOKEN
import pretty_errors
import sqlite3 as sql

con = sql.connect('tasks.db')
cursor = con.cursor()

bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Ну давай, запусти меня. Запусти меня полностью, я хочу, чтоб ты запустил меня")



@bot.message_handler(commands=['добавить тудудики'])
def do_


