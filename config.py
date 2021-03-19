import os

class Config(object):
    # get a token from @BotFather
    TOKEN = os.environ.get("1357614130:AAEnVZv3qsS1LXDBUCACJPsOSvxJgiyBiz0", "")
    # The Telegram API things
    APP_ID = int(os.environ.get("1749924", 1749924))
    API_HASH = os.environ.get("87e4a056bb574f7939ac283b9a9187ab")
    # Get these values from my.telegram.org
    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("984441749", "").split())
    DB_URI = os.environ.get("postgres://eyofrnogltxmwz:9f85e8584199a374615a67bfe18f73edc4afaf9451d16eed3aee5b179708589b@ec2-54-243-195-160.compute-1.amazonaws.com:5432/d325npis91qikn", "")
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    log_chat = -1001367221700
    bot_name = "Search_All_Files_bot"
    netnum = "12"
