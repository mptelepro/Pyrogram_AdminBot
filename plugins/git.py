import aiohttp
import pyrogram
import json


@pyrogram.Client.on_message(pyrogram.Filters.command(["git"]))
async def git(bot, update):
    command, text = update.text.split(" ", 1)
    async with aiohttp.ClientSession() as session:
        req = await session.get('https://api.github.com/users/' + text)
        rep = await req.json()
        repstr = str(rep)
        res = json.loads(repstr)
    replyttext = """<B>Name :</B> <code>res["name"]</code>
<B>Login :</B> <code>res["login"]</code>
<B>Location :</B> <code>res["location"]</code>
<B>Type :</B> <code>res["type"]</code> 
<B>Bio : </B> <code>res["bio"]</code>
    """
    if not res.get('login'):
        await bot.send_message(
            chat_id=update.chat.id,
            text="User {} not found".format(text),
            reply_to_message_id=update.message_id
        )
        return
    else:
        await bot.send_message(chat_id=update.chat.id, text=replyttext, reply_to_message_id=update.message_id, parse_mode="HTML") 
        return
        
