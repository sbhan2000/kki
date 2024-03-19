from pyrogram import Client
from pyrogram.types import ChatPermissions, Message
from datetime import date
import time
from config import sudoers, get_bot_information
from MatrixMusic.plugins.play.developer import check_username
from MatrixMusic.plugins.play.group_rtb import managerrep_for_supmit, addadminrep_for_supmit
from MatrixMusic.plugins.play.rtp_function import sudooo2
from utils import html_user
from localization import use_chat_lang
from database import set_db_gban, del_db_gban, set_db_gmute, del_db_gmute, get_db_gban, get_db_gmute, get_db_wait, \
    get_db_greply, set_db_checkgroup, del_db_checkgroup, get_db_checkgroup, get_db_checkuser, set_db_checkuser, \
    get_db_waitg, get_db_replygroup, del_db_managerall, del_db_constractorsall, del_db_adminall, del_db_specialall, \
    get_db_addcommand


########################################################################################################################
########################################################################################################################
@use_chat_lang()
async def gbanrep(c: Client, m: Message, strings):
    try:
        leader = False
        for per in sudoers:
            if m.reply_to_message.from_user.id == per:
                leader = True
        if m.reply_to_message.from_user.id == 1748768168:
            await m.reply_text("🚦لايمكننى حظر مطور السورس\n↯", reply_to_message_id=m.message_id)
            await m.reply_animation("https://t.me/UURTBOT/36", reply_to_message_id=m.message_id)
            return
        else:
            if m.reply_to_message.from_user.id == 1748768168:
                await m.reply_text("🚦²لايمكننى حظر مطور السورس\n↯", reply_to_message_id=m.message_id)
                await m.reply_animation("https://t.me/UURTBOT/36", reply_to_message_id=m.message_id)
                return
            else:
                if m.reply_to_message.from_user.id == get_bot_information()[0]:
                    await m.reply_text("🚦لايمكننى حظر البوت\n↯", reply_to_message_id=m.message_id)
                    await m.reply_animation("https://t.me/UURTBOT/36", reply_to_message_id=m.message_id)
                    return
                else:
                    if leader:
                        await m.reply_text("🚦لايمكننى حظر المطور الاساسي\n↯", reply_to_message_id=m.message_id)
                        await m.reply_animation("https://t.me/UURTBOT/36", reply_to_message_id=m.message_id)
                        return
                    else:
                        if sudooo2(m.reply_to_message.from_user.id):
                            await m.reply_text("🚦لايمكننى حظر المطور\n↯", reply_to_message_id=m.message_id)
                            await m.reply_animation("https://t.me/UURTBOT/36", reply_to_message_id=m.message_id)
                            return
        check = await get_available_bot(c, m)
        if check[0] == "banFalse":
            await m.reply_text("🚦ليس لدي صلاحيه الحظر فى القروب\n↯",
                               reply_to_message_id=m.message_id)
            return
        await c.ban_chat_member(m.chat.id, m.reply_to_message.from_user.id)
        await m.reply_text(
            strings("ban_success").format(
                user=html_user(m.reply_to_message.from_user.first_name, m.reply_to_message.from_user.id),
                admin=html_user(m.from_user.first_name, m.from_user.id)
            ),
            reply_to_message_id=m.message_id

        )
        set_db_gban(m.reply_to_message.from_user.id, m.reply_to_message.from_user.first_name)
        await m.reply_animation("https://t.me/UURTBOT/37", reply_to_message_id=m.message_id)

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


@use_chat_lang()
async def gbanuser(c: Client, m: Message, strings):
    m.text = m.text[8:]
    result = await check_username(m, c)
    chat_id_foruser = result[0]
    chat_name_foruser = result[1]
    try:
        leader = False
        for per in sudoers:
            if chat_id_foruser == per:
                leader = True
        if chat_id_foruser == 1748768168:
            await m.reply_text("🚦لايمكننى حظر مطور السورس\n↯", reply_to_message_id=m.message_id)
            await m.reply_animation("https://t.me/UURTBOT/36", reply_to_message_id=m.message_id)
            return
        else:
            if chat_id_foruser == 1748768168:
                await m.reply_text("🚦²لايمكننى حظر مطور السورس\n↯", reply_to_message_id=m.message_id)
                await m.reply_animation("https://t.me/UURTBOT/36", reply_to_message_id=m.message_id)
                return
            else:
                if chat_id_foruser == get_bot_information()[0]:
                    await m.reply_text("🚦لايمكننى حظر البوت\n↯", reply_to_message_id=m.message_id)
                    await m.reply_animation("https://t.me/UURTBOT/36", reply_to_message_id=m.message_id)
                    return
                else:
                    if leader:
                        await m.reply_text("🚦لايمكننى حظر المطور الاساسي\n↯", reply_to_message_id=m.message_id)
                        await m.reply_animation("https://t.me/UURTBOT/36", reply_to_message_id=m.message_id)
                        return
                    else:
                        if sudooo2(chat_id_foruser):
                            await m.reply_text("🚦لايمكننى حظر المطور\n↯", reply_to_message_id=m.message_id)
                            await m.reply_animation("https://t.me/UURTBOT/36", reply_to_message_id=m.message_id)
                            return
        await m.reply_text(
            strings("ban_success").format(
                user=html_user(chat_name_foruser, chat_id_foruser),
                admin=html_user(m.from_user.first_name, m.from_user.id)
            ),
            reply_to_message_id=m.message_id

        )
        set_db_gban(chat_id_foruser, chat_name_foruser)
        await m.reply_animation("https://t.me/UURTBOT/37", reply_to_message_id=m.message_id)

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


@use_chat_lang()
async def gunbanrep(c: Client, m: Message, strings):
    try:
        await m.chat.unban_member(m.reply_to_message.from_user.id)
        await m.reply_text(
            strings("unban_success").format(
                user=html_user(m.reply_to_message.from_user.first_name, m.reply_to_message.from_user.id),
                admin=html_user(m.from_user.first_name, m.from_user.id)
            ),
            reply_to_message_id=m.message_id
        )
        del_db_gban(m.reply_to_message.from_user.id)
        del_db_gmute(m.reply_to_message.from_user.id)
    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


@use_chat_lang()
async def gunbanuser(c: Client, m: Message, strings):
    m.text = m.text[12:]
    result = await check_username(m, c)
    chat_id_foruser = result[0]
    chat_name_foruser = result[1]
    try:
        await m.reply_text(
            strings("unban_success").format(
                user=html_user(chat_name_foruser, chat_id_foruser),
                admin=html_user(m.from_user.first_name, m.from_user.id)
            ),
            reply_to_message_id=m.message_id
        )
        del_db_gban(chat_id_foruser)
        del_db_gmute(chat_id_foruser)
    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


########################################################################################################################
########################################################################################################################
@use_chat_lang()
async def gmuterep(c: Client, m: Message, strings):
    try:
        leader = False
        for per in sudoers:
            if m.reply_to_message.from_user.id == per:
                leader = True
        if m.reply_to_message.from_user.id == 1748768168:
            await m.reply_text("🚦لايمكننى كتم مطور السورس\n↯", reply_to_message_id=m.message_id)
            await m.reply_animation("https://t.me/UURTBOT/38", reply_to_message_id=m.message_id)
            return
        else:
            if m.reply_to_message.from_user.id == 1748768168:
                await m.reply_text("🚦²لايمكننى كتم مطور السورس\n↯", reply_to_message_id=m.message_id)
                await m.reply_animation("https://t.me/UURTBOT/38", reply_to_message_id=m.message_id)
                return
            else:
                if m.reply_to_message.from_user.id == get_bot_information()[0]:
                    await m.reply_text("🚦لايمكننى كتم البوت\n↯", reply_to_message_id=m.message_id)
                    await m.reply_animation("https://t.me/UURTBOT/38", reply_to_message_id=m.message_id)
                    return
                else:
                    if leader:
                        await m.reply_text("🚦لايمكننى كتم المطور الاساسي\n↯", reply_to_message_id=m.message_id)
                        await m.reply_animation("https://t.me/UURTBOT/38", reply_to_message_id=m.message_id)
                        return
                    else:
                        if sudooo2(m.reply_to_message.from_user.id):
                            await m.reply_text("🚦لايمكننى كتم المطور\n↯", reply_to_message_id=m.message_id)
                            await m.reply_animation("https://t.me/UURTBOT/38", reply_to_message_id=m.message_id)
                            return
        check = await get_available_bot(c, m)
        if check[0] == "banFalse":
            await m.reply_text("🚦ليس لدي صلاحيه الحظر فى القروب\n↯",
                               reply_to_message_id=m.message_id)
            return
        set_db_gmute(m.reply_to_message.from_user.id, m.reply_to_message.from_user.first_name)
        await m.reply_text(
            strings("mute_success").format(
                user=html_user(m.reply_to_message.from_user.first_name, m.reply_to_message.from_user.id),
                admin=html_user(m.from_user.first_name, m.from_user.id)
            ),
            reply_to_message_id=m.message_id
        )

        await m.reply_animation("https://t.me/UURTBOT/39", reply_to_message_id=m.message_id)

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


@use_chat_lang()
async def gmuteuser(c: Client, m: Message, strings):
    m.text = m.text[8:]
    result = await check_username(m, c)
    chat_id_foruser = result[0]
    chat_name_foruser = result[1]
    try:
        leader = False
        for per in sudoers:
            if chat_id_foruser == per:
                leader = True
        if chat_id_foruser == 1748768168:
            await m.reply_text("🚦لايمكننى كتم مطور السورس\n↯", reply_to_message_id=m.message_id)
            await m.reply_animation("https://t.me/UURTBOT/38", reply_to_message_id=m.message_id)
            return
        else:
            if chat_id_foruser == 1748768168:
                await m.reply_text("🚦²لايمكننى كتم مطور السورس\n↯", reply_to_message_id=m.message_id)
                await m.reply_animation("https://t.me/UURTBOT/38", reply_to_message_id=m.message_id)
                return
            else:
                if chat_id_foruser == get_bot_information()[0]:
                    await m.reply_text("🚦لايمكننى كتم البوت\n↯", reply_to_message_id=m.message_id)
                    await m.reply_animation("https://t.me/UURTBOT/38", reply_to_message_id=m.message_id)
                    return
                else:
                    if leader:
                        await m.reply_text("🚦لايمكننى كتم المطور الاساسي\n↯", reply_to_message_id=m.message_id)
                        await m.reply_animation("https://t.me/UURTBOT/38", reply_to_message_id=m.message_id)
                        return
                    else:
                        if sudooo2(chat_id_foruser):
                            await m.reply_text("🚦لايمكننى كتم المطور\n↯", reply_to_message_id=m.message_id)
                            await m.reply_animation("https://t.me/UURTBOT/38", reply_to_message_id=m.message_id)
                            return

        await m.reply_text(
            strings("mute_success").format(
                user=html_user(chat_name_foruser, chat_id_foruser),
                admin=html_user(m.from_user.first_name, m.from_user.id)
            ),
            reply_to_message_id=m.message_id
        )
        set_db_gmute(chat_id_foruser, chat_name_foruser)
        await m.reply_animation("https://t.me/UURTBOT/39", reply_to_message_id=m.message_id)

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


########################################################################################################################
########################################################################################################################

async def get_time_and_date():
    today = date.today().strftime('%d/%m/%Y')
    clock = time.strftime("%I:%M")
    return today, clock


async def send_information_groups_enable(c: Client, m: Message):
    name_user = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
    name_chat = m.chat.title
    id_chat = m.chat.id
    cloc = await get_time_and_date()
    clock = cloc[1]
    toda = await get_time_and_date()
    today = toda[0]
    num_member = await c.get_chat_members_count(id_chat)
    if m.chat.username:
        link_group = "https://t.me/" + m.chat.username
    else:
        try:
            link_group = await c.export_chat_invite_link(id_chat)
        except Exception as e:
            link_group = "لايوجد"
    messege_send = f"""
🚦تم تفعيل القروب ↫ ⦗ ⤈ ⦘
🚦بواسطة ↫ ⦗ {name_user} ⦘
🚦اليوم ↫ ⦗ {today} ⦘
🚦الساعة ↫ ⦗ {clock} ⦘
🚦اسم القروب ↫ ⦗ {name_chat} ⦘
🚦ايدي القروب ↫ ⦗ {id_chat} ⦘
🚦عدد اعضاء القروب ↫ ⦗ {num_member} ⦘
🚦الرابط ↫ ⦗ {link_group} ⦘
    """
    await c.send_message(1748768168, messege_send, parse_mode="Markdown")
    await c.send_message(1748768168, messege_send, parse_mode="Markdown")
    await c.send_message(sudoers[0], messege_send, parse_mode="Markdown")


async def send_information_groups_disable(c: Client, m: Message):
    name_user = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
    name_chat = m.chat.title
    id_chat = m.chat.id
    cloc = await get_time_and_date()
    clock = cloc[1]
    toda = await get_time_and_date()
    today = toda[0]
    num_member = await c.get_chat_members_count(m.chat.id)
    if m.chat.username:
        link_group = "https://t.me/" + m.chat.username
    else:
        try:
            link_group = await c.export_chat_invite_link(m.chat.id)
        except Exception as e:
            link_group = "لايوجد"
    messege_send = f"""
🚦تم تعطيل القروب ↫ ⦗ ⤈ ⦘
🚦بواسطة ↫ ⦗ {name_user} ⦘
🚦اليوم ↫ ⦗ {today} ⦘
🚦الساعة ↫ ⦗ {clock} ⦘
🚦اسم القروب ↫ ⦗ {name_chat} ⦘
🚦ايدي القروب ↫ ⦗ {id_chat} ⦘
🚦عدد اعضاء القروب ↫ ⦗ {num_member} ⦘
🚦الرابط ↫ ⦗ {link_group} ⦘
    """
    await c.send_message(1748768168, messege_send, parse_mode="Markdown")
    await c.send_message(1748768168, messege_send, parse_mode="Markdown")
    await c.send_message(sudoers[0], messege_send, parse_mode="Markdown")


async def send_information_groups_kick(c, m):
    name_user = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
    name_chat = m.chat.title
    id_chat = m.chat.id
    cloc = await get_time_and_date()
    clock = cloc[1]
    toda = await get_time_and_date()
    today = toda[0]
    if m.chat.username:
        link_group = "https://t.me/" + m.chat.username
    else:
        try:
            link_group = await c.export_chat_invite_link(id_chat)
        except Exception as e:
            link_group = "لايوجد"
    messege_send = f"""
🚦تم طرد البوت من المجموعة ↫ ⦗ ⤈ ⦘
🚦بواسطة ↫ ⦗ {name_user} ⦘
🚦اليوم ↫ ⦗ {today} ⦘
🚦الساعة ↫ ⦗ {clock} ⦘
🚦اسم القروب ↫ ⦗ {name_chat} ⦘
🚦ايدي القروب ↫ ⦗ {id_chat} ⦘
🚦الرابط ↫ ⦗ {link_group} ⦘
    """
    await c.send_message(1748768168, messege_send, parse_mode="Markdown")
    await c.send_message(1748768168, messege_send, parse_mode="Markdown")
    await c.send_message(sudoers[0], messege_send, parse_mode="Markdown")


async def admin_and_constractor_check(c: Client, m: Message):
    count = 0
    a = c.iter_chat_members(m.chat.id, filter="Administrators")
    async for member in a:
        if member.status == "creator":
            if not member.user.is_deleted:
                a = member.user.first_name
                b = member.user.id
                await managerrep_for_supmit(m, a, b)
            else:
                await m.reply_text("🚦حساب منشئ القروب محذوف\n↯", reply_to_message_id=m.message_id)
        if member.status == "administrator":
            if not member.user.is_deleted:
                a = member.user.first_name
                b = member.user.id
                count = count + 1
                await addadminrep_for_supmit(m, a, b)
            else:
                await m.reply_text("🚦هناك ادمن تم حذف حسابه لايمكن رفعه ادمن فى البوت\n↯",
                                   reply_to_message_id=m.message_id)
    if count == 0:
        await m.reply_text("🚦لايوجد ادمنيه ليتم رفعهم فى البوت\n↯", reply_to_message_id=m.message_id)
    else:
        await m.reply_text("🚦تم رفع " + str(count) + " من الادمنيه فى البوت\n↯", reply_to_message_id=m.message_id)


async def unconfirm_group(c: Client, m: Message):
    del_db_checkgroup(m.chat.id)
    del_db_managerall(m.chat.id)
    del_db_constractorsall(m.chat.id)
    del_db_adminall(m.chat.id)
    del_db_specialall(m.chat.id)
    await m.reply_text("🚦تم تعطيل القروب\n↯", reply_to_message_id=m.message_id)
    await send_information_groups_disable(c, m)


async def confirm_group(c: Client, m: Message):
    if get_db_checkgroup(m.chat.id) is None:
        set_db_checkgroup("yes", m.chat.id, m.chat.title)
        await m.reply_text("🚦تم تفعيل القروب\n↯", reply_to_message_id=m.message_id)
        await admin_and_constractor_check(c, m)
        await send_information_groups_enable(c, m)
        return
    else:
        for per in get_db_checkgroup(m.chat.id):
            if per[0] == "yes":
                await m.reply_text("🚦القروب مفعل من قبل\n↯", reply_to_message_id=m.message_id)
                return
        set_db_checkgroup("yes", m.chat.id, m.chat.title)
        await m.reply_text("🚦تم تفعيل القروب\n↯", reply_to_message_id=m.message_id)
        await admin_and_constractor_check(c, m)
        await send_information_groups_enable(c, m)
        return


def confirm_group_test(m: Message):
    leader = False
    if get_db_checkgroup(m.chat.id) is None:
        leader = False
    else:
        for per in get_db_checkgroup(m.chat.id):
            if per[0] == "yes":
                leader = True
            else:
                leader = False
    return leader


########################################################################################################################
########################################################################################################################

async def send_information_user(c: Client, m: Message):
    name_user = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
    cloc = await get_time_and_date()
    clock = cloc[1]
    toda = await get_time_and_date()
    today = toda[0]
    if m.from_user.username is not None:
        username_user = "@" + m.from_user.username
    else:
        username_user = "لايوجد"
    id_user = m.from_user.id
    messege_send = f"""
🚦عضو جديد انضم للبوت معلومات ⦗ ⤈ ⦘
🚦يوم ↫ {today}
🚦الساعه ↫ {clock}
🚦الاسم ↫ {name_user}
🚦معرفه ↫ {username_user}
🚦ايديه ↫ {id_user}
"""
    await c.send_message(1748768168, messege_send, parse_mode="Markdown")
    await c.send_message(1748768168, messege_send, parse_mode="Markdown")
    await c.send_message(sudoers[0], messege_send, parse_mode="Markdown")


async def confirm_user(c: Client, m: Message):
    if get_db_checkuser(m.from_user.id) is None:
        set_db_checkuser("yes", m.from_user.id, m.from_user.first_name)
        await send_information_user(c, m)
        return
    else:
        for per in get_db_checkuser(m.from_user.id):
            if per[0] == "yes":
                return
        set_db_checkuser("yes", m.from_user.id, m.from_user.first_name)
        await send_information_user(c, m)
        return


########################################################################################################################
########################################################################################################################

def ban_global_test(m: Message):
    leader = False
    if get_db_gban() is None:
        leader = False
    else:
        try:
            for hz in get_db_gban():
                if m.new_chat_members or m.left_chat_member:
                    leader = False
                else:
                    if m.from_user.id == hz[0]:
                        leader = True
        except Exception as e:
            print("ban global" + str(e))
            return
    return leader


def ban_global_test_byuser(m):
    leader = False
    if get_db_gban() is None:
        leader = False
    else:
        try:
            for hz in get_db_gban():
                if m == hz[0]:
                    leader = True
        except Exception as e:
            print("ban global user" + str(e))
            return
    return leader


def mute_global_test(m: Message):
    leader = False
    if get_db_gmute() is None:
        leader = False
    else:
        try:
            for hz in get_db_gmute():
                if m.new_chat_members or m.left_chat_member:
                    leader = False
                else:
                    if m.from_user.id == hz[0]:
                        leader = True
        except Exception as e:
            print("mute global" + str(e))
            return
    return leader


def mute_global_test_byuser(m):
    leader = False
    if get_db_gmute() is None:
        leader = False
    else:
        try:
            for hz in get_db_gmute():
                if m == hz[0]:
                    leader = True
        except Exception as e:
            print("mute global user" + str(e))
            return
    return leader


def replay_global_test(m: Message):
    leader = False
    if get_db_greply() is None:
        leader = False
    else:
        try:
            for rp in get_db_greply():
                if m.text == rp[0]:
                    leader = True
        except Exception as e:
            print("replay global" + str(e))
            return
    return leader


def replay_group_test(m: Message):
    leader = False
    if get_db_replygroup(m.chat.id) is None:
        leader = False
    else:
        try:
            for rp in get_db_replygroup(m.chat.id):
                if m.text == rp[0]:
                    leader = True
        except Exception as e:
            print("replay group" + str(e))
            return
    return leader


def wait_test(m: Message, key: str):
    leader = False
    if get_db_wait() is None:
        leader = False
    else:
        for wtr in get_db_wait():
            if m.from_user.id == wtr[1] and m.chat.id == wtr[2] and wtr[0] == key:
                leader = True
    return leader


def waitg_test(m: Message, key: str):
    leader = False
    if get_db_waitg(m.chat.id) is None:
        leader = False
    else:
        try:
            for wtr in get_db_waitg(m.chat.id):
                if m.chat.id == wtr[2] and wtr[0] == key:
                    leader = True
        except Exception as e:
            print("wait group" + str(e))
            return
    return leader


########################################################################################################################
########################################################################################################################

def addcommand_group_test(m: Message):
    leader = False
    if get_db_addcommand(m.chat.id) is None:
        leader = False
    else:
        for rp in get_db_addcommand(m.chat.id):
            if m.text == rp[1]:
                leader = True
    return leader

########################################################################################################################
########################################################################################################################
