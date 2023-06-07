import re, asyncio, time, shutil, psutil, os, sys
from pyrogram import Client, filters, enums
from pyrogram.types import *
from info import BOT_START_TIME, ADMINS
from utils import humanbytes  


@Client.on_message(filters.private & filters.command("status") & filters.user(ADMINS))          
async def stats(bot, update):
    currentTime = time.strftime("%Hh%Mm%Ss", time.gmtime(time.time() - BOT_START_TIME))
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent

    ms_g = f"""<b><u>BOT STATUS</b></u>

Uptime: <code>{currentTime}</code>
CPU Usage: <code>{cpu_usage}%</code>
RAM Usage: <code>{ram_usage}%</code>
Total Disk Space: <code>{total}</code>
Used Space: <code>{used} ({disk_usage}%)</code>
Free Space: <code>{free}</code> """

    msg = await bot.send_message(chat_id=update.chat.id, text="__Processing...__", parse_mode=enums.ParseMode.MARKDOWN)         
    await msg.edit_text(text=ms_g, parse_mode=enums.ParseMode.HTML)
   
@Client.on_message(filters.command('logs') & filters.user(ADMINS))
async def log_file(bot, message):
    try:
        await message.reply_document('BotLog.txt')
    except Exception as e:
        await message.reply(str(e))


@Client.on_message(filters.command("restart") & filters.user(ADMINS))
async def stop_button(bot, message):
    msg = await bot.send_message(text="**🔄 𝖲𝗈𝗋𝗋𝗒 𝖬𝖺𝗍𝖾 𝖸𝗈𝗎𝗋𝖾 𝖦𝗈𝗇𝗇𝖺 𝖧𝖺𝗏𝖾 𝖳𝗈 𝖶𝖺𝗂𝗍 𝖠 𝖡𝗂𝗍 𝖨 𝖧𝖺𝗏𝖾 𝖳𝗈 𝖱𝖾𝗌𝗍𝖺𝗋𝗍 𝖬𝗒𝗌𝖾𝗅𝖿 𝖩𝗎𝗌𝗍 𝖠 𝖲𝖾𝖼...**", chat_id=message.chat.id)       
    await asyncio.sleep(3)
    await msg.edit("**✅️ 𝖠𝗅𝗋𝗂𝗀𝗁𝗍 𝖨𝗆 𝖣𝗈𝗇𝖾! 𝖸𝗈𝗎 𝖢𝖺𝗇 𝖴𝗌𝖾 𝖬𝖾 𝖭𝗈𝗐**")
    os.execl(sys.executable, sys.executable, *sys.argv)



