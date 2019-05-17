from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
import time
from conf.settings import TELEGRAM_TOKEN
#coding: utf-8
def start(bot, update):
	response_message = "Salve"
	bot.send_message(
		chat_id=update.message.chat_id,
		text=response_message
)

def talk(bot, update, args):
	response_message = "Ola, meu nome eh Sylas, e o seu?"
	bot.send_message(
		chat_id=update.message.chat_id,
		text=response_message + agrs[0]
	)
		

def main():
	updater = Updater(token=TELEGRAM_TOKEN)
	dispatcher = updater.dispatcher
	dispatcher.add_handler(
		CommandHandler('start', start)
	)
	dispatcher.add_handler(
		CommandHandler('talk',talk)
	)
	updater.start_polling()
	updater.idle()


if __name__ == '__main__':
    print("No ar...")
main()
