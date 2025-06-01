from telebot import TeleBot
from app.config import TOKEN
from app.handlers import setup_handlers

bot = TeleBot(TOKEN)
setup_handlers(bot)
