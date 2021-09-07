"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging, ephem, datetime, settings

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import datetime

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')



def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def planets_info(update, context):
    planet_comm = update.message.text
    planet_name = planet_comm.split()[1]
    
    date_today = datetime.today().strftime('%d/%m/%Y')

    if planet_name == 'Mars':
        planet = ephem.Mars(date_today)

    elif planet_name == 'Mercury':
        planet = ephem.Mercury(date_today)
    
    elif planet_name == 'Venus':
        planet = ephem.Venus(date_today)
    
    elif planet_name == 'Jupiter':
        planet = ephem.Jupiter(date_today)
    
    elif planet_name == 'Saturn':
        planet = ephem.Saturn(date_today)
    
    elif planet_name == 'Uranus':
        planet = ephem.Uranus(date_today)

    elif planet_name == 'Neptune':
        planet = ephem.Neptune(date_today)
    
    else:
        update.message.reply_text(f'Ne znayu {planet_name}, ne trogai menya')
        return

    const_planet = ephem.constellation(planet)[1]
    update.message.reply_text(const_planet)    


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planets_info))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
