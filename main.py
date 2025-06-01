from flask import Flask, request
from bot import bot
from config import WEBHOOK_URL

app = Flask(__name__)

@app.route(f"/{bot.token}", methods=['POST'])
def webhook():
    update = bot.types.Update.de_json(request.stream.read().decode("utf-8"))
    bot.process_new_updates([update])
    return "OK", 200

@app.route('/')
def index():
    return "Bot is running!", 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK_URL + "/" + bot.token)
    app.run(host="0.0.0.0", port=5000, debug=True)
