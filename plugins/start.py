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
from pyrogram import Client, Filters, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from database import TRChatBase
from sql.sql import *
from pyrogram import MessageHandler
from concurrent.futures import Future
import asyncio

class AwaitableFuture(Future):
    def __await__(self):
        return (yield from asyncio.wrap_future(self))

class Conversation:
    def __init__(self, client: Client, peer):
        self.peer = peer
        self.client = client
        self.handlers = []
        self.msgs = []
        self.message_handler = MessageHandler(self.handle_message, Filters.chat(self.peer))
        self.last_sent_id = 0
    def handle_message(self, _, message):
        if not self.check(message):
            self.msgs.append(message)
        message.stop_propagation()
    def add_awaiter(self, filters):
        fut = AwaitableFuture()
        self.handlers.append((filters, fut))
        return fut
    def check(self,message):
        for filters, fut in self.handlers:
            if fut.cancelled():
                self.handlers.remove((filters, fut))
            elif filters(message):
                self.handlers.remove((filters, fut))
                fut.set_result(message)
                return True
        return False
    def send_message(self, *args, **kwargs):
        msg = self.client.send_message(self.peer, *args, **kwargs)
        self.last_sent_id = msg.message_id
        return msg
    def get_response(self, filters=Filters.text):
        for msg in self.msgs:
            if msg.message_id < self.last_sent_id:
                self.msgs.remove(msg)
            elif filters(msg):
                fut = AwaitableFuture()
                fut.set_result(msg)
                self.msgs.remove(msg)
                return fut
        return self.add_awaiter(filters)
    async def __aenter__(self):
        return self.__enter__()
    def __enter__(self):
        self.client.add_handler(self.message_handler, -1)
        return self
    async def __aexit__(self):
        self.__exit__()
    def __exit__(self, *args):
        self.client.remove_handler(self.message_handler, -1)

class AwaitableClient(Client):
    def conversation(self, peer):
        return Conversation(self, peer)
    
    
token = Config.TOKEN
#client = AwaitableClient('await_bot', bot_token=token, api_id=Config.APP_ID, api_hash=Config.API_HASH)

@Client.on_message(Filters.command('sync'))
def _test(_, msg):
    with AwaitableClient.conversation(msg.chat.id) as conv:
        conv.send_message('I am (sync) waiting for your reply!')
        response = conv.get_response(Filters.text).result()
        response.reply('You said: ' + response.text)

run_async = lambda func: lambda *args: asyncio.run(func(*args))

@Client.on_message(Filters.command('async'))
@run_async
async def _test(_, msg):
    with AwaitableClient.conversation(msg.chat.id) as conv:
        conv.send_message('I am awaiting your reply!')
        response = await conv.get_response(Filters.text)
        response.reply('You said: ' + response.text)

#client.run()

STARTKEY = [[InlineKeyboardButton("📚 Commands", callback_data="commands"), InlineKeyboardButton("ℹ️ Info", url="https://t.me/keralasbots")]]
STARTKEY += [[InlineKeyboardButton("★ Jinja", callback_data="jinja")]]
BACKKEY = [[InlineKeyboardButton("🔙 Back", callback_data="start_back")]]

@pyrogram.Client.on_message(pyrogram.Filters.command(["start"]))
async def start(bot, update):
    await bot.send_message(chat_id=update.chat.id, text=Translation.START, parse_mode="html", disable_web_page_preview=True, reply_to_message_id=update.message_id, reply_markup=InlineKeyboardMarkup(STARTKEY))

@pyrogram.Client.on_callback_query(pyrogram.Filters.callback_data("start_back"))
async def start_back(bot, update):
    await bot.edit_message_text(chat_id=update.message.chat.id, text=Translation.START, parse_mode="html", disable_web_page_preview=True, message_id=update.message.message_id, reply_markup=InlineKeyboardMarkup(STARTKEY))


@pyrogram.Client.on_callback_query(pyrogram.Filters.callback_data("commands"))
async def commands(bot, update):
    await bot.edit_message_text(chat_id=update.message.chat.id, text=Translation.COMMAND, parse_mode="html", disable_web_page_preview=True, message_id=update.message.message_id, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("👤Private Commands", url="https://t.me/keralasbots"), InlineKeyboardButton("👷 Admin Commands", url="https://docs.pyrogram.org"),], [InlineKeyboardButton("🔙 Back", callback_data="start_back")]]))

@Client.on_callback_query(Filters.callback_data("jinja"))
async def jinja(bot, update):
    jin = [[InlineKeyboardButton("★ Set Jinja", callback_data="setjinja")]]
    jin += BACKKEY
    jinjamark = InlineKeyboardMarkup(jin)
    view = vjinja(update.from_user.id)
    if view == None:
        jinja = "None"
    else:
        jinja = str(view)
    await bot.edit_message_text(chat_id=update.message.chat.id, text=jinja, message_id=update.message.message_id, reply_markup=jinjamark)

@Client.on_callback_query(Filters.callback_data("setjinja"))
async def setjinja(bot, update):
    back = InlineKeyboardButton(BACKKEY)
    with AwaitableClient.conversation(update.chat.id) as conv:
        await conv.send_message(chat_id=update.message.chat.id, text="Now send me the jinja", reply_markup=back)
        response = await conv.get_response(Filters.text)
        jinja(update.from_user.id, response.text)
        response.reply("Successfully set jinja")

    
