# -- coding: utf-8 -

import logging

import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update: telegram.Update, context: CallbackContext):
    update.message.reply_text(
        'Привет! Я бот АМУ при МГК им. П.И. Чайковского!'
        'Я могу попробвать ответить на ваш вопрос,'
        'или попробуйте зайти в menu, набрав комманду /menu'
    )

def menu(update: telegram.Update, context: CallbackContext):
    update.message.reply_text(
        '/service_journal - поддержка по внутреннему журналу \r\n'
        '/help_abiturient - поддержка абитуриента\r\n'
        '/show_my_rights  - показать мои права\r\n'
    )


def echo(update: telegram.Update, context: CallbackContext):
    txt = update.message.text

    update.message.reply_text('Эхо заглушка текст: ' + txt)

updater = Updater("1919840721:AAGqTwCKaV_WsQRAKp8etFnWG-EClFyKDK8", use_context=True)
dispatcher = updater.dispatcher

# on different commands - answer in Telegram
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("menu", menu))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

# Start the Bot
updater.start_polling()
updater.idle()
