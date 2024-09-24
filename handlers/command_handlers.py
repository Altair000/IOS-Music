import os, telebot
from telebot import types, TeleBot
from config.config import bot, progress_bar
from config.sign import upload_to_diawi

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    info_button = types.InlineKeyboardButton("Info", callback_data="info")
    owner_button = types.InlineKeyboardButton("Owner", url="https://t.me/alltallr")
    markup.add(info_button, owner_button)
    bot.send_message(message.chat.id, "¡Bienvenido! Selecciona una opción:", reply_markup=markup)
   
@bot.message_handler(content_types=['document'])
def document(message):
    # Verifica si el archivo es un .ipa
    if message.document.file_name.endswith('.ipa'):
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        
        # Guardar temporalmente el archivo
        file_name = message.document.file_name
        with open(file_name, 'wb') as new_file:
            new_file.write(downloaded_file)
        
        # Llamar a la función con el número total de pasos
        progress_bar(100)
        bot.send_message(message.chat.id, "1")
        # Subir el archivo a Diawi
        install_link = upload_to_diawi(file_name)
        bot.send_message(message.chat.id, "2")
        if install_link:
            markup = telebot.types.InlineKeyboardMarkup()
            bot.send_message(message.chat.id, "3")
            install_button = telebot.types.InlineKeyboardButton("Instalar App", url=install_link)
            bot.send_message(message.chat.id, "4")
            markup.add(install_button)
            bot.send_message(message.chat.id, "5")
            bot.send_message(message.chat.id, "Tu aplicación está lista para instalar. Password:(1234):", reply_markup=markup)
           bot.send_message(message.chat.id, "6")
      
        # Eliminar el archivo temporal
        os.remove(file_name)
    else:
        bot.send_message(message.chat.id, "Por favor, envía un archivo .ipa válido.")

def register_command_handlers(bot: TeleBot):
    bot.register_message_handler(start, commands=['start'])
    bot.register_message_handler(document, content_types=['document'])
