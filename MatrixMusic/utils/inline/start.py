from pyrogram.types import InlineKeyboardButton

import config
from MatrixMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?startgroup=Commands&admin=ban_users+restrict_members+delete_messages+add_admins+change_info+invite_users+pin_messages+manage_call+manage_chat+manage_video_chats+promote_members",
            )
        ],
        [
            InlineKeyboardButton(text=_["S_B_6"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(text=" English 🇺🇸 ", callback_data="english"), 
            InlineKeyboardButton(text=" عربي 🇮🇶 ", callback_data="arbic")],
        [
            InlineKeyboardButton(text=" الـمطور ", user_id=config.OWNER_ID),
        ],
    ]
    return buttons
