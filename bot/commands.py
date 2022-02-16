from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def hello(update: Update, context: CallbackContext):
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

def help(update: Update, context: CallbackContext):
    update.message.reply_text(f'hello, help, sum')

def sum(update: Update, context: CallbackContext):
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} + {y} = {x+y}')