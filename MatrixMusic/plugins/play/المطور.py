import asyncio
import os
import requests
import pyrogram
from pyrogram import Client, filters, emoji
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified
from MatrixMusic import app
from config import OWNER_ID, LOGGER_ID, SUPPORT_CHANNEL


@app.on_message(command(["مطور", "", "المطور"]))
async def devid(client: Client, message: Message):
    usr = await client.get_users(OWNER_ID)
    name = usr.first_name
    usrnam = usr.username
    uid = OWNER_ID
    await app.download_media(usr.photo.big_file_id, file_name=os.path.join("downloads", "developer.jpg"))
       
    await message.reply_photo(
        photo="downloads/developer.jpg",
        caption=f"""<b> ⦗ 𝐃𝒆𝒗𝒆𝒍𝒐𝒑𝒆𝒓 ⦘<b>\n<b>↯︙𝖣𝖾𝗏 ↬ :</b>⦗ <a href='tg://user?id={uid}'>{name}</a> ⦘\n\n<b>↯︙𝖴𝗌𝖤𝗋 ↬</b> ⦗ @{usrnam} ⦘\n<b>↯︙𝖨𝖣 ↬<b> ⦗ {usr.id} ⦘\n<b>↯︙𝖡𝗂𝖮 ↬ <b>⦗ {usr.bio} ⦘""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(name, url=f"tg://user?id={uid}"),
                ],[
                    InlineKeyboardButton(
                        "قناة الـبوت", url=config.SUPPORT_CHANNEL),
                ],
            ]
        ),
    )
