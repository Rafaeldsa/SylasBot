from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
import time
import sys
from conf.settings import TELEGRAM_TOKEN
#coding: utf-8

updater = Updater(token=TELEGRAM_TOKEN)
dispatcher = updater.dispatcher
def start(bot, update):
	response_message = "Salve"
	bot.send_message(
		chat_id=update.message.chat_id,
		text=response_message
)

def talk(bot, update):
	response_message = "Ola, meu nome eh Sylas, e o seu?"
	bot.send_message(
		chat_id=update.message.chat_id,
		text=response_message
	)
	time.sleep(10)
	bot.send_message(
		chat_id=update.message.chat_id,
		text="fuedasse"
	)

def unknow(bot, update):
    response_message = "EOQ?"
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
)	

starth = CommandHandler('start', start)
talkh = CommandHandler('talk', talk)
unkh = MessageHandler(Filters.command, unknow)

handlers = [starth, talkh, unkh]

for e in handlers:
	dispatcher.add_handler(e)

def main_loop():
	updater.start_polling()
	


if __name__ == '__main__':
	try:
		main_loop()
	except Exception as e:
		print (e)
		sys.exit(0)
	

