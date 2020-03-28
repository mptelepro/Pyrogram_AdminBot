#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Anand PS Kerala

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import asyncio

# the secret configuration specific things

from config import Config

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)


async def run(app):
    await app.start()
    await app.send_message(Config.log_chat, "**Bot started**\n\n"
                                        f"**Version:** 1.0 `[Beta]`")
    await app.idle()

plugins = dict(
    root="plugins"
)


app = pyrogram.Client(
    "JOkER",
    bot_token=Config.TOKEN,
    api_id=Config.APP_ID,
    api_hash=Config.API_HASH,
    plugins=plugins
)
    #app.run()

if __name__ == "__main__" :
    # create download directory, if not exist
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(app))
    
