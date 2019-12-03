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
from pyrogram import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from database import TRChatBase
from start import start_back


@pyrogram.Client.on_callback_query()
async def commands(bot, update):
await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.COMMAND,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id,
        reply_markup=InlineKeyboardMarkup(
            [
                [  # First row
                    InlineKeyboardButton(  # Generates a callback query when pressed
                        "🕵️ Private Commands",
                        url="https://t.me/keralasbots"  # Note how callback_data must be bytes
                    ),
                    InlineKeyboardButton(  # Opens a web URL
                        "👷 Admin Commands",
                        url="https://docs.pyrogram.org"
                    ),
                ],
                [  # Second row
                    InlineKeyboardButton(  # Opens the inline interface
                        "🔙 Back",
                        callback_data=b"start_back"
                    )
                ]
            ]
        )
    )
