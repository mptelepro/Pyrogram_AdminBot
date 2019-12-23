import aiohttp
import pyrogram



@pyrogram.Client.on_message(pyrogram.Filters.command(["git"]))
async def git(bot, update):
    text = update.text[5:]
    async with aiohttp.ClientSession() as session:
        req = await session.get('https://api.github.com/users/' + text)
        res = await req.json()
    replyttext = """<B>Name :</B> <code>{res["name"]}</code>
<B>Login :</B> <code>{res["login"]}
<B>Location :</B> <code>{res["location"]}
<B>Type :</B> <code>{res["type"]}
<B>Bio : </B> <code>{res["bio"]}
    """
    if not res.get('login'):
        await bot.send_message(
            chat_id=update.chat.id,
            text="User {} not found".format(text),
            reply_to_message_id=update.message_id
        )
        return
    else:
        await bot.send_message(chat_id=update.chat.id, text=replyttext, reply_to_message_id=update.message_id) 
        return
        
