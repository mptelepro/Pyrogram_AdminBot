import pyrogram
from config import Config

@pyrogram.Client.on_message(pyrogram.Filters.command(["set_title"]) & pyrogram.Filters.group)
async def setchat_title(bot, update):
    title = update.text[10:]
    await bot.set_chat_title(
        chat_id=update.chat.id,
        title=title
    )



