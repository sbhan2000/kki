import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from MatrixMusic import LOGGER, app, userbot, app2
from MatrixMusic.core.call import Zelzaly
from MatrixMusic.misc import sudo
from MatrixMusic.plugins import ALL_MODULES
from MatrixMusic.utils.database import get_banned_users, get_gbanned
from MatrixMusic import (
    ASS_ID,
    ASS_NAME,
    ASS_USERNAME,
    BOT_ID,
    BOT_NAME,
    BOT_USERNAME,
    LOGGER,
    SUNAME,
    app,
    app2,
    pytgcalls,
)
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("كود جلسة الحساب المساعد غير مدعوم ...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("MatrixMusic.plugins" + all_module)
    LOGGER("ميــوزك ريڤو").info("تم تحميل الاضافات ...✓")
    await userbot.start()
    await Zelzaly.start()
    try:
        await Zelzaly.stream_call("https://telegra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("ميــوزك ريڤو").info(
            "خطأ .. قم بفتح المكالمة في مجموعة السجل الخاصه بك\n\nجارِ ايقاف بوت الميوزك . . ."
        )
        exit()
    except:
        pass
    await Zelzaly.decorators()
    LOGGER("ميــوزك ريڤو").info("MatrixThon")
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("ميــوزك ريڤو").info("جارِ ايقاف بوت الميوزك . . .")

    
    try:
        await app2.send_message(
            SUNAME,
            f"✯ ѕᴘɪᴅᴇʀ ᴍᴜsɪᴄ ᴀss ✯\n\n𖢵 ɪᴅ : `{ASS_ID}`\n𖢵 ɴᴀᴍᴇ : {ASS_NAME}\n𖢵 ᴜsᴇʀɴᴀᴍᴇ : @{ASS_USERNAME}",
        )
    except:
        LOGGER.error(
            f"{ASS_NAME} failed to send message at @{SUNAME}, please go & check."
        )

    await app2.send_message(BOT_USERNAME, "/start")

    LOGGER.info(f"[•] Bot Started As {BOT_NAME}.")
    LOGGER.info(f"[•] Assistant Started As {ASS_NAME}.")

    LOGGER.info(
        "[•] \x53\x74\x61\x72\x74\x69\x6e\x67\x20\x50\x79\x54\x67\x43\x61\x6c\x6c\x73\x20\x43\x6c\x69\x65\x6e\x74\x2e\x2e\x2e"
    )
    await pytgcalls.start()
    await idle()



if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())







    
