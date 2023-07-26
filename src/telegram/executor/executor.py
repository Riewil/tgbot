import configparser

config = configparser.ConfigParser()
config.read("E:/git/tgbot/src/resources/text.ini")

from telebot import types


class Executor:
    def __init__(self, bot):
        self.bot = bot

    def start(self, message):
        self.bot.send_message(message.chat.id, config.get("executor", "start"))

    def menu(self, message, markup):
        self.bot.send_message(message.chat.id, config.get("executor", "menu"),
                              reply_markup=markup)

    def menu_button(self):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('💤' + config.get("m_but", "btn1"))
        markup.add(btn1)
        return markup

    def zodiac_btn(self):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        zodiac_again = types.KeyboardButton(config.get("z_btn", "again"))
        menu = types.KeyboardButton(config.get("executor", "back_menu"))
        markup.add(zodiac_again, menu)
        return markup

    def zodiac(self, message, markup):
        self.bot.send_message(message.chat.id, config.get("zodiac", "zodiac"),
                              reply_markup=markup)

    def get_zodiac(self, message):
        try:
            day, month = message.text.split('.')
            zodiac_signs = {
                config.get("zz", "z1") + "♒️": [(20, 1), (18, 2)],
                config.get("zz", "z2") + "♓️": [(19, 2), (20, 3)],
                config.get("zz", "z3") + "♈️":  [(21, 3), (20, 4)],
                config.get("zz", "z4") + "♉️": [(21, 4), (20, 5)],
                config.get("zz", "z5") + "♊️": [(21, 5), (21, 6)],
                config.get("zz", "z6") + "♋️": [(22, 6), (22, 7)],
                config.get("zz", "z7") + "♌️": [(23, 7), (22, 8)],
                config.get("zz", "z8") + "♍️": [(23, 8), (22, 9)],
                config.get("zz", "z9") + "♎️": [(23, 9), (22, 10)],
                config.get("zz", "z10") + "♏️": [(23, 10), (21, 11)],
                config.get("zz", "z11") + "♐️": [(22, 11), (21, 12)],
                config.get("zz", "z12") + "♑️": [(22, 12), (19, 1)]

            }
            day, month = int(day), int(month)
            for sign, ((start_day, start_month), (end_day, end_month)) in zodiac_signs.items():
                if (day >= start_day and month == start_month) or (day <= end_day and month == end_month):
                    self.bot.send_message(message.chat.id, config.get("zodiac", "send_zodiac") + ' ' + sign)
                    break
            else:
                self.bot.send_message(message.chat.id, config.get("zodiac", "value_error"))

        except ValueError:
            self.bot.send_message(message.chat.id, config.get("zodiac", "value_error"))
