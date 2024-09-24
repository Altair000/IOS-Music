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
    
    # Subir el archivo a Diawi
    req = requests.post(url_1, data=data, files=files)
    
    if req.status_code == 200:
        j = req.json()
        if 'job' in j:
            job = j['job']
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
    while True:
        response = requests.post(url=url_status, data=payload)
        
        if response.status_code == 200:
            link_info = response.json()
            if link_info['status'] == 2000:  # El archivo está listo para descargar
                return link_info['link']
            elif link_info['status'] in [4000, 4001]:  # Errores de Diawi
                print('Error en la subida:', link_info['message'])
                return None
            else:
                # Estado aún no completado, seguir esperando
                time.sleep(5)  # Espera 5 segundos antes de volver a consultar
        else:
            print('Error al contactar Diawi:', response.status_code)
            return None