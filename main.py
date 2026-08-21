import telebot

# استبدل YOUR_BOT_TOKEN بـ توكن البوت الخاص بك من BotFather
BOT_TOKEN = "YOUR_BOT_TOKEN"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك! البوت يعمل بنجاح.")

bot.infinity_polling()
