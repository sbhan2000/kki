import requests
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import CallbackQuery, InputMediaPhoto, InlineKeyboardMarkup, InlineKeyboardButton
from pySmartDL import SmartDL
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from MatrixMusic import app


last_clicked_button = {}

@app.on_message(filters.command("تنزيل", ""))
async def tom_youtube(client, message):
    global video_link, audio_link, title, duration, rating, views, description

    name = message.text.split(None, 1)[1]
    response = requests.get(f"https://youtube.dev-tomtom.repl.co/tom={name}")
    data = response.json()
    tom_info = data[0]["Tom"]
    audio_link = tom_info["audio_link"]
    video_link = tom_info["download_link_video"]
    photo_link = tom_info["photo"]
    title = tom_info["title"]
    duration = tom_info["duration"]
    rating = tom_info["rating"]
    views = tom_info["views"]
    description = tom_info["description"]
    

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("تحميل الصوت", callback_data=f"audio_{name}"),
                InlineKeyboardButton("تحميل الفيديو", callback_data=f"video_{name}"),
            ]
        ]
    )
    
    
    msg = await message.reply_photo(photo_link, caption=f"Name = {title} \n\nDuration = {duration} \n\nRating = {rating} \n\nViews = {views}", reply_markup=keyboard)


@app.on_callback_query()
async def handle_callback_query(client, callback_query: CallbackQuery):
    global video_link
    global audio_link
    button_type = callback_query.data.split("_")[0]
    name = callback_query.data.split("_")[1]
    

    msg = await callback_query.message.reply_text("يرجى الانتظار جار الرفع  ...")
    last_clicked_button[callback_query.message.chat.id] = msg.id
    
    if button_type == "audio":
        obj = SmartDL(audio_link, progress_bar=False, verify=False)
        obj.start()
        obj.wait()
        audio = obj.get_dest()
      
        await callback_query.message.reply_audio(audio, title=f"{title}")
    
    elif button_type == "video":
        obj = SmartDL(video_link, progress_bar=False, verify=False)
        obj.start()
        obj.wait()
        video=obj.get_dest()
       
        await callback_query.message.reply_video(video, caption=f"{title}")
    

    await client.delete_messages(chat_id=callback_query.message.chat.id, message_ids=[last_clicked_button.get(callback_query.message.chat.id)])

