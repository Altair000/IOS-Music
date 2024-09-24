import requests
from config.config import DIAWI

# Función para subir el archivo a Diawi
def upload_to_diawi(file_path):
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
    req = requests.post(url_1, data=data, files=files)
    
    if req.status_code == 200:
        j = req.json()
        if j:
            return j['job']
        else:
            print("Error en la subida:", result)
            return None
    else:
        print("Error al contactar Diawi:", req.status_code)
        return None
        
    url = 'https://upload.diawi.com/status'
    
    payload = {
        'token': os.getenv('Diawi'),
        'job': job
        }
    
    response = requests.post(url=url, data=payload)
    
    if response.status_code == 200:
        link = response.json()
        if link['message'] == 'OK':
            return link['link']
        else:
            print('Error en la Subida, result')
    else:
        print('Error al contactar Diawi:', response.status_code)
    
    
    
