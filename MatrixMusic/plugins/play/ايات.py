from pyrogram import Client, filters , enums
from pyrogram.types import Message
from requests import get
from random import randint
import asyncio
from MatrixMusic import app

@app.on_message(filters.command(["اية","ايه"]))
async def send_quran_verse(c: Client, m: Message):
    online = True
    while online:
        verse_number = randint(1, 6236)
        res = get(f"http://api.alquran.cloud/v1/ayah/{verse_number}/ar.abdulsamad").json()
        
        text = f"• {res['data']['surah']['name']} • \n\n*﴿ {res['data']['text']} ﴾* \n\n- الجزء: {res['data']['juz']} - الحزب: {res['data']['hizbQuarter']} - الأية: {res['data']['numberInSurah']} - الصفحة: {res['data']['page']} . \n\n"
        
        async for dialog in c.get_dialogs():
            if dialog.chat.type != enums.ChatType.BOT:
                try:
                    await c.send_audio(dialog.chat.id, res['data']['audio'], text)
                except Exception as e:
                    print(e)
        
        await asyncio.sleep(86400)

client.run()
