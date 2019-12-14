#!/usr/bin/env python
import TelegramBotAPI
from pytube import YouTube
import telebot
import os

bot = telebot.TeleBot('916677436:AAEbJdYesuKAMOWslIWJ-kq5_pgfBOpaAwU')



@bot.message_handler(content_types=['text', 'video'])
def get_text_messages(message):
    prov = 'https://youtu.be/'
    desc = 'https://www.youtube.com/watch?'
    if prov[:30] or desc in message.text:
        bot.send_message(message.from_user.id, "Ваше видео уже в пути!")
        video_mp4 = YouTube(message.text).streams.first().download()
        p = os.path.abspath(video_mp4)
        p = p.replace("\\", "/")
        video = open(p, 'rb')
        bot.send_video(message.from_user.id, video)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Пока я только могу скачивать видео с ютуб")
    else:
        bot.send_message(message.from_user.id, "Ссылка неверна!")



bot.polling()