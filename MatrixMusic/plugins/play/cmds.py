import asyncio
import os
import requests
import pyrogram
from pyrogram import Client, filters, emoji
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified
from MatrixMusic import app
from config import OWNER_ID, LOGGER_ID
import config




@app.on_message(command(["مطور", "المطور"]) & filters.group)
async def zilzal(client: Client, message: Message):
    usr = await client.get_users(OWNER_ID)
    name = usr.first_name
    usrnam = usr.username
    async for photo in client.iter_profile_photos(OWNER_ID):
                    await message.reply_photo(photo.file_id,       caption=f"""ٴ<b>- - - - - - - - - - - - - - - - - -</b>
                    
- 𝚆𝙾𝙽𝙴𝚁 :{usr.first_name}
- 𝚄𝚂𝙴𝚁 :@{usrnam} 
- 𝙸𝙳 :{usr.id}
 </b>- - - - - - - - - - - - - - - - - -</b> """, 
reply_markup=InlineKeyboardMarkup(
          [               
            [            
              InlineKeyboardButton (name, url=f"https://t.me/{usrnam}"),
                ],
                [
                    InlineKeyboardButton(
                        " الدعم ", url=config.SUPPORT_CHAT
                    ),
                    InlineKeyboardButton(
                        " القناة ", url=config.SUPPORT_CHANNEL),
            ],
          ]
       )                 
    )                    
                    sender_user = "@{senderuser}" if senderuser else "لا يوجـد"
                    await app.send_message(OWNER_ID, f"- المستخـدم {message.from_user.mention} يناديـك \n\n- الاسـم : {sender_name} \n- الايـدي : {sender_id}\n- اليـوزر : {sender_user}")
                    return await app.send_message(LOGGER_ID, f"- المستخـدم {message.from_user.mention} يناديـك \n\n- الاسـم : {sender_name} \n- الايـدي : {sender_id}\n- اليـوزر : {sender_user}")
