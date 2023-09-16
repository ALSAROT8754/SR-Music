import asyncio

import speedtest
from pyrogram import filters

from ZelzalMusic import SUDOERS, app


def testspeed(m):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = m.edit("**⇆ جارٍ تشغيل اختبار سرعة التنزيل...**")
        test.download()
        m = m.edit("**⇆ تشغيل اختبار سرعة التحميل...**")
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit("**↻ مشاركة نتائج اختبار السرعة...**")
    except Exception as e:
        return m.edit(e)
    return result


@app.on_message(filters.command(["speedtest", "spt"]) | filters.command(["فحص","السرعة","السرعه","سرعه","سرعة"],prefixes= ["/", "!","","#"]) & SUDOERS)
async def speedtest_function(_, message):
    m = await message.reply_text("**- تشغيل اختبار السرعة...**")
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, testspeed, m)
    output = f"""✯ **نتائج اختبار سرعه البوت ** ✯
    
<u>**- عميل :**</u>
**- مزود خدمة الإنترنت :** {result['client']['isp']}
**- الدولة :** {result['client']['country']}
  
<u>**- سيرفر :**</u>
**- الاسم :** {result['server']['name']}
**- الدولة :** {result['server']['country']}, {result['server']['cc']}
**- راعي :** {result['server']['sponsor']}
**- وقت الإستجابة :** {result['server']['latency']}  
**- البنج :** {result['ping']}"""
    msg = await app.send_photo(
        chat_id=message.chat.id, photo=result["share"], caption=output
    )
    await m.delete()
