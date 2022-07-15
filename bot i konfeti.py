import random
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler
import random


TOKEN = '5430361376:AAF5PNc74KH6Z5x6mt5mJbNk2A3MShYMbJA'
bot = Bot(token=TOKEN)
updater = Updater(token = TOKEN, use_context=True)
dispatcher = updater.dispatcher

global  konfeti
konfeti = 100
global  max
max = 28
global c
c = 0
global whogo
whogo=''
def start(update, context):
  context.bot.send_message(update.effective_chat.id, "Привет! Давай поиграем в игру.У нас 100 конфет."
                                                     "Берем по очереди, но не более 28 за ход.Ты первый!"
                                                     "Выигрывает тот,кто делает последний ход,забрав все конфеты: ")
  return "knopka_1"

def user_hod(update, context):
    global whogo
    whogo = 'user'
    print(whogo)
    chislo = int(update.message.text)
    global  konfeti
    konfeti = konfeti - chislo
    context.bot.send_message(update.effective_chat.id, f'{"Осталось ", konfeti,"конфет"}')
    print('я тут')
    proverka(update, context)

def hod_bota(update, context):
    global konfeti
    global whogo
    whogo = 'bot'
    print(whogo)
    b = random.randint(1, 10)
    if b % 2 == 0:
        c = konfeti % (max + 1)
    if b % 2 == 1:
        c = random.randint(1, 28)
    if konfeti <= 28:
        c = konfeti
    print(c)
    konfeti = konfeti - c
    context.bot.send_message(update.effective_chat.id, f'{"Бот взял ", c ,"конфет. "," Осталось", konfeti, "конфет"}')
    proverka(update, context)


def proverka(update, context):
  print(konfeti,' конфет провеяется')
  if konfeti >= 28:
      if whogo == 'bot':
          print(whogo,'проверка')
          return "knopka_1"
      if whogo == 'user':
          print(whogo, 'проверка')
          hod_bota(update, context)
  if 1 <= konfeti < 28:
      if whogo == 'bot':
        context.bot.send_message(update.effective_chat.id, "Вы выиграли! Для завершения игры введите команду /cancel ")
        return ConversationHandler.END
      if whogo == 'user':
        context.bot.send_message(update.effective_chat.id, "Вы проиграли!Для завершения игры введите команду /cancel ")
        return ConversationHandler.END

  if konfeti == 0:
     context.bot.send_message(update.effective_chat.id, "Вы проиграли! Для завершения игры введите команду /cancel ")
     return ConversationHandler.END
  if konfeti < 0:
     context.bot.send_message(update.effective_chat.id, "Конфет больше нет!Давайте играть заново=) ")
     return ConversationHandler.END

def cancel(update,context):
    return ConversationHandler.END


start_handler = CommandHandler('start', start)
first_handler = MessageHandler(Filters.text,user_hod)
second_handler = MessageHandler(Filters.text, hod_bota)
proverka_handler = MessageHandler(Filters.text, proverka)
cancel_handler = CommandHandler('cancel', cancel)
conv_handler = ConversationHandler(entry_points=[start_handler],
                                          states={
                                              "knopka_1":[first_handler],
                                              "knopka_2":[second_handler],
                                              "knopka_3":[proverka_handler],
                                          },
                                          fallbacks=[cancel_handler]
                                   )

dispatcher.add_handler(conv_handler)

updater.start_polling()
updater.idle()
