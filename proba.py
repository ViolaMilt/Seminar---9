'''from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler
import random


TOKEN = '5430361376:AAF5PNc74KH6Z5x6mt5mJbNk2A3MShYMbJA'
bot = Bot(token=TOKEN)
updater = Updater(token = TOKEN, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
  context.bot.send_message(update.effective_chat.id, "Привет!Напиши мне число: ")
  return "knopka_1"

def otvet(update, context):
   chislo = int(update.message.text)
   if 10 < chislo < 20:
    context.bot.send_message(update.effective_chat.id, "Принято!")
   return "knopka_2"

def poka(update, context):
    context.bot.send_message(update.effective_chat.id, "Пока!")
    return ConversationHandler.END

def cansel(update, context):
    return ConversationHandler.END


start_handler = CommandHandler('start', start)
first_handler = MessageHandler(Filters.text, otvet)
second_handler = MessageHandler(Filters.text, poka)
cansel_handler = CommandHandler('cansel', cansel)
conv_handler = ConversationHandler(entry_points=[start_handler],
                                          states={
                                              "knopka_1":[first_handler],
                                              "knopka_2":[second_handler],
                                          },
                                          fallbacks=[cansel_handler]
                                   )

dispatcher.add_handler(conv_handler)

updater.start_polling()
updater.idle()'''

# "Привет!Я - умный калькулятор.Я умею работать с комплексными числами.
# Напомню формулу комплексного числа: z = x + i y, где x, y – действительные числа,
# i − так называемая мнимая единица. Введи действительную часть первого числа: "

