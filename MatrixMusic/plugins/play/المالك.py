import asyncio
import os
import time
import requests
import aiohttp
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from MatrixMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from MatrixMusic import app
from asyncio import gather
from pyrogram import enums
from pyrogram.enums import ChatMemberStatus


    
@app.on_message(command(["المالك"]) & filters.group)
async def creator(c, msg):
    x = []
    async for m in app.get_chat_members(msg.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        if m.status == ChatMemberStatus.OWNER:
            adox = await app.get_chat(chat_id=m.user.id)
            bio = adox.bio
            if adox.photo:
                async for photo in app.get_chat_photos(m.user.id, limit=1):
                    await msg.reply_photo(
                        photo.file_id,
                        caption=f"᥆ꪝᥒ꧖ᖇ | - {adox.mention_markdown} ↯︙\n\nႦᎥ᥆ | - {adox.bio} ↯︙",
                        reply_markup=InlineKeyboardMarkup(
                            [[InlineKeyboardButton(adox.first_name, url=f"https://t.me/{adox.username}")]])
                    )
            else:
                await msg.reply_text(
                    f"᥆ꪝᥒ꧖ᖇ | - {adox.mention_markdown} ↯︙\n\nႦᎥ᥆ | - {adox.bio} ↯︙",
                    reply_markup=InlineKeyboardMarkup(
                        [[InlineKeyboardButton(adox.first_name, url=f"https://t.me/{adox.username}")]]
                    )
                )
    else:
        await msg.reply_text("الحساب محذوف")
