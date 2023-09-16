from pyrogram import filters
from pyrogram.types import Message

from ZelzalMusic import app, pytgcalls
from ZelzalMusic.Helpers import admin_check, close_key, is_streaming, stream_on


@app.on_message(filters.command(["resume"]) | filters.command(["كمل","الغاء كتم","الغاء الكتم","اتكلم"],prefixes= ["/", "!","","#"]) & filters.group)
@admin_check
async def res_str(_, message: Message):
    try:
        await message.delete()
    except:
        pass

    if await is_streaming(message.chat.id):
        return await message.reply_text("انت موقفني اكتب كمل عشان اشتغل تاني")
    await stream_on(message.chat.id)
    await pytgcalls.resume_stream(message.chat.id)
    return await message.reply_text(
        text=f"- تم استئناف التشغيل 🎧\n \n- بواسطة : {message.from_user.mention} .",
        reply_markup=close_key,
    )
