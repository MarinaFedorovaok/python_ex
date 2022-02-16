from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import commands as c



updater = Updater('5194267730:AAGkpss1bUcufm7GHyfG5yARclQskKXu938')
print("Server starts")
updater.dispatcher.add_handler(CommandHandler('hello', c.hello))
updater.dispatcher.add_handler(CommandHandler('help', c.help))
updater.dispatcher.add_handler(CommandHandler('sum', c.sum))


updater.start_polling()
updater.idle()