import telebot
import pretty_errors
import sqlite3 as sql
import os
from telebot import types
import time

TOKEN = '5358080391:AAFDzoHlb8xiwSQCAeuhC_pOtRlqkxD0dvU'
bot = telebot.TeleBot(TOKEN)

keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
item1=types.InlineKeyboardButton("/new_task")
item2=types.InlineKeyboardButton("/delete")
item3=types.InlineKeyboardButton("/all")
item4=types.InlineKeyboardButton("/start")
item5=types.InlineKeyboardButton("/help")
keyboard.add(item1,item2,item3,item4,item5)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Ну давай, запусти меня. Запусти меня полностью, я хочу, чтоб ты запустил меня")
    if not os.path.exists(str(message.from_user.id)):
        os.mkdir(str(message.from_user.id))                                                    
        f = open(os.getcwd() +"\\"+ str(message.from_user.id) + '\\tasks.txt', 'w')             
        f.close()
    answer="Привет!) \nЯ ботяра Никитоса. \nНапиши мне /help, чтобы получить инфу о том, что я могу делать"
    bot.send_message(message.from_user.id, answer,reply_markup=keyboard)
    
        
@bot.message_handler(commands=['help'])                                                        
def help_handler(message):                                                                      
    answer="Привет!) \nЯ бот todo. \nНапиши мне /start, чтобы я наахуй запустился. \n"+\
    "/new_item <название задачи> - добавь новую задачу ебобо\n "+\
    "/all - вывел тебе блять все.\n "+\
    "/delete <номер задачи> - нахуй эту задачу"
    bot.send_message(message.from_user.id, answer,reply_markup=keyboard)                          
        
        
@bot.message_handler(commands=['new_task'])                                                 
def new_item_handler(message):                                                                 
    f = open(os.getcwd() +"\\"+ str(message.from_user.id) + '\\tasks.txt', 'a')
    if len(message.text.split())>1:
        f.write(' '.join(message.text.split()[1:]) +'\n')
    else: 
        bot.send_message(message.from_user.id, "И че ты молчишь?",reply_markup=keyboard)
    f.close()
        

@bot.message_handler(commands=['all'])                                                         
def all_handler(message):
    filename = os.getcwd() +"\\"+ str(message.from_user.id) + '\\tasks.txt'
    answer=''
    i=1
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        with open(filename, 'r') as f:
            for line in f:
                answer += str(i)+'. ' + line 
                i+=1
        bot.send_message(message.from_user.id, answer)
    else:
        bot.send_message(message.from_user.id, "В списке задач нихуя.",reply_markup=keyboard)
    

@bot.message_handler(commands=['delete'])                                                     
def delete_handler(message):
    if '<' not in message.text and '>' not in message.text and len(message.text.split())>1:
        i = int(message.text.split()[-1])
    
        filename = os.getcwd() +"\\"+ str(message.from_user.id) + '\\tasks.txt'
        with open(filename, 'r') as f:
            lines = f.readlines()
        del lines[i-1]
        
        with open(filename, 'w') as f:
            f.write(''.join(lines))
        
    else:
        bot.send_message(message.from_user.id, "После комманды /delete введи только число еблан,нах мне твой текст",reply_markup=keyboard)
bot.polling()


