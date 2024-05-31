import asyncio
import os
import requests
import pyrogram
from pyrogram import Client, filters, emoji
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified
from MatrixMusic import app
from config import OWNER_ID, LOGGER_ID


@app.on_message(command(["الاوامر","اوامر"]))
async def zdatsr(client: Client, message: Message):
    usr = await client.get_users(OWNER_ID)
    name = usr.first_name
    usrnam = usr.username
    await message.reply_photo(
        photo=f"https://t.me/c/2136629772/3",
        caption=f"""
↯︙ {usrnam}مرحباً بك عزيزي \n<b>↯︙استخدم الازرار بالاسفل\nٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆\nღ ل- تصفح اوامر البوت ⇣
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◍ اوامر التشغيل ◍", callback_data="zzzll"),
                ],[
                    InlineKeyboardButton(
                        "◍ اوامر القناة ◍", callback_data="zzzch"),
                    InlineKeyboardButton(
                        "◍ اوامر الادمن ◍", callback_data="zzzad"),
                ],[
                    InlineKeyboardButton(
                        "◍ اوامر المطور ◍", callback_data="zzzdv"),
                ],[
                    InlineKeyboardButton(name, url=f"https://t.me/{usrnam}"),
                ],[
                    InlineKeyboardButton(
                        " َٰ𝚂ُِ𝙾ِّ𝚄ٓ𝚁ٍّ𝙲ٍ𝙴 ٍ𝙴ٓ𝚁ٓ𝚁ُِ𝙾ٓ𝚁 ", url="https://t.me/JOE_Ch"),
                ],
            ]
        ),
    )


