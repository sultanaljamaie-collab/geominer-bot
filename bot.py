import os
import random

from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters


TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [[KeyboardButton("📍 ارسال الموقع", request_location=True)]]

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    text = (
        "🛰️ مرحبا بك في GeoMiner AI\n\n"
        "أرسل موقعك ليتم تحليل المنطقة جيولوجياً."
    )

    await update.message.reply_text(text, reply_markup=reply_markup)


async def location(update: Update, context: ContextTypes.DEFAULT_TYPE):

    lat = update.message.location.latitude
    lon = update.message.location.longitude

    value = random.randint(1, 100)

    if value > 70:
        result = "🪨 احتمال معادن مرتفع"
    elif value > 40:
        result = "⛏ احتمال متوسط"
    else:
        result = "📍 احتمال ضعيف"

    text = f"""
📡 تقرير تحليل الموقع

📍 الإحداثيات:
{lat}
{lon}

🔎 النتيجة:
{result}

⚠️ التحليل تقديري وليس تأكيداً علمياً.
"""

    await update.message.reply_text(text)


def main():

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.LOCATION, location))

    print("Bot is running...")

    app.run_polling()


if __name__ == "__main__":
    main()
