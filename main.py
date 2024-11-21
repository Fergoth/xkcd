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
    freq = int(os.environ["POST_FREQ"])
    chat_id = os.environ["TG_CHAT_ID"]
    parser = argparse.ArgumentParser(description="Скрипт для публикации фотографий XKCD")
    parser.add_argument(
        "freq", nargs="?", type=int, default=freq, help="частота публикации"
    )
    args = parser.parse_args()
    token = os.environ["TG_BOT_API"]
    bot = telegram.Bot(token=token)
    amount_of_comics = get_amount_of_comics()
    while True:
        id = randint(1, amount_of_comics)
        try:
            comics = get_comics(id)
        except requests.HTTPError as error:
            print("Некорректный ответ от сервера", error)
        image_url, comment = comics["img"], comics["alt"]
        bot.send_message(chat_id=chat_id, text=comment)
        bot.send_photo(chat_id=chat_id, document=requests.get(image_url).content)
        sleep(args.freq)
