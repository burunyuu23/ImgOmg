import requests

api_key = 'f18e1864a303d1fb63dae5620a4348cf'  # Замените на ваш реальный API Key

# Путь к файлу, который вы хотите загрузить
file_path = 'background.png'

# Открытие файла в бинарном режиме и чтение его содержимого
with open(file_path, 'rb') as file:
    # Создание POST-запроса с параметром 'key' и вашим API Key
    data = {'key': api_key}
    # Отправка POST-запроса на URL загрузки изображения с файлом в теле запроса
    response = requests.post('https://api.imgbb.com/1/upload', data=data, files={'image': file})

# Проверка статуса ответа и получение URL загруженного изображения
if response.status_code == 200:
    data = response.json()
    image_url = data['data']['url']
    print(f'Изображение загружено: {image_url}')
else:
    print('Произошла ошибка при загрузке изображения')