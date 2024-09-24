import requests
from config.config import DIAWI

# Función para subir el archivo a Diawi
def upload_to_diawi(file_path, bot, chat_id):
    url_1 = 'https://upload.diawi.com/'
    data = {
        'token': DIAWI,
        'wall_of_apps': 'false',  # Opciones de configuración de Diawi
        'password': '1234',           # Puedes agregar una contraseña si es necesario
        'comment': 'No olvides hacer tu pequeña donacion, esto me ayudara a mejorar este y nuevos proyectos para la comunidad.'
    }
    files = {
        'file': open(file_path, 'rb')
    }
    
    # Subir el archivo a Diawi
    req = requests.post(url_1, data=data, files=files)
    
    if req.status_code == 200:
        j = req.json()
        if 'job' in j:
            job = j['job']
            print(job)
        else:
            print("Error en la subida:", j)
            return None
    else:
        print("Error al contactar Diawi:", req.status_code)
        return None

    # Comprobar el estado de la subida y obtener el enlace de instalación
    url_status = 'https://upload.diawi.com/status'
    
    payload = {
        'token': DIAWI,
        'job': job
    }

    # Revisar el estado periódicamente hasta obtener el enlace
    attempts = 0
    max_attempts = 10  # Número máximo de intentos para verificar el estado
    print("sign")
    # Envía un mensaje inicial al usuario
    bot.send_message(chat_id, "Tu aplicación se está procesando, por favor espera...")
    print("sign")
    while attempts < max_attempts:
        response = requests.get(url=url_status, data=payload)
        print(response.text)
        if response.status_code == 200:
            print("sign")
            link_info = response.json()
            print(link_info)
            if link_info['status'] == 2000:  # Archivo listo para descargar
                return link_info['link']
            elif link_info['status'] == 2001:  # Procesando
                if attempts % 3 == 0:  # Envía un mensaje cada 3 intentos
                    bot.send_message(chat_id, "Aún estamos esperando a que tu aplicación sea procesada...")
                time.sleep(5)  # Espera antes de volver a consultar
            elif link_info['status'] in [4000, 4001]:  # Errores de Diawi
                bot.send_message(chat_id, 'Error en la subida: {}'.format(link_info['message']))
                return None
        else:
            bot.send_message(chat_id, 'Error al contactar Diawi: {}'.format(response.status_code))
            return None
    
        attempts += 1  # Incrementar el contador de intentos

        # Si se alcanzó el máximo de intentos
        bot.send_message(chat_id, "No se pudo obtener el enlace después de varios intentos.")
        return None  # O un mensaje de error

    
    
    