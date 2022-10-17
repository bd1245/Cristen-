import os
import sys
from datetime import datetime
from time import time
from pyrogram import Client, filters
from pyrogram.types import Message
from config import HNDLR, SUDO_USERS
from Miq.helpers.decorators import authorized_users_only

START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (    ("Minggu", 60 * 60 * 24 * 7),    ("Hari", 60 * 60 * 24),    ("Jam", 60 * 60),    ("Menit", 60),    ("Detik", 1),)
async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else ""))
    return ", ".join(parts)


@Client.on_message(    filters.user(SUDO_USERS) & filters.command(["ريستارت"], prefixes=f"{HNDLR}"))
@authorized_users_only

async def restart(client, m: Message):
    await m.delete()
    loli = await m.reply("1")
    await loli.edit("2")
    await loli.edit("3")
    await loli.edit("4")
    await loli.edit("5")
    await loli.edit("6")
    await loli.edit("7")
    await loli.edit("8")
    await loli.edit("9")
    await loli.edit("**✅ تم اعاده تشغيل بوت كرستين**")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()
@Client.on_message(filters.user(SUDO_USERS) & filters.command(["اوامر","اوامر كرستين"], prefixes=f"{HNDLR}"))
@authorized_users_only
async def help(client, m: Message):
    await m.delete()
    HELP = f"""
<b>👋 اهلا {m.from_user.mention}!

𝘰𝘳𝘥𝘦𝘳𝘴 ς.ᖇ ຮ๏ʊᖇς℮
✛┈┉━｢ ᥴ.𝘳 𝘴ꪮꪊ𝘳ᥴꫀ ｣━┅┈✛

👉 | لتشغيل صوتية في المكالمة أرسل ⇦ [ `{HNDLR}شغل  + اسم الاغنيه + او الرابط من يوتيوب` ]
👉 | لتشغيل فيديو في المكالمة  ⇦ [ `{HNDLR}تشغيل_فيديو  + اسم الاغنيه + او الرابط من اليوتيوب` ]
✛┈┉━｢ ᥴ.𝘳 𝘴ꪮꪊ𝘳ᥴꫀ ｣━┅┈✛

👉 | لأيقاف الصوت او الفيديو مؤقتآ  ⇦ [ `{HNDLR}اسكت` ] 
👉 | لأعاده تشغيل الصوت ⇦  [ `{HNDLR}اسكت_كمل` ]
👉 | لأيقاف الصوت  ⇦ [ `{HNDLR}اسكت` ] 
✛┈┉━｢ ᥴ.𝘳 𝘴ꪮꪊ𝘳ᥴꫀ ｣━┅┈✛

👉 | لتحميل صوتية أرسل ⇦ [ `{HNDLR}تحميل + اسم الاغنيه او الرابط` ]
👉 | لتحميل فيديو  ⇦  [ `{HNDLR}تحميل_فيديو + اسم الاغنيه او الرابط` ]
✛┈┉━｢ ᥴ.𝘳 𝘴ꪮꪊ𝘳ᥴꫀ ｣━┅┈✛

👉 | لأعاده تشغيل السورس  ⇦  [ `{HNDLR}ريستارت` ]
✛┈┉━｢ ᥴ.𝘳 𝘴ꪮꪊ𝘳ᥴꫀ ｣━┅┈✛
 مطور سورس كرستين  : @wjj_u 
قناة السورس:  @cr_source"""
    await m.reply(HELP)
@Client.on_message(filters.command(["الريبو"], prefixes=f"{HNDLR}"))
async def repo(client, m: Message):
    await m.delete()
    REPO = f"""
<b>👋  اهلا {m.from_user.mention}!
- للمطور : @wjj_u 
@cr_source 
"""
    await m.reply(REPO, disable_web_page_preview=True)
