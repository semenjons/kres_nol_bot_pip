#Командный модуль

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler
from active import *
import klava as kl


app = ApplicationBuilder().token("5844437623:AAE-FNmAQ01lSSM5KW-bXmxlpEmEfNnFYOk").build()
app.add_handler(CommandHandler('start', newGame))
app.add_handler(CommandHandler('hello', hello_comand ))
app.add_handler(CommandHandler('help', help_command))

print('сервер запусился')
app.run_polling()  
