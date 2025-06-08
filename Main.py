import telebot
import os

# Use o token da variável de ambiente (iremos configurar no Replit)
TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🤖 Olá! Eu sou o bot de sinais Bac Bo.\nAguarde o próximo sinal.")

bot.infinity_polling()
