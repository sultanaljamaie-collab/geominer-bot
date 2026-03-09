import os
import random
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [[KeyboardButton("📍 ارسال الموقع", request_location=True)]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "🛰️ مرحبا بك في GeoMiner AI\n\nارسل موقعك ليتم تحليل المنطقة جيولوجيا.",
        reply_markup=reply_markup
    )

def analyze(lat, lon):

    value = random.randint(1,100)

    if value > 70:
        return "🪨 احتمال معادن مرتفع"
    elif value > 40:
        return "⛏ احتمال متوسط"
    else:
        return "📍 احتمال ضعيف"

async def location(update: Update, context: ContextTypes.DEFAULT_TYPE):

    lat = update.message.location.latitude
    lon = update.message.location.longitude

    result = analyze(lat, lon)

    text = f"""
📡 تقرير تحليل الموقع

الإحداثيات:
{lat}
{lon}

النتيجة:
{result}

⚠️ التحليل تقديري اعتمادًا على البيانات المتاحة
"""

    await update.message.reply_text(text)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.LOCATION, location))

app.run_polling()
