#! /usr/bin/env python3

# Author        :    InferiorAK
# Github        :    github.com/InferiorAK
# facebook      :    fb.com/InferiorAK
# Youtbe	:    youtube.com/@InferiorAk
# twitter	:    twitter.com/@InferiorAk
## 1st Release: 16th May 2023

# -------- Copyright (C) 2023 InferiorAK ------

from telegram.ext import (
	Updater,
	CommandHandler,
	MessageHandler,
	Filters
)
import requests
import socket
from time import time

TOKEN = "Your_Token"

updater = Updater(token=TOKEN, use_context=True)
disp = updater.dispatcher


def rest(msg):
	restricted = ["fuck", "f*ck", "motherfucker", "asshole"]
	for gali in restricted:
		if gali in msg:
			return True
		return False

def reply(update, context):
	msg = update.message.text.lower()
	out = update.message.reply_text
	user = update.message.from_user
	full_name = user.first_name + " " + user.last_name if user.last_name else user.first_name
	
	if rest(msg):
		out("Hey Bloody Asshole! Don't use bad words.")
	else:
		if "who are you" in msg:
			out(f"Hello! Mr. {full_name}. I am Mr. Guti")
		elif "how are you" in msg:
			out("I am fine")
		else:
			pass

doc = """
Command List
   /start   : To start Conversation
   /help    : See How to use
   /ipinfo  : Gather All Information of an IP.
   /about   : About Me
"""

user_last_message_time = {}

def start(update, context):
	context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm a Mr.Guti. Who are you?")
def help(update, context):
	update.message.reply_text(doc)
def ipinfo(update, context):
	# out = context.bot.send_message
	user_id = update.message.from_user.id
	ip = update.message.text.split(" ")[1]
	current_time = time()
	if user_id in user_last_message_time and current_time - user_last_message_time[user_id] < 3:
		update.message.reply_text("Please wait a few seconds before sending another request.")
	else:
		try:
			socket.inet_aton(ip)
			res = requests.get(f"https://api.ipdata.co/{ip}?api-key=38f41c58368c377cc05ea48410a83819efe36681a083a9e776d58119")
			data = (res.text).replace('"', "").replace("{", "").replace("}", "").replace("[", "").replace("]", "").replace(",", "")
			update.message.reply_text(text=data)
			user_last_message_time[user_id] = current_time
		except OSError:
			update.message.reply_text("Invalid IP")
def about(update, context):
	bio = """
Hello I am Mr. Guti, made by Master InferiorAK. I was his Experimental bot, but you can use me in your Purposes.

My Master's Links:
   Github   : https://github.com/InferiorAK
   Facebook : https://www.facebook.com/InferiorAK
   Messanger: https://m.me/InferiorAK
   Twitter  : https://www.twitter.com/@InferiorAK
   Youtube  : https://youtube.com/@InferiorAK
"""
	# update.message.reply_text(bio)
	context.bot.send_message(chat_id=update.effective_chat.id, text=bio+doc)



disp.add_handler(MessageHandler(~Filters.command, reply))
disp.add_handler(CommandHandler("start", start))
disp.add_handler(CommandHandler("help", help))
disp.add_handler(CommandHandler("ipinfo", ipinfo))
disp.add_handler(CommandHandler("about", about))
updater.start_polling()
updater.idle()
