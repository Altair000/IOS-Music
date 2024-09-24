from telebot import types, TeleBot
from config.config import bot
from handlers.command_handlers import start

@bot.callback_query_handler(func=lambda call: True)
def info(call):
    if call.data == "info":
        markup = types.InlineKeyboardMarkup()
        back_button = types.InlineKeyboardButton("Back", callback_data="atras")
        markup.add(back_button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Este bot te ayuda a instalar aplicaciones '.ipa'. Envía la aplicación que deseas instalar. Aviso: Las aplicaciones tienen una duracion de 3 dias luego de esto necesita volver a instalarlas, esto debido al consumo monetario de la pagina de hosting que utiliza el bot, les recomiendo instalar ADGuardVPN, esta les permitira instalar aplicaciones desde la appstore, Saludos",
                              reply_markup=markup)
    elif call.data == "atras":
        bot.edit_message_text(start(call.message))
        
def register_callback_handlers(bot: TeleBot):
    bot.register_callback_query_handler(info, func=lambda call: call.data == 'info')
