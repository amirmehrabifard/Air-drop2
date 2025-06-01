from telebot import TeleBot
from config import TOKEN
from handlers import setup_handlers

bot = TeleBot(TOKEN)
setup_handlers(bot)
