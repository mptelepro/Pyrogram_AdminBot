import html
import os

import pyrogram


@pyrogram.Client.on_message(pyrogram.Filters.command(["jsondump"]))
async def jsondump(bot, update):
    if len(str(update)) < 3000 and "-f" not in update.command:
        await bot.send_message(chat_id=update.chat.id, text="<code>Json Dump\n\n" + update + "\n\n@Keralasbots</code>", parse_mode="HTML")
    else:
        fname = f"dump-{update.chat.id}.json"
        with open(fname, "w") as f:
            f.write(str(update))
        await bot.send_document(chat_id=update.chat.id, document=fname)
        os.remove(fname)
