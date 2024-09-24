import telebot
import os
from flask import Flask, request
from config.config import bot
from handlers.command_handlers import register_command_handlers
from handlers.callback_handlers import register_callback_handlers
from config.config import bot, TOKEN

WEBHOOK_URL = f''

app = Flask(__name__)

@app.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "¡Mensaje recibido!", 200

@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK_URL + TOKEN)
    return "¡Webhook configurado!", 200

# Main
if __name__ == "__main__":
      register_command_handlers(bot)
      register_callback_handlers(bot)
      app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))