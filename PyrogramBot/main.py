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
 "https://telegra.ph/file/0cc1f6fdae2105c199fd0.jpg",
 "https://telegra.ph/file/947a16fb2c4e150d5ef7c.jpg",
 "https://telegra.ph/file/e6ba07f722e4a172a3bc5.jpg",
 "https://telegra.ph/file/a29fcc91c946e7d6ce34e.jpg"
]


@Nandhu.on_message(filters.command("start")) 
async def start_message(bot, message):
    await message.reply_photo(
        photo=random.choice(ALL_PIC),
        caption=f""" ๐๐ {message.from_user.mention} ๐'๐ข ๐ ๐ฌ๐ค๐ง๐  ๐๐ฃ ๐ฅ๐ง๐ค๐๐ง๐๐จ๐จ ๐๐ค๐ฉ ๐ฉ๐๐๐จ ๐๐ค๐ฉ ๐ฌ๐๐ก๐ก ๐๐ ๐๐๐ฉ๐๐ซ๐ ๐จ๐ค๐ค๐ฃ ๐ฅ๐ก๐๐๐จ๐ ๐๐ค๐๐ฃ ๐ค๐ช๐ง ๐ข๐๐๐ฃ ๐๐๐๐ฃ๐ฃ๐๐ก ๐๐ฃ๐ ๐๐ง๐ค๐ช๐ฅ.

โ WHICH ARE THE COMMANDS? โ
Press /help to see all the commands and how they work!
https://t.me/Uncanny_Movies01 """,
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("โ๐ ๐ฃ๐ฃ ๐ณ๐ฎ ๐ธ๐ฎ๐ด๐ฑ ๐ฆ๐ฑ๐ฎ๐ด๐ฏโ", url=f"https://t.me/LucasHood099_Bot?startgroup=true")
            ],[
            InlineKeyboardButton("๐ง๐พ๐pโ๏ธ", url="t.me/LucasHood_099"),
            InlineKeyboardButton("๐ข๐๐๐๐บ๐ผ๐ ๐ด๐๐ฌ", url="t.me/LucasHood_099")
            ],[
            InlineKeyboardButton("๐ฆ๐๐๐๐๐ฅ", url="https://t.me/Uncanny_Group"),
            InlineKeyboardButton("๐ข๐๐บ๐๐๐พ๐๐", url="t.me/Uncanny_Movies01")
            ]]
            )
        )


@Nandhu.on_message(filters.command("help")) 
async def help_message(bot, message):
    await message.reply_text(
        text="Help เดเดจเตเดจเตเด เดเดฒเตเดฒ เดเดเดฟเดเตเดเต......"
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
