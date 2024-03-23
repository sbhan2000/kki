from requests import Session
import urllib.request as request
from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery
from pyrogram.types import InlineKeyboardMarkup as Markup, InlineKeyboardButton as Button
from pyrolistener import Listener
from pyrolistener.exceptions import TimeOut
from os import remove
from MatrixMusic import app

listener = Listener(app)
session = Session()
api = 'https://api.saidazim.uz/tiktok/'
turl = 'https://vm.tiktok.com/{id}'

caption = '''
- nickname : {nickname}
- username : {username}
- title : {title}
- views : {views}
- likes : {likes}
- commments : {comments}
- shares : {shares}
'''

def downloadTiktok(url):
    params = {
        'url': url
    }
    res = session.get(api, params= params).json()
    if res.get('id') is None : return {'error' : '- invalid url!!!'}
    _caption = caption.format(
        nickname = res['nickname'],
        username = res['username'],
        title = res['title'],
        views = res['view_count'],
        likes = res['like_count'],
        comments = res['comment_count'],
        shares = res['share_count']
    )
    return {
        'caption': _caption,
        'id': url.split('/')[3],
        'video': res['video']
    }

def downloadAudio(_id):
    url = turl.format(id=_id)
    params = {
        'url': url
    }
    res = session.get(api, params= params).json()
    audio = res['music']
    request.urlretrieve(audio, f'{_id}.mp3')


@app.on_message(filters.command(['تيك', 'تيك توك'], ''))
async def reciveURL(_: Client, message: Message):
    try: ask = await listener.listen(
        chat_id = message.chat.id,
        from_id = message.from_user.id,
        text = '- Okey send me a tiktok url now.',
        timeout = 30
    )
    except TimeOut: return await message.reply('- Time to recieve a tiktok url is ran out.', reply_to_message_id = message.id)
    response = downloadTiktok(ask.text)
    if response.get('error'): return await ask.reply(response['error'])
    request.urlretrieve(response['video'], f'{response["id"]}.mp4')
    markup = Markup([
        [Button('- Download Audio -',f'adownload {response["id"]}')],
        [Button('- Developer -', user_id = 5451878368)]
    ])
    await ask.reply_video(video = f'{response["id"]}.mp4', caption = response['caption'], reply_markup = markup, reply_to_message_id = message.id)  
    remove(f'{response["id"]}.mp4')
    

@app.on_callback_query(filters.regex(r'^(adownload)'))
async def aDownload(_: Client, callback: CallbackQuery):
    _id = callback.data.split()[1]
    downloadAudio(_id)
    await callback.message.reply_audio(
        audio = f'{_id}.mp3',
        reply_to_message_id = callback.message.id
    )
    remove(f'{_id}.mp4')


# https://vm.tiktok.com/ZM6NRL4nG
if __name__ == '__main__': 
