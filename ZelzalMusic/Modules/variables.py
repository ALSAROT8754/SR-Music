from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import Message

import config
from ZelzalMusic import BOT_NAME, app


@app.on_message(
    filters.command(["config", "variables"]) | filters.command(["الاكواد","الفارات","الايبيات","كونفج"],prefixes= ["/", "!","","#"]) & filters.user(config.OWNER_ID)
)
async def get_vars(_, message: Message):
    try:
        await app.send_message(
            chat_id=int(config.OWNER_ID),
            text=f"""<u>**{BOT_NAME} ᴄᴏɴғɪɢ ᴠᴀʀɪᴀʙʟᴇs :**</u>

**ايبي ايدي :** `{config.API_ID}`
**ايبي هاش :** `{config.API_HASH}`

**توكن البوت :** `{config.BOT_TOKEN}`
**حد المدة :** `{config.DURATION_LIMIT}`

**ايدي المالك :** `{config.OWNER_ID}`
**سودو يوزر :** `{config.SUDO_USERS}`

**بنج :** `{config.PING_IMG}`
**بدأ :** `{config.START_IMG}`
**قنـاة السوࢪس :** `{config.SUPPORT_CHANNEL}`

**الجلسة :** `{config.SESSION}`""",
            disable_web_page_preview=True,
        )
    except:
        return await message.reply_text("- فشل في إرسال متغيرات التكوين .")
    if message.chat.type != ChatType.PRIVATE:
        await message.reply_text(
            "- ᴘʟᴇᴀsᴇ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴘᴍ, ɪ'ᴠᴇ sᴇɴᴛ ᴛʜᴇ ᴄᴏɴғɪɢ ᴠᴀʀɪᴀʙʟᴇs ᴛʜᴇʀᴇ."
        )
