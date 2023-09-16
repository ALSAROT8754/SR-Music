from ZelzalMusic import zelzaldb


async def put(
    chat_id,
    title,
    duration,
    videoid,
    file_path,
    ruser,
    user_id,
):
    put_f = {
        "title": title,
        "duration": duration,
        "file_path": file_path,
        "videoid": videoid,
        "req": ruser,
        "user_id": user_id,
    }
    get = zelzaldb.get(chat_id)
    if get:
        zelzaldb[chat_id].append(put_f)
    else:
        zelzaldb[chat_id] = []
        zelzaldb[chat_id].append(put_f)
