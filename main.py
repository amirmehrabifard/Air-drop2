import os
import json
import telebot
from flask import Flask, request

# دریافت متغیرهای محیطی از Vercel
BOT_TOKEN = os.environ.get("BOT_TOKEN")
PRIVATE_KEY = os.environ.get("PRIVATE_KEY")
PORT = int(os.environ.get("PORT", 8000))

# بررسی مقدار توکن ربات
if not BOT_TOKEN:
    raise ValueError("❌ خطا: BOT_TOKEN در محیط تنظیم نشده است!")

# تنظیم Flask
app = Flask(__name__)
bot = telebot.TeleBot(BOT_TOKEN)

# مسیر تست برای بررسی اجرای صحیح
@app.route("/", methods=["GET"])
def home():
    return "✅ Bot is running on Vercel!"

# مسیر اصلی برای دریافت آپدیت‌های تلگرام
@app.route("/webhook", methods=["POST"])
def webhook():
    """ دریافت پیام‌های ورودی از تلگرام و پردازش آنها. """
    json_data = request.get_json()
    if json_data:
        bot.process_new_updates([telebot.types.Update.de_json(json_data)])
    return "OK", 200

# تنظیم دستورات ربات
@bot.message_handler(commands=["start"])
def send_welcome(message):
    """ پاسخ به دستور /start با پیام خوش‌آمدگویی. """
    bot.reply_to(message, "🚀 خوش آمدید! ربات شما در حال اجرا است.")

# اجرای برنامه روی پورت صحیح
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
