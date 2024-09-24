import os, telebot, time

TOKEN = os.getenv('Token')
bot = telebot.TeleBot(TOKEN)
DIAWI = os.getenv('Diawi')

def progress_bar(message.chat.id, bot):
    total_steps = 10
    msg = bot.send_message(chat_id, "Progreso: 0%")
    
    for i in range(total_steps):
        time.sleep(0.5)  # Simula el tiempo que tarda el proceso
        bot.edit_message_text(chat_id=chat_id, message_id=msg.message_id, 
                              text=f"Progreso: {int((i + 1) / total_steps * 100)}%")
    
    bot.edit_message_text(chat_id=chat_id, message_id=msg.message_id, 
                          text="Proceso completado.")