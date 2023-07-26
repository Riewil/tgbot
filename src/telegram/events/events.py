import configparser

from src.telegram.executor.executor import Executor

config = configparser.ConfigParser()
config.read("E:/git/tgbot/src/resources/text.ini")


class Events:
    def __init__(self, bot):
        self.bot = bot
        self.executor = Executor(bot)

    def start_listener(self):
        tg_bot = self.bot

        @tg_bot.message_handler(commands=['start'])
        def start(message):
            self.executor.start(message)

        @tg_bot.message_handler(commands=['menu'])
        @tg_bot.message_handler(func=lambda message: message.text == config.get("executor", "back_menu"))
        def menu(message):
            markup = self.executor.menu_button()
            self.executor.menu(message, markup)

        @tg_bot.message_handler(func=lambda message: message.text == '💤Zodiac' or config.get("z_btn", "again"))
        def zodiac(message):
            markup = self.executor.zodiac_btn()
            self.executor.zodiac(message, markup)
            tg_bot.register_next_step_handler(message, self.executor.get_zodiac)

        tg_bot.polling(none_stop=True)
