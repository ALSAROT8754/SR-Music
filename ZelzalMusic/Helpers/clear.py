from ZelzalMusic import zelzaldb
from ZelzalMusic.Helpers import remove_active_chat


async def _clear_(chat_id):
    try:
        zelzaldb[chat_id] = []
        await remove_active_chat(chat_id)
    except:
        return
