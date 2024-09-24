import os, telebot, time
from tqdm import tqdm

TOKEN = os.getenv('Token')
bot = telebot.TeleBot(TOKEN)
DIAWI = os.getenv('Diawi')

def progress_bar(total):
    for i in tqdm(range(total), desc="Progreso", unit="item"):
        time.sleep(0.1)  # Simula un trabajo que toma tiempo
