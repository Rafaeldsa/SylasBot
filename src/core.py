from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
import time
from conf.settings import TELEGRAM_TOKEN

def start(bot, update):
	i = 0
	while i < 2:
		
		response_message = "Salve"
		bot.send_message(
			chat_id=update.message.chat_id,
			text=response_message
			
		)
		time.sleep(120)
		i += 1
		

def main():
    updater = Updater(token=TELEGRAM_TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(
        CommandHandler('start', start)
)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    print("press CTRL + C to cancel.")
main()
