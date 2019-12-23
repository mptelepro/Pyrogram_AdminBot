import pyrogram
from config import Config

@pyrogram.Client.on_message(pyrogram.Filters.command(["set_title"]) & pyrogram.Filters.group)
async def setchat_title(bot, update):
    title = update.text[10:]
    try:
        await bot.set_chat_title(
            chat_id=update.chat.id,
            title=title
        )
    except:
        pass
        await bot.send_message(
            chat_id=update.chat.id, 
            text="Successfully changed title", 
            reply_to_message_id=update.message_id
        )

@pyrogram.Client.on_message(pyrogram.Filters.command(["pin"]) & pyrogram.Filters.group)
async def pin_message(bot, update):
    await bot.pin_chat_message(chat_id=update.chat.id, message_id=update.reply_to_message.message_id)



