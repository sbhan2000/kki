from config import MUST_JOIN
from pyrogram import Client, filters
from pyrogram.types import Message
from MatrixMusic.plugins.play.filters import command
from pyrogram.types import InlineKeyboardMarkup as Markup, InlineKeyboardButton as Button
from pyrogram.enums import ChatType
from pyrogram.errors import UserNotParticipant
from MatrixMusic import app



@app.on_message( filters.incoming & filters.private, group=-1)
@app.on_message( filters.incoming & filters.group, group=-1)
async def must_join_channel(app: Client, msg: Message):
    if not MUST_JOIN:
        return
    try:
        try:
            await app.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await app.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply(f"↯︙عـذراً، عـلـيـڪ الانـضـمـام الى هـذهِ [ الـقـنـاة ]({link}) أولاً\n↯︙اشـتـرڪ ثـم أرسـل /start",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("اقناة البوت", url=link),
                            ]
                        ]
                    )
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"ارفع البوت مشࢪف في القناة: {MUST_JOIN} !")

