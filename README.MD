# XKCD В телеграм

Скрипт для отправки рандомных фотографий комиксов [XKCD](https://xkcd.com/)
### Как установить
Создайте .env файл, добавьте токен Телеграм бота и айди тг канала.
Пример:
```
    TG_BOT_API=[Токен бота]
    TG_CHAT_ID=[Id телеграм-канала, в который отправляются картинки]
```

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Как запустить

Запустите бота

```
python main.py
```
В указанный телеграм канал отправится картинка и описание к ней.

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).