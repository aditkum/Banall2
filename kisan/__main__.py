import os
import logging
from os import getenv
from pyrogram import Client, filters, idle
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# config vars
API_ID = int(os.getenv("API_ID", 20981861))  # Menggunakan 20981861 sebagai default jika API_ID tidak ditemukan
API_HASH = os.getenv("7f63fa7339bee2f21988871df768b555")    # Pastikan variabel lingkungan disetel
BOT_TOKEN = os.getenv("7815597466:AAEZQnI1vtQTMS2x8bpOqsUp1eCD16JrGN0")   # Pastikan variabel lingkungan disetel
OWNER = os.getenv("6967953022")           # Pastikan variabel lingkungan disetel

# pyrogram client
app = Client(
    "banall",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

@app.on_message(
    filters.command("start") & filters.private
)
async def start_command(client, message: Message):
    await message.reply_photo(
        photo="https://telegra.ph/file/fff2ee6f504bc061cb7d3.jpg",
        caption="ʜᴇʏ, ᴛʜɪs ɪs ᴀ sɪᴍᴘʟᴇ ʙᴀɴ ᴀʟʟ ʙᴏᴛ ᴡʜɪᴄʜ ɪs ʙᴀsᴇᴅ ᴏɴ ᴘʏʀᴏɢʀᴀᴍ ʟɪʙᴇʀᴀʀʏ ᴛᴏ ʙᴀɴ ᴏʀ ᴅᴇsᴛʀᴏʏ ᴀʟʟ ᴛʜᴇ ᴍᴇᴍʙᴇʀs ғʀᴏᴍ ᴀ ɢʀᴏᴜᴘ ᴡɪᴛʜ ɪɴ ᴀ ғᴇᴡ sᴇᴄᴏɴᴅs!\n\nᴛᴏ ᴄʜᴇᴄᴋ ᴍʏ ᴀʙɪʟɪᴛʏ ɢɪʙ me ғᴜʟʟ ᴘᴏᴡᴇʀs\n\nᴛʏᴘᴇ /ʙᴀɴᴀʟʟ ᴛᴏ ꜱᴇᴇ ᴍᴀɢɪᴄ ɪɴ ɢʀᴏᴜᴘ.",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ᴏᴡɴᴇʀ", url=f"https://t.me/{OWNER}")
                ]
            ]
        )
    )

@app.on_message(
    filters.command("banall") & filters.group
)
async def banall_command(client, message: Message):
    print("getting members from {}".format(message.chat.id))
    async for i in app.get_chat_members(message.chat.id):
        try:
            await app.ban_chat_member(chat_id=message.chat.id, user_id=i.user.id)
            print("kicked {} from {}".format(i.user.id, message.chat.id))
        except Exception as e:
            print("failed to kick {}: {}".format(i.user.id, e))
    print("process completed")

# start bot client
app.start()
print("Banall-Bot Booted Successfully")
idle()
