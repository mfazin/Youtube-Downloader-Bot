from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/ekbotz_update")],
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/Ek_comme_nt_bot")]
        [InlineKeyboardButton("Share", url="https://t.me/share/url?url=http://t.me/Ek_Youtube_Bot
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}. I am a powerful YouTube DL Bot of EK BOTZ PROJECT.</b>\n/help for More info"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
