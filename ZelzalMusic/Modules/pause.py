from pyrogram import filters
from pyrogram.types import Message

from ZelzalMusic import app, pytgcalls
from ZelzalMusic.Helpers import admin_check, close_key, is_streaming, stream_off


@app.on_message(filters.command(["pause"]) | filters.command(["كتم","اسكت","ايقاف مؤقت"],prefixes= ["/", "!","","#"]) & filters.group)
@admin_check
async def pause_str(_, message: Message):
    try:
        await message.delete()
    except:
        pass

    if not await is_streaming(message.chat.id):
        return await message.reply_text(
            "- اكتب كمل او /resume عشان يكمل الاغنيه"
        )

    await pytgcalls.pause_stream(message.chat.id)
    await stream_off(message.chat.id)
    return await message.reply_text(
        text=f"- تم ايقاف التشغيل مؤقتاً 🥺\n \n- بواسطة : {message.from_user.mention} .",
        reply_markup=close_key,
    )
