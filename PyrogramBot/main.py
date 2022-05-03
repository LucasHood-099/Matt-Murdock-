from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config API_ID, API_HASH, BOT_TOKEN
import random

Nandhu=Client(
    "Pyrogram Bot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)


ALL_PIC = [
 "https://telegra.ph/file/6cff45eb89df1648be888.jpg",
 "https://telegra.ph/file/c283bf783cc9ba943949d.jpg",
 "https://telegra.ph/file/3ac4981982a84f8599030.jpg",
 "https://telegra.ph/file/a8c47c80387d02ed58eaf.jpg"
]


@Nandhu.on_message(filters.command("start")) 
async def start_message(bot, message):
    await message.reply_photo(
        photo=random.choice(ALL_PIC),
        caption=f""" 𝙃𝙞 {message.from_user.mention} 𝙞'𝙢 𝙖 𝙬𝙤𝙧𝙠 𝙞𝙣 𝙥𝙧𝙤𝙜𝙧𝙚𝙨𝙨 𝙗𝙤𝙩 𝙩𝙝𝙞𝙨 𝙗𝙤𝙩 𝙬𝙞𝙡𝙡 𝙗𝙚 𝙖𝙘𝙩𝙞𝙫𝙚 𝙨𝙤𝙤𝙣 𝙥𝙡𝙚𝙖𝙨𝙚 𝙟𝙤𝙞𝙣 𝙤𝙪𝙧 𝙢𝙖𝙞𝙣 𝙘𝙝𝙖𝙣𝙣𝙚𝙡 𝙖𝙣𝙙 𝙜𝙧𝙤𝙪𝙥.

❓ WHICH ARE THE COMMANDS? ❓
Press /help to see all the commands and how they work!
https://t.me/Uncanny_Movies01 """,
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("➕𝖠𝖣𝖣 𝖳𝖮 𝖸𝖮𝖴𝖱 𝖦𝖱𝖮𝖴𝖯➕", url=f"https://t.me/LucasHood099_Bot?startgroup=true")
            ],[
            InlineKeyboardButton("𝖧𝖾𝗅p⚙️", url="t.me/LucasHood_099"),
            InlineKeyboardButton("𝖢𝗈𝗇𝗍𝖺𝖼𝗍 𝖴𝗌💬", url="t.me/LucasHood_099")
            ],[
            InlineKeyboardButton("𝖦𝗋𝗈𝗎𝗉👥", url="https://t.me/Uncanny_Group"),
            InlineKeyboardButton("𝖢𝗁𝖺𝗇𝗇𝖾𝗅📎", url="t.me/Uncanny_Movies01")
            ]]
            )
        )


@Nandhu.on_message(filters.command("help")) 
async def help_message(bot, message):
    await message.reply_text(
        text="Help ഒന്നും ഇല്ല ഓടിക്കോ......"
        )


@Nandhu.on_message(filters.command("video")) 
async def video_message(bot, message):
    await message.reply_video(
        video="https://telegra.ph/file/3453d9d55866422f3fbbf.mp4",
        )



@Nandhu.on_message(filters.command("demo"))
async def demo(bot, msg):
    text = f"""
First Name - {msg.from_user.first_name} 
Last Name - {msg.from_user.last_name} 
UserName - {msg.from_user.username} 
Id - {msg.from_user.id} 
Mention - {msg.from_user.mention}"""

    await msg.reply_text (text=text)



Nandhu.run()
