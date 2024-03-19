from config import channel
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup as Markup, InlineKeyboardButton as Button
from pyrogram.enums import ChatType
from pyrogram.errors import UserNotParticipant
from MatrixMusic import app


async def subscription(_, __: Client, message: Message):
    user_id = message.from_user.id
    try: await app.get_chat_member(channel, user_id)
    except UserNotParticipant: return False
    return True
    
subscribed = filters.create(subscription)

@app.on_message(~subscribed)
async def checker(_: Client, message: Message):
    if message.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]: await message.delete()
    user_id = message.from_user.id
    user = message.from_user.first_name
    markup = Markup([
        [Button("قناة البوت", url=f"https://t.me/{channel}")]
    ])
    await message.reply(
        f"عذرًا عزيزي {user} عليك الإشتراك بقناة البوت اولا.",
        reply_markup = markup
    )
    



#------------------------
@app.on_message( filters.incoming & filters.private, group=-1)
async def checker(_: Client, message: Message):
    if not channel:
        return
    try:
        try:
            await app.get_chat_member(channel, msg.from_user.id)
        except UserNotParticipant:
            if channel.isalpha():
                link = "https://t.me/" + channel
            else:
                chat_info = await app.get_chat(channel)
                link = chat_info.invite_link
            try:
                await msg.reply(f"عذراً عزيزي {user} عليك الإشتراك بقناة البوت اولا.",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("قناة البوت", url=link),
                            ]
                        ]
                    )
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"ارفع البوت مشࢪف في القناة: {channel} !")
