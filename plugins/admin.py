import pyrogram
import time
from config import Config
from pyrogram.errors import RPCError
from pyrogram import ChatPermissions

from util import *

@pyrogram.Client.on_message(pyrogram.Filters.command(["setitle", "setitle@edu_jokerbot", "setitle@Edu_jokerbot"]) & pyrogram.Filters.group)
async def setchat_title(bot, update):
    user = update.from_user.id
    b = await bot.get_chat_member(update.chat.id, user)
    if b.status == "administrator" or b.status == "creator":
        if update.text.lower() == "/setitle@" + Config.bot_name:
            num = int(Config.netnum) + int(9)
            title = update.text[num:]
        else:
            title = update.text[9:]
        await bot.set_chat_title(
            chat_id=update.chat.id,
            title=title
        )
    else:
        await bot.send_message(chat_id=update.chat.id, text="Who are you Non-Admin to command me?", reply_to_message_id=update.message_id)
        
@pyrogram.Client.on_message(pyrogram.Filters.command(["pin"]) & pyrogram.Filters.group)
async def pin_message(bot, update):
    if update.reply_to_message is not None:
        user = update.from_user.id
        b = await bot.get_chat_member(update.chat.id, user)
        if b.status == "administrator" or b.status == "creator":
            await bot.pin_chat_message(chat_id=update.chat.id, message_id=update.reply_to_message.message_id)
        else:
            await bot.send_message(chat_id=update.chat.id, text="Who are you Non-Admin to command me?", reply_to_message_id=update.message_id)
    else:
        await bot.send_message(chat_id=update.chat.id, text=" Reply to a message to be pinned", reply_to_message_id=update.message_id)


@pyrogram.Client.on_message(pyrogram.Filters.command(["unpin"]) & pyrogram.Filters.group)
async def unpin_message(bot, update):
    user = update.from_user.id
    b = await bot.get_chat_member(update.chat.id, user)
    if b.status == "administrator" or b.status == "creator":
        await bot.unpin_chat_message(chat_id=update.chat.id)
    else:
        await bot.send_message(chat_id=update.chat.id, text="Who are you Non-Admin to command me?", reply_to_message_id=update.message_id)



@pyrogram.Client.on_message(pyrogram.Filters.command(["ban"]) & pyrogram.Filters.group)
async def ban(bot, update):
    user = update.from_user.id
    u = await bot.get_chat_member(update.chat.id, user)
    if u.status == "administrator" or u.status == "creator":
        if update.reply_to_message is None:
            command, user = update.text.split(" ", 2)
            #user_id = int(user)
            if user.isdigit() == True:
                user_id = int(user)
            else:
                user_id = str(user)
            try:
                b = await bot.get_chat_member(update.chat.id, user_id)
            except RPCError:
                await bot.send_message(chat_id=update.chat.id, text="An unknown error while banning", reply_to_message_id=update.message_id)
                return
            ban_text = "Another bit of dust!\n\n<a href='tg://user?id={}'>{}</a> Banned <a href='tg://user?id={}'>{}</a>!".format(update.from_user.id, update.from_user.first_name, b.user.id, b.user.first_name) 
        else:
            user_id = update.reply_to_message.from_user.id
            ban_text = "Another bit of dust!\n\n<a href='tg://user?id={}'>{}</a> Banned <a href='tg://user?id={}'>{}</a>!".format(update.from_user.id, update.from_user.first_name, update.reply_to_message.from_user.id, update.reply_to_message.from_user.first_name) 
        await bot.kick_chat_member(chat_id=update.chat.id, user_id=user_id)
        await bot.send_message(chat_id=update.chat.id, text=ban_text, reply_to_message_id=update.message_id)
    else:
        await bot.send_message(chat_id=update.chat.id, text="Who are you Non-Admin to command me?", reply_to_message_id=update.message_id)

@pyrogram.Client.on_message(pyrogram.Filters.command(["tban"]) & pyrogram.Filters.group)
async def tban(bot, update):
    user = update.from_user.id
    u = await bot.get_chat_member(update.chat.id, user)
    if u.status == "administrator" or u.status == "creator":
        if update.reply_to_message is None:
            command, user, timev = update.text.split(" ", 3)
            #user_id = int(user)
            if user.isdigit() == True:
                user_id = int(user)
            else:
                user_id = str(user)
            utime = await sec(timev)
            try:
                b = await bot.get_chat_member(update.chat.id, user_id)
            except RPCError:
                await bot.send_message(chat_id=update.chat.id, text="An unknown error while banning", reply_to_message_id=update.message_id)
                return
            ban_text = "Another bit of dust!\n\n<a href='tg://user?id={}'>{}</a> Banned <a href='tg://user?id={}'>{}</a>! for {}".format(update.from_user.id, update.from_user.first_name, b.user.id, b.user.first_name, timev) 
        else:
            user_id = update.reply_to_message.from_user.id
            command, timev = update.text.split(" ", 2)
            utime = await sec(timev)
            ban_text = "Another bit of dust!\n\n<a href='tg://user?id={}'>{}</a> Banned <a href='tg://user?id={}'>{}</a>! for {}".format(update.from_user.id, update.from_user.first_name, update.reply_to_message.from_user.id, update.reply_to_message.from_user.first_name, timev) 
        await bot.kick_chat_member(chat_id=update.chat.id, user_id=user_id, until_date=int(time.time()) + int(utime))
        await bot.send_message(chat_id=update.chat.id, text=ban_text, reply_to_message_id=update.message_id)
    else:
        await bot.send_message(chat_id=update.chat.id, text="Who are you Non-Admin to command me?", reply_to_message_id=update.message_id)


@pyrogram.Client.on_message(pyrogram.Filters.command(["unban"]) & pyrogram.Filters.group)
async def unban(bot, update):
    user = update.from_user.id
    u = await bot.get_chat_member(update.chat.id, user)
    if u.status == "administrator" or u.status == "creator":
        if update.reply_to_message is None:
            command, user = update.text.split(" ", 2)
            if user.isdigit() == True:
                user_id = int(user)
            else:
                user_id = str(user)
            try:
                b = await bot.get_users(user_id)
            except RPCError:
                await bot.send_message(chat_id=update.chat.id, text="Invalid username or user id", reply_to_message_id=update.message_id)
                return
            unban_text = "Ok I will give a second chance for <a href='tg://user?id={}'>{}</a> !".format(b.id, b.first_name) 
        else:
            user_id = update.reply_to_message.from_user.id
            unban_text = "OK I will give a second chance for <a href='tg://user?id={}'>{}</a>!".format(update.reply_to_message.from_user.id, update.reply_to_message.from_user.first_name) 
        try:
            await bot.unban_chat_member(chat_id=update.chat.id, user_id=user_id)
        except RPCError:
            await bot.send_message(chat_id=update.chat.id, text="Invalid username or user id", reply_to_message_id=update.message_id)
            return
        await bot.send_message(chat_id=update.chat.id, text=unban_text, reply_to_message_id=update.message_id)

@pyrogram.Client.on_message(pyrogram.Filters.command(["mute"]) & pyrogram.Filters.group)
async def mute(bot, update):
    user = update.from_user.id
    u = await bot.get_chat_member(update.chat.id, user)
    if u.status == "administrator" or u.status == "creator":
        if update.reply_to_message is None:
            command, user = update.text.split(" ", 2)
            #user_id = int(user)
            if user.isdigit() == True:
                user_id = int(user)
            else:
                user_id = str(user)
            try:
                b = await bot.get_chat_member(update.chat.id, user_id)
            except RPCError:
                await bot.send_message(chat_id=update.chat.id, text="An unknown error while banning", reply_to_message_id=update.message_id)
                return
            mute_text = "<a href='tg://user?id={}'>{}</a> Muted <a href='tg://user?id={}'>{}</a>!".format(update.from_user.id, update.from_user.first_name, b.user.id, b.user.first_name) 
        else:
            user_id = update.reply_to_message.from_user.id
            mute_text = "<a href='tg://user?id={}'>{}</a> Muted <a href='tg://user?id={}'>{}</a>!".format(update.from_user.id, update.from_user.first_name, update.reply_to_message.from_user.id, update.reply_to_message.from_user.first_name) 
        await bot.restrict_chat_member(chat_id=update.chat.id, user_id=user_id, permissions=ChatPermissions(can_invite_users=True))
        await bot.send_message(chat_id=update.chat.id, text=mute_text, reply_to_message_id=update.message_id)
    else:
        await bot.send_message(chat_id=update.chat.id, text="Who are you Non-Admin to command me?", reply_to_message_id=update.message_id)

