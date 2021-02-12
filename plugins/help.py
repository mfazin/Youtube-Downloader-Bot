from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Currently Only supports Youtube Single url  (No playlist). Just Send Youtube Url and I will fetch the data and you select the quality, will get the video😃."
    await message.reply_text(helptxt)
