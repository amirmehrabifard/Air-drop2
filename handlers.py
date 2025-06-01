from telebot.types import Message
from app.storage import register_user, record_invite
from app.blockchain import send_tokens

def setup_handlers(bot):
    @bot.message_handler(commands=['start'])
    def welcome_user(message: Message):
        user_id = message.chat.id
        args = message.text.split()
        
        if len(args) > 1:  # بررسی ورود با لینک دعوت
            inviter_id = args[1]
            if inviter_id.isdigit():
                record_invite(inviter_id, user_id)
                bot.send_message(inviter_id, "یک دعوت موفق انجام شد، شما ۱۰۰ توکن دریافت کردید!")

        bot.send_message(user_id, "به کانال Benjamin Franklin Token خوش آمدید، ۵۰۰ توکن دریافت کردید!")
        register_user(user_id, message.chat.username)
        send_tokens(user_id, 500)

    @bot.message_handler(commands=['invite'])
    def invite_user(message: Message):
        inviter_id = message.chat.id
        invite_link = f"https://t.me/your_bot?start={inviter_id}"
        bot.send_message(inviter_id, f"Your invite link: {invite_link}")
