# Pyrogram_Adminbot

Bot developed by [Kerala Developer Team](https://t.me/keralasbots) for better administration.
Heavily inspired by [@EduuRobot](https://t.me/EduuRobot).

But it is not yet completed 😢

## Installation

Change the values according to you:

```


class Config(object):
    # get a token from @BotFather
    TOKEN = os.environ.get("BOT_TOKEN", "")
    # The Telegram API things
    APP_ID = int(os.environ.get("ID", 12345))
    API_HASH = os.environ.get("HASH")
    # Get these values from my.telegram.org
    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())
    DB_URI = os.environ.get("DATABASE_URL", "")
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    log_chat = -1001296501406
    bot_name = "Edu_jokerbot"


```

## Contributions

Contributions are always welcome. 

With <b>[💖 Kerala Developer Team](https://t.me/Keralasbots)</b>

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/mptelepro/Youtube-Downloader-Bot/tree/master)
