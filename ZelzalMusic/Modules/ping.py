import time
from datetime import datetime

import psutil
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

import config
from ZelzalMusic import BOT_NAME, StartTime, app
from ZelzalMusic.Helpers import get_readable_time


@app.on_message(filters.command("ping") | filters.command(["بنج","البنج"],prefixes= ["/", "!","","#"]))
async def ping_zelzal(_, message: Message):
    hmm = await message.reply_photo(
        photo=config.PING_IMG, caption=f"{BOT_NAME} ⚡"
    )
    upt = int(time.time() - StartTime)
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    start = datetime.now()
    resp = (datetime.now() - start).microseconds / 1000
    uptime = get_readable_time((upt))

    await hmm.edit_text(
        f"""- آلبنج : `{resp}ᴍs`

<b><u>{BOT_NAME} آلحآله :</u></b>

**- مدة التشغيل :** {uptime}
**- الرام :** {mem}
**- وحدة المعالجة المركزية :** {cpu}
**- القرص :** {disk}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("• قنـاة السوࢪس •", url=config.SUPPORT_CHANNEL),
                ],
            ]
        ),
    )
