import telebot
import openai
import os

TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

bot = telebot.TeleBot(TELEGRAM_TOKEN)
openai.api_key = OPENAI_API_KEY

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message.text}]
        )
        bot.send_message(message.chat.id, response['choices'][0]['message']['content'])
    except Exception as e:
        bot.send_message(message.chat.id, f"Ошибка: {str(e)}")

bot.polling()
