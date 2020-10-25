#!/usr/bin/env python3

import json
from pprint import pprint

import requests
import random
from io import BytesIO

TOKEN = '' # Мой токен
URL = 'https://api.vk.com/method/messages.send?&v=5.52' # Урл на метод отправки сообщения через АПИ
USER_ID = 327708634 # Кому
PEER_ID = 327708634 # От кого
RANDOM_ID = random.randint(10000000, 1000000000) # Рандомное значение для уникального сообщения


def random_message_generate():

    GOOD_MORNING = ['Доброе', 'Чудесное', 'Потрясающее', 'Прекрасное', 'Волшебное', 'Сказочное', 'Шоколадное',
                    'Солнечное']

    ADJECTIVE = ['Сладкая', 'Нежная', ' Изумрудная', 'Вишнёвая', 'Спелая', 'Космическая', 'Пушистая', 'Волшебная',
                 'Тёплая', 'Мягкая', 'Розовая', 'Невероятная', 'Морская', 'Любимая', 'Сахарная', 'Карамельная',
                 'Ласковая', 'Приятная', 'Чудесная', 'Потрясающая', 'Сказочная', 'Солнечная', 'Звёздная',
                 'Удивительная', 'Супер-пупер', 'Бархатная', 'Красивая', 'Самая лучшая', 'Самая-самая', 'Вкусная',
                 'Бесконечная']

    NOUN = ['Звёздочка', 'Карамелька', 'Солнышко', 'Изюминка', 'Вишенка', 'Ангелочек', 'Сахара кусочек', 'Персик',
            'Весна', 'Муза', 'Принцесса', 'Царевна', 'Изумрудинка', 'Мякиш', 'Море', 'Чудо', 'Цветочек', 'Конфетка',
            'Шоколадка', 'Облачко', 'Сердечко', 'Киса', 'Тигрица', 'Кошечка']

    HEART = ['🧡', '❤', '💜', '💛', '💚', '💙', '💖', '💗', '💞', '💘', '💝', '💓']

    final_message = f"{random.choice(GOOD_MORNING)} утро, моя " \
                    f"{random.choice(ADJECTIVE)} {random.choice(NOUN)} {random.choice(HEART)}"
    return final_message

def sender():

    message = random_message_generate()
    attachment = photo_to_vk()
    response = requests.get(URL, params={'access_token': TOKEN,
                                         'peer_id': PEER_ID,
                                         'user_id': USER_ID,
                                         'random_id': RANDOM_ID,
                                         'message': message,
                                         'attachment': attachment
                                         })
    json_response = json.loads(response.text)


def random_cat():
    response = requests.get('https://cataas.com/cat')
    norm_image = BytesIO(response.content)
    norm_image.seek(0)
    return norm_image

def photo_to_vk():
    image = random_cat()
    URL = 'https://api.vk.com/method/photos.getMessagesUploadServer?&v=5.52'
    response = requests.get(URL, params={'access_token': TOKEN})
    json_response = json.loads(response.text)

    upload_url = json_response['response']['upload_url']
    upload_data = requests.post(url=upload_url, files={'photo': ('image.png', image, 'image/png')}).json()

    server = upload_data['server']
    photo = upload_data['photo']
    hash = upload_data['hash']

    image_data = requests.get(f"https://api.vk.com/method/photos.saveMessagesPhoto?&v=5.52",
                              params={'access_token': TOKEN,
                                      'server': server,
                                      'photo': photo,
                                      'hash': hash})
    json_image_data = json.loads(image_data.text)

    if json_image_data:
        attachment = f'photo{PEER_ID}_{json_image_data["response"][0]["id"]}'
        return attachment
    else:
        return ''

if __name__ == '__main__':
    sender()
