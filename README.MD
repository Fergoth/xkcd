# XKCD В телеграм

Скрипт для отправки рандомных фотографий комиксов [XKCD](https://xkcd.com/)
### Как установить
Создайте .env файл, добавьте токен Телеграм бота, айди тг канала и изначальное время для отправки картинок.
Пример:
```
    TG_BOT_API=[Токен бота]
    POST_FREQ=[Частота отправления фотографий в секундах]
    TG_CHAT_ID=[Id телеграм-канала, в который отправляются картинки]
```

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Как запустить

Запустите бота
    Позиционный необязательный аргумент:
   * freq частота отправки комиксов
   * По умолчанию значение для частоты берется из env,

     ```
         python main.py  100 
     ```


### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).