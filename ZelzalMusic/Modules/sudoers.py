from pyrogram import filters
from pyrogram.types import Message

from config import OWNER_ID
from ZelzalMusic import SUDOERS, app


@app.on_message(filters.command(["addsudo"]) | filters.command(["رفع مطور","مط","ترقيه","م"],prefixes= ["/", "!","","#"]) & filters.user(OWNER_ID))
async def sudoadd(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(
                "- قم بالـرد ع الشخـص او اضف اليـوزر او الايـدي لـ الامـر ؟!"
            )
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await app.get_users(user)
        if int(user.id) in SUDOERS:
            return await message.reply_text(f"- {user.mention} هو بالفعل مطور فى البوت.")
        try:
            SUDOERS.add(int(user.id))
            await message.reply_text(f"تم {user.mention} اضافته مطور.")
        except:
            return await message.reply_text("- خطـأ .. حـاول مجـدداً")

    if message.reply_to_message.from_user.id in SUDOERS:
        return await message.reply_text(
            f"- {message.reply_to_message.from_user.mention} هو بالفعل مطور في البوت"
        )
    try:
        SUDOERS.add(message.reply_to_message.from_user.id)
        await message.reply_text(
            f"تم اضافة {message.reply_to_message.from_user.mention} في قائمة المطورين"
        )
    except:
        return await message.reply_text("ғᴀɪʟᴇᴅ ᴛᴏ ᴀᴅᴅ ᴜsᴇʀ ɪɴ sᴜᴅᴏᴇʀs.")


@app.on_message(filters.command(["delsudo", "rmsudo"]) | filters.command(["تك","تنزيل","تنزيل مطور"],prefixes= ["/", "!","","#"]) & filters.user(OWNER_ID))
async def sudodel(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(
                "- قم بالـرد ع الشخـص او اضف اليـوزر او الايـدي لـ الامـر ؟!"
            )
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await app.get_users(user)
        if int(user.id) not in SUDOERS:
            return await message.reply_text(
                f"- {user.mention} ليس في قائمة المطورين"
            )
        try:
            SUDOERS.remove(int(user.id))
            return await message.reply_text(
                f"- إزالة  {user.mention} من قائمة المطورين ."
            )
        except:
            return await message.reply_text(f"- خطـأ .. حـاول مجـدداً")
    else:
        user_id = message.reply_to_message.from_user.id
        if int(user_id) not in SUDOERS:
            return await message.reply_text(
                f"- {message.reply_to_message.from_user.mention} ليس في قائمة المطورين ."
            )
        try:
            SUDOERS.remove(int(user_id))
            return await message.reply_text(
                f"- ليس {message.reply_to_message.from_user.mention} من قائمة المطورين."
            )
        except:
            return await message.reply_text(f"- فشـل .. حـاول مجـدداً.")


@app.on_message(filters.command(["sudolist", "sudoers", "sudo"]) | filters.command(["المطورين","قائمه المطورين"],prefixes= ["/", "!","","#"]))
async def sudoers_list(_, message: Message):
    hehe = await message.reply_text("- جارٍ الحصول على قائمة المطورين...")
    text = "<u>- **المالك :**</u>\n"
    count = 0
    user = await app.get_users(OWNER_ID)
    user = user.first_name if not user.mention else user.mention
    count += 1
    text += f"{count}➤ {user}\n"
    smex = 0
    for user_id in SUDOERS:
        if user_id != OWNER_ID:
            try:
                user = await app.get_users(user_id)
                user = user.first_name if not user.mention else user.mention
                if smex == 0:
                    smex += 1
                    text += "\n<u>- **المساعد :**</u>\n"
                count += 1
                text += f"{count}➤ {user}\n"
            except Exception:
                continue
    if not text:
        await message.reply_text("- لم يتم العثور  على قائمة المطورين .")
    else:
        await hehe.edit_text(text)
