from datetime import datetime

import pyrogram

@pyrogram.Client.on_message(pyrogram.Filters.command(["ping"]))
async def ping(bot, update):
    first = datetime.now()
    sent = await bot.send_message(chat_id=update.chat.id, text="<B>Pong!</B>", parse_mode="html")
    second = datetime.now()
    await sent.edit_message_text(chat_id=update.message.chat.id, text=f"**Pong!** `{(second - first).microseconds / 1000}`ms")
