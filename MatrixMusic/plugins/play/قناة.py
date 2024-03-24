from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from MatrixMusic import app
from config import channel, OWNER_ID

@app.on_message(filters.private & filters.user(OWNER_ID))
async def must_join_channel(_, message):
    if "‹ قناة الاشتراك ›" in message.text:
        link = f"https://t.me/{channel}"
        await message.reply(
            text=f"~ عزيزي المطور \n~ هذا هي قناة الاشتراك الاجباري @{channel} .",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("قناة البوت", url=link)]
            ])
        )
