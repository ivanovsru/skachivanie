#!/usr/bin/env python

from modules import pytube
from modules import telebot
import os





bot = telebot.TeleBot('916677436:AAEbJdYesuKAMOWslIWJ-kq5_pgfBOpaAwU')

@bot.message_handler(content_types=['text', 'video'])
def get_text_messages(message):
    prov = 'https://youtu.be/'
    desc = 'https://www.youtube.com/watch?'
    if prov in message.text and len(message.text)==28 or desc in message.text and len(message.text)==43:
        bot.send_message(message.from_user.id, "Ваше видео уже в пути!")
        video_mp4 = pytube.YouTube(message.text).streams.first().download()
        p = os.path.abspath(video_mp4)
        p = p.replace("\\", "/")
        video = open(p, 'rb')
        bot.send_video(message.from_user.id, video)
        video.close()
        os.remove(p)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Пока я только могу скачивать видео с ютуб")
    else:
        bot.send_message(message.from_user.id, "Ссылка неверна!")



bot.polling()