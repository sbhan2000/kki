from pyrogram import filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from MatrixMusic import app as Client
from MatrixMusic import app
from pyrogram.types import InlineKeyboardButton
import config
import asyncio
import random
from strings.filters import command


@Client.on_callback_query(filters.regex("arbic"))
async def arbic(_, query: CallbackQuery):
    await query.answer("الـصفحة الـرئيسية")
    await query.edit_message_text(
        f"""<b> انا بوت تشغيل الميديا الصوتية والمرئية .⚡
قم بإضافة البوت إلي مجموعتك او قناتك .⚡
سيتم تفعيل البوت وانضمام المساعد تلقائياً
في حال مواجهت مشاكل تواصل مع المطور 
استخدم الازرار لمعرفه اوامر الاستخدام .⚡<b> """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "اضف البوت الى مجموعتك ⚡♥",
                        url=f"https://t.me/{app.username}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton(" الدعم والتواصل ", url=f"https://t.me/ah07v"),
                ],
                [                   InlineKeyboardButton(" طريقه التشغيل ", callback_data="bcmds"),
                    InlineKeyboardButton(" طريقه التفعيل ", callback_data="bhowtouse"),
                ],
                [
                    InlineKeyboardButton(
                        " الدعم ", url=config.SUPPORT_CHAT
                    ),
                    InlineKeyboardButton(
                        " القناة ", url=config.SUPPORT_CHANNEL),
                ],
                [
                    InlineKeyboardButton(
                        " الـمطور ", user_id=config.OWNER_ID 
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )

@Client.on_callback_query(filters.regex("english"))
async def english(_, query: CallbackQuery):
    await query.answer("الـصفحة الـرئيسية")
    await query.edit_message_text(
        f"""<b> A Telegram Music Bot
Played Music and Video in VC
Bot Online Now ......🖱️❤️
Add Me To Your Chat
Powered By [ᎪᎻᎷᎬᎠ]  
        <b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝐴𝑑𝑑 𝑚𝑒 𝑡𝑜 𝑦𝑜𝑢𝑟 𝐺𝑟𝑜𝑢𝑝",
                        url=f"https://t.me/{app.username}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("𝑠𝑢𝑝𝑝𝑜𝑟𝑡 ", url=f"https://t.me/ah07v"),
                ],
                [                
                    InlineKeyboardButton(" 𝐶𝑜𝑚𝑚𝑎𝑛𝑑𝑠", callback_data="cbcmds"),
                    InlineKeyboardButton(" 𝐵𝑎𝑠𝑖𝑐 𝐺𝑢𝑖𝑑𝑒 ", callback_data="cbhowtouse"),
                ],
                [
                    InlineKeyboardButton(
                        " 𝐺𝑟𝑜𝑢𝑝 ", url=config.SUPPORT_CHAT
                    ),
                    InlineKeyboardButton(
                        " 𝐶ℎ𝑎𝑛𝑛𝑒𝑙 ", url=config.SUPPORT_CHANNEL
                    ),
                ],
                [
                    InlineKeyboardButton(
                        " 𝐷𝑒𝑣𝑒𝑙𝑜𝑝𝑒𝑟 ", user_id=config.OWNER_ID 
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )

@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.answer("طريقة الـتفعيل")
    await query.edit_message_text(
        f"""<b>
 ❓ Basic Guide for using this bot:
1.) First, add me to your group.
2.) Then, promote me as administrator and give all permissions except Anonymous Admin.
3.) After promoting me, type /reload in group to refresh the admin data.
3.) Add Assistant to your group or invite her.
4.) Turn on the video chat first before start to play video/music.
5.) Sometimes, reloading the bot by using /reload command can help you to fix some problem.
📌 If the userbot not joined to video chat, make sure if the video chat already turned on.
💡 If you have a follow-up questions about this bot, you can tell it on my support chat here: https://t.me/ah_2_v
⚡  Developer by ᎪᎻᎷᎬᎠ   
<b>""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="english")]]
        ),
    )


    
    
@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.answer("طريقة الـتشغيل")
    await query.edit_message_text(
        f""" <b>✨Hello  {query.message.chat.first_name} !
» press the button below to read the explanation and see the list of available commands !
⚡ Powered by ᎪᎻᎷᎬᎠ<b> """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Admin Cmd", callback_data="wwwer"),
                    InlineKeyboardButton("Basic Cmd", callback_data="cbsud"),
                ],[
                    InlineKeyboardButton("Sudo Cmd", callback_data="ophgd")
                ],[
                    InlineKeyboardButton("Go Back ", callback_data="english")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("wwwer"))
async def cbwwwer(_, query: CallbackQuery):
    await query.answer("اوامر الادمن")
    await query.edit_message_text(
        f"""<b>
🏮 here is the admin commands:
» /pause - pause the stream
» /resume - resume the stream 
» /skip - switch to next stream 
» /stop - stop the streaming 
» /loop - loop the streaming 
⚡️  Developer by ᎪᎻᎷᎬᎠ 
<b>""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbsud"))
async def cbsud(_, query: CallbackQuery):
    await query.answer("اوامر الـتشغيل")
    await query.edit_message_text(
        f"""<b> 
🏮 here is the basic commands:
» /play (song name/link) - play music on video chat
» /vplay (video name/link) - play video on video chat
» /video (query) - download video from youtube
» /song (query) - download song from youtube
» /search (query) - search a youtube video link
» /ping - show the bot ping status
» /alive - show the bot alive info (in group)
» /tgm - To make a telegraph link
⚡️  Developer by ᎪᎻᎷᎬᎠ

<b>""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("ophgd"))
async def cbophgd(_, query: CallbackQuery):
    await query.answer("sudo commands")
    await query.edit_message_text(
        f""" 
✏ اوامر المطورين.
» • تعين اسم البوت • 
» • الاحصائيات •
» • المجموعات • 
» • المستخدمين • 
» • قسم الاذاعه •
» • قسم التحكم في الحساب المساعد •
» • تفعيل سجل التشغيل • 
» • تعطيل سجل التشغيل •
» • تغير مكان سجل التشغيل •
» • تفعيل الاشتراك الإجباري • 
» • تعطيل الاشتراك الإجباري • 
» • المكالمات النشطه • 
» • تشغيل مخصص • 
» • اذاعه صوتيه • تغير مكان سجل التشغيل • : لتغير مجموعة السجل
⚡  Developer by ᎪᎻᎷᎬᎠ

""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("bhowtouse"))
async def acbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>
طريقة تفعيل البوت في مجموعتك ⚡♥️:
1.) اولا قم بإضافة البوت اللي مجموعتك ⚡.
2.) قم بترقية البوت مشرف مع الصلاحيات المطلوبة ⚡.
3.)  يقوم البوت بتحديث قائمة الاداره تلقائياً ⚡.
3.)  قم بإضافة الحساب المساعد اللي المجموعة ⚡.
4.) تاكد من تشغيل المحادثة المرئية ⚡.
📌  اذا لم يستطع الحساب المساعد الانضمام اللي المحادثة المرئيه قم بإعادة تشغيل المحادثه ⚡.
💡 في حال واجهت اي مشكلة اخري يمكنك التواصل مع المطور من هنا : https://t.me/ah07v
⚡  Developer by ᎪᎻᎷᎬᎠ

<b> """,

        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(" عوده ", callback_data="arbic")]]
        ),
    )


@Client.on_callback_query(filters.regex("bcmds"))
async def acbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>✨Hello  {query.message.chat.first_name} !
» اتبع الازرار بالاسفل لمعرفة طريقة التشغيل ⚡
⚡  Developer by 𝗔𝗛𝗠𝗘𝗗 <b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("اوامر التشغيل", callback_data="bbasic"),
                    InlineKeyboardButton("اوامر الادمن", callback_data="aladmin"),
                ],[
                    InlineKeyboardButton("اوامر المطورين", callback_data="bsudo")
                ],[
                    InlineKeyboardButton(" عوده ", callback_data="arbic")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("bbasic"))
async def acbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>
      اوامر التشغيل ⚡:
» شغل او تشغيل - لتشغيل الموسيقى   
» بحث - للبحث عن نتائج في اليوتيوب 
» فيديو + اسم الفيديو - لتحميل مقطع فيديو 
» تحميل + اسم الاغنيه - لتحميل ملف صوتي
» المصحف - لأظهار قائمة السور القران
» طباعه - لطباعة كلمه او جمله في صوره
» صور - للبحث عن الصور وتحميلها
» تلجراف - لعمل رابط تلجراف بالرد على الصوره او الفيديو
» تفعيل الاذان - تفعيل تنبيهات الصلاة في المحادثه 
» بنج - عرض سرعة الاستجابة 
» سورس - لعرض معلومات البوت 
⚡️  Developer by ᎪᎻᎷᎬᎠ  
       <b> """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(" عوده ", callback_data="bcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("aladmin"))
async def acaladmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>
      اوامر التحكم للخاصة بالادمنية: 
» ايقاف مؤقت - ايقاف التشغيل موقتأ 
» استكمال - لاستكمال التشغيل 
» تخطي - لتخطي تشغيل الحالي 
» ايقاف او اسكت - لايقاف تشغيل الحالي 
» تكرار او كررها - لتكرار التشغيل الحالي 
» تمرير او مرر - لتتغير وقت التشغيل الحالي 
⚡️  Developer by ᎪᎻᎷᎬᎠ  
      <b>  """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(" عوده ", callback_data="bcmds")]]
        ),
    )
    

@Client.on_callback_query(filters.regex("bsudo"))
async def acbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>
       ✏ اوامر الـمطورين.
» انضم - انضمام الحساب المساعد الى المجموعة
» غادر - خروج الحساب المساعد من المجموعة
» المكالمات الصوتيه - لجلب المكالمات الصوتيه النشطه
» المكالمات المرئيه - لجلب المكالمات المرئيه النشطه
» اذاعه - لعمل اذاعه في المجموعات والكروبات
» حظر - لحظر عضو من المجموعه
» الغاء الحظر - لرفع الحظر عن العضو
» المحظورين - لعرض المحضورين في المجموعه
» حظر المجموعه - لحظر المجموعه من استخدام البوت[حظر+ايدي المجموعه] 
» الغاء حظر المجموعه - لرفع الحظر عن المجموعه[الغاء حظر المجموعه+ايدي المجموعه] 

⚡  Developer by ᎪᎻᎷᎬᎠ 
        <b>""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(" عوده ", callback_data="bcmds")]]
        ),
    )

