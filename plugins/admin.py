import pyrogram
from config import Config
from pyrogram.errors import RPCError

@pyrogram.Client.on_message(pyrogram.Filters.command(["setitle", "setitle@edu_jokerbot", "setitle@Edu_jokerbot"]) & pyrogram.Filters.group)
async def setchat_title(bot, update):
    if update.text.lower() == "/setitle@" + Config.bot_name:
        num = int(Config.netnum) + int(9)
        title = update.text[num:]
    else:
        title = update.text[9:]
    await bot.set_chat_title(
        chat_id=update.chat.id,
        title=title
    )
        
@pyrogram.Client.on_message(pyrogram.Filters.command(["pin"]) & pyrogram.Filters.group)
async def pin_message(bot, update):
    await bot.pin_chat_message(chat_id=update.chat.id, message_id=update.reply_to_message.message_id)

@pyrogram.Client.on_message(pyrogram.Filters.command(["unpin"]) & pyrogram.Filters.group)
async def unpin_message(bot, update):
    await bot.unpin_chat_message(chat_id=update.chat.id)


@pyrogram.Client.on_message(pyrogram.Filters.command(["ban"]) & pyrogram.Filters.group)
async def ban(bot, update):
    if update.reply_to_message is None:
        command, user = update.text.split(" ", 2)
        user_id = int(user)
        try:
            b = await bot.get_chat_member(update.chat.id, user_id)
        except RPCError:
            await bot.send_message(chat_id=update.chat.id, text="An unknown error while banning")
            return
        ban_text = "Another bit of dust\n<a href='tg://user?id={}'>{}</a> Banned <a href='tg://user?id={}'>{}</a>".format(update.from_user.id, update.from_user.first_name, b.user.id, b.user.first_name) 
    else:
        user_id = update.reply_to_message.from_user.id
        ban_text = "Another bit of dust\n<a href='tg://user?id={}'>{}</a> Banned <a href='tg://user?id={}'>{}</a>".format(update.from_user.id, update.from_user.first_name, update.reply_to_message.from_user.id, update.reply_to_message.from_user.first_name) 
    await bot.kick_chat_member(chat_id=update.chat.id, user_id=user_id)
    await bot.send_message(chat_id=update.chat.id, text=ban_text)
