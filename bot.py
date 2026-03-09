from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import random
import os

TOKEN = os.getenv("BOT_TOKEN")

# رسالة البداية
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [[KeyboardButton("📍 ارسال الموقع", request_location=True)]]

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "🛰️ مرحبا بك في GeoMiner AI\n\n"
        "ارسل موقعك ليتم تحليل المنطقة جيولوجيا.",
        reply_markup=reply_markup
    )

# تحليل الموقع
def analyze(lat, lon):

    value = random.randint(1,100)

    if value > 70:
        return "🪨 احتمال معادن مرتفع"
    elif value > 40:
        return "⛏ احتمال متوسط"
    else:
        return "📍 احتمال ضعيف"

# استقبال الموقع
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

⚠️ التحليل تقديري اعتمادا على البيانات المتاحة.
"""

    await update.message.reply_text(text)

# تشغيل البوت
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.LOCATION, location))

app.run_polling()
