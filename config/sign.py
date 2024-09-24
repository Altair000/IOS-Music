import requests
from config.config import DIAWI

# Función para subir el archivo a Diawi
def upload_to_diawi(file_path):
    url = 'https://upload.diawi.com/'
    data = {
        'token': DIAWI,
        'wall_of_apps': 'false',  # Opciones de configuración de Diawi
        'password': '1234',           # Puedes agregar una contraseña si es necesario
        'comment': 'No olvides hacer tu pequeña donacion, esto me ayudara a mejorar este y nuevos proyectos para la comunidad.'
    }
    files = {
        'file': open(file_path, 'rb')
    }
    response = requests.post(url, data=data, files=files)
    
    if response.status_code == 200:
        result = response.json()
        if result['status'] == 'ok':
            return result['link']
        else:
            print("Error en la subida:", result)
            return None
    else:
        print("Error al contactar Diawi:", response.status_code)
        return None
