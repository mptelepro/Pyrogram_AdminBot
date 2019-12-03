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
from commands import commands

@pyrogram.Client.on_message(pyrogram.Filters.command(["start"]))
async def start(bot, update):
TRChatBase(update.from_user.id, update.text, "/start")
inline_keyboard = [pyrogram.InlineKeyboardButton("📚 Commands", callback_data="commands"),
 pyrogram.InlineKeyboardButton("ℹ️ Info", url="https://t.me/keralasbots")]
reply_markup = pyrogram.InlineKeyboardMarkup(inline_keyboard)
await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id,
        reply_markup=reply_markup
    )

async def start_back(bot, update):
TRChatBase(update.from_user.id, update.text, "start")
ikeyboard = [pyrogram.InlineKeyboardButton("📚 Commands", callback_data="commands"),
 pyrogram.InlineKeyboardButton("ℹ️ Info", url="https://t.me/keralasbots")]
replymarkup = pyrogram.InlineKeyboardMarkup(ikeyboard)
await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id,
        reply_markup=replymarkup
    )
