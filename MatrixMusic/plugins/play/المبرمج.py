import asyncio
from config import OWNER
import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from MatrixMusic.plugins.play.filters import command
from MatrixMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from MatrixMusic import app
from random import  choice, randint

                


@app.on_message(filters.command(["مبرمج","المبرمج"]))
async def yas(client, message):
    usr = await client.get_chat("ah_2_v")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"↯︙𝙽𝙰𝙼𝙴 :{name}\n↯︙𝚄𝚂𝙴𝚁 :@{usr.username}\n↯︙𝙸𝙳 :`{usr.id}`\n↯︙𝙱𝙸𝙾 :{usr.bio}", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )  



@app.on_message(filters.command("المالك"))
async def yas(client, message):
    usr = await client.get_chat("{OWNER}")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"↯︙𝙽𝙰𝙼𝙴 :{name}\n↯︙𝚄𝚂𝙴𝚁 :@{usr.username}\n↯︙𝙸𝙳 :`{usr.id}`\n↯︙𝙱𝙸𝙾 :{usr.bio}", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )    
