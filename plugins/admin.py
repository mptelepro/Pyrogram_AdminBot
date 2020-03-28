import pyrogram
from config import Config

@pyrogram.Client.on_message(pyrogram.Filters.command(["setitle"]) & pyrogram.Filters.group)
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
    else:
        user_id = update.reply_to_message.from_user.id
    await bot.kick_chat_member(chat_id=update.chat.id, user_id=user_id)
