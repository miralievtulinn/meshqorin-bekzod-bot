import os
import telebot
from telebot import types

TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)


SAVOL_JAVOBLAR = {
    "📍 Manzilimiz": "Bizning manzil: Toshkent shahri, Chilonzor tumani, 1-mavze.",
    "💰 Narxlar": "Xizmatlarimiz narxi 100 000 so'mdan boshlanadi.",
    "⏰ Ish vaqti": "Dushanbadan Shanbagacha, soat 09:00 dan 18:00 gacha ishlaymiz.",
    "📞 Aloqa": "Murojaat uchun telefon: +998 90 123 45 67"
}


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    tugmalar = [types.KeyboardButton(savol) for savol in SAVOL_JAVOBLAR.keys()]
    markup.add(*tugmalar)
    
    bot.send_message(
        message.chat.id, 
        "Assalomu alaykum! Quyidagi savollardan birini tanlang:", 
        reply_markup=markup
    )

@bot.message_handler(func=lambda message: True)
def javob_berish(message):
    matn = message.text
    if matn in SAVOL_JAVOBLAR:
        bot.send_message(message.chat.id, SAVOL_JAVOBLAR[matn])
    else:
        bot.send_message(message.chat.id, "Iltimos, pastdagi tugmalardan birini tanlang.")

bot.polling(none_stop=True)
