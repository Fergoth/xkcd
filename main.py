import requests
import argparse
import os
from random import randint
from time import sleep

import telegram

from dotenv import load_dotenv


def get_comics(id):
    url = f"https://xkcd.com/{id}/info.0.json"
    response = requests.get(url)
    response.raise_for_status()
    decoded_response = response.json()
    if "error" in decoded_response:
        raise requests.exceptions.HTTPError(decoded_response["error"])
    return decoded_response


def get_amount_of_comics():
    url = "https://xkcd.com/info.0.json"
    response = requests.get(url)
    response.raise_for_status()
    decoded_response = response.json()
    if "error" in decoded_response:
        raise requests.exceptions.HTTPError(decoded_response["error"])
    return decoded_response["num"]


if __name__ == "__main__":
    load_dotenv()
    chat_id = os.environ["TG_CHAT_ID"]
    token = os.environ["TG_BOT_API"]
    bot = telegram.Bot(token=token)
    amount_of_comics = get_amount_of_comics()
    comics_id = randint(1, amount_of_comics)
    try:
        comics = get_comics(comics_id)
    except requests.HTTPError as error:
        print("Некорректный ответ от сервера", error)
    image_url, comment = comics["img"], comics["alt"]
    bot.send_message(chat_id=chat_id, text=comment)
    bot.send_photo(chat_id=chat_id, photo=requests.get(image_url).content)
