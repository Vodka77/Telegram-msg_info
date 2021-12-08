import telebot 
import requests
import random 
import vodka
from telebot import types
from time import sleep
import time
import os,sys
def vodka(s):
 for ASU in s + '\n':
  sys.stdout.write(ASU)
  sys.stdout.flush()
  sleep(2./600)
Z = '\x1b[1;31m'#احمر
X = '\x1b[1;32m'#اخضر
C = '\x1b[1;33m'#yellow
V = '\x1b[1;34m'#blue 
B = '\x1b[1;35m'#pink
N = '\x1b[1;36m'#لبني
M = '\x1b[1;37m'#ابيض  
t = time.localtime()
current_time = time.strftime('%H:%M:%S', t)
current_date =  time.strftime('%D', t)
vodka(X+'__     _  ____  _      _    ')
vodka(Z+'\ \   / / _ \|  _ \| |/ /   / \   ')
vodka(X+' \ \ / / | | | | | |   /   / _ \  ')
vodka(Z+'  \ V /| |_| | |_| | . \  / _ \ ')
vodka(X+'   \_/  \___/|____/|_|\_\/_/   \_\ ')
vodka(N+'Time Now : '+M+current_time)
vodka(N+'Date Now : '+M+current_date)
vodka(M+'- - - - - - - - - - - - - - - - - - - - ')
vodka(Z+'('+X+'⌯'+Z+')'+N+'Telegram : '+M+'@Vodka_tk')
vodka(Z+'('+X+'⌯'+Z+')'+N+'GitHub : '+M+'https://github.com/Vodkahunter.com')
vodka(Z+'('+X+'⌯'+Z+')'+N+'Program Code : '+M+'python3')
vodka(Z+'('+X+'⌯'+Z+')'+N+'Program App : '+M+'vscode')
vodka(M+'- - - - - - - - - - - - - - - - - - - - ')
Token = input(N+'('+B+'⌯'+N+')'+B+'Enter Token : '+M)
bot = telebot.TeleBot(Token)
co = types.InlineKeyboardButton(text ="- Dev Channel",url='https://t.me/Vodka_Tools')
@bot.message_handler(commands=['start'])
def first(message):
    maac = types.InlineKeyboardMarkup()
    maac.row_width = 2
    maac.add(co)    
    bot.send_message(message.chat.id , f'<b>Hi VODKA #1st - python☬\n- - - - - - - - - - - - - -\nWelcome To Telegram Msg-Info!\nSend Any msg-link To Get Info!\n- - - - - - - - - - - - - -\nBy  : @Vodka_tk</b>', parse_mode="html",reply_to_message_id=message.message_id, reply_markup=maac)

@bot.message_handler(func=lambda m:True)  
def good(message):
    try:
        msg = message.text    
        sleep(2) 
        bot.reply_to(message,f'*- Wait Bro*', parse_mode='markdown') 
        sleep(1)            
        ur = requests.get(f"https://apis.red/api/teleinfo/?url={msg}").json()
        q = ur['date']
        w = ur['msg']
        e = ur['views']  
        bot.send_message(message.chat.id,f'*Hi VODKA #1st - python☬ Done Get Info\n- - - - - - - - - - - -\nMsg-Date : '+q+'\nMsg : '+w+'\nMsg-View : '+e+'\n- - - - - - - - - - - -\nBY : @VODKA_Tk*',parse_mode='markdown')  
    except:
        pass
bot.polling(True)
