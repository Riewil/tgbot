import configparser

import telebot

from src.telegram.events.events import Events

config = configparser.ConfigParser()
config.read("E:/git/tgbot/src/resources/text.ini")
TOKEN = config.get("KEY", "token")


def main():
    bot = telebot.TeleBot(TOKEN)
    events = Events(bot)
    events.start_listener()


if __name__ == '__main__':
    main()
