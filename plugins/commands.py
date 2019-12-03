#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Anand PS Kerala

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3

from config import Config
from translation import Translation

import pyrogram
from database import TRChatBase
from start import start_back


@pyrogram.Client.on_callback_query()
async def commands(bot, update):
TRChatBase(update.from_user.id, update.text, "/commands")
inlinekeyboard = [pyrogram.InlineKeyboardButton("🕵️ Private Commands", url="t.me/keralasbots"),
 pyrogram.InlineKeyboardButton("👷 Admin Commands", url="t.me/keralasbots")
inlinekeyboard.append(pyrogram.InlineKeyboardButton("🔙 Back", callback_data="start_back"))
replycmarkup = pyrogram.InlineKeyboardMarkup(inlinekeyboard)
await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.COMMAND,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id,
        reply_markup=replycmarkup
    )
