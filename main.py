import logging
import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# === ТВОЙ ТОКЕН БОТА ===
TELEGRAM_TOKEN = 'ВСТАВЬ_СЮДА_СВОЙ_ТОКЕН'

# === НАСТРОЙКА ПРОКСИ GPT ===
openai.api_key = 'free'  # или любое слово
openai.base_url = 'https://chatgpt.pawan.krd/v1/'  # прокси

logging.basicConfig(level=logging.INFO)

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Напиши мне сообщение — я отвечу с помощью GPT.")

# Обработка сообщений
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}]
        )
        reply = response.choices[0].message.content
    except Exception as e:
        reply = f"Произошла ошибка: {e}"

    await update.message.reply_text(reply)

if _name_ == '_main_':
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
