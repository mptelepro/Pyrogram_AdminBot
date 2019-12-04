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
logging.getLogger("pyrogram").setLevel(logging.WARNING)
from database import TRChatBase

from pyrogram import InlineKeyboardMarkup, InlineKeyboardButton

@pyrogram.Client.on_message(pyrogram.Filters.command(["start"]))
async def start(bot, update):
    # logger.info(update)
 reply = InlineKeyboardMarkup(
            [
                [  # First row
                    InlineKeyboardButton(  # Generates a callback query when pressed
                        "📚 Commands",
                        callback_data=b"commands"  # Note how callback_data must be bytes
                    ),
                    InlineKeyboardButton(  # Opens a web URL
                        "ℹ️ Info",
                        url="https://t.me/keralasbots"
                    )
                ]
            ]
        )

        await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT,
        reply_to_message_id=update.message_id,
        reply_markup=reply
    )

@pyrogram.Client.on_callback_query()
async def startback(bot, update):
    # logger.info(update)
 replyk = InlineKeyboardMarkup(
            [
                [  # First row
                    InlineKeyboardButton(  # Generates a callback query when pressed
                        "📚 Commands",
                        callback_data=b"commands"  # Note how callback_data must be bytes
                    ),
                    InlineKeyboardButton(  # Opens a web URL
                        "ℹ️ Info",
                        url="https://t.me/keralasbots"
                    )
                ]
            ]
        )

        await bot.edit_message_text(
        chat_id=update.chat.id,
        text=Translation.START_TEXT,
        reply_to_message_id=update.message_id,
        reply_markup=replyk
    )


@pyrogram.Client.on_callback_query(dynamic_data(b"commands"))
async def commands(bot, update):
home_string = "{}".format("startback")
      await bot.edit_message_text(
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
                        callback_data=home_string.encode("UTF-8")
                    )
                ]
            ]
        )
    )

