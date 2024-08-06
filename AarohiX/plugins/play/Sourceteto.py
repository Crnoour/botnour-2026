import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AarohiX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AarohiX import app
from random import  choice, randint

                
@app.on_message(
    command(["سورس","السورس"])
    
)
async def huhh(client: Client, message: Message):
    await message.reply_video(
        video=f"https://te.legra.ph/file/d04bea15f20fb094a047c.mp4",
        caption=f"""⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "{مـطور السـورس}", url=f"https://t.me/M_9_T"), 
                 InlineKeyboardButton(
                   "{مـساعد المـطور}",       url=f"https://t.me/N_7_K"), 
                 
             ],[ 
            InlineKeyboardButton(
                        "{قـناه السـورس}", url=f"https://t.me/vzo_a"), 
                   
             ],[ 
                  InlineKeyboardButton(
                text="اضغط لاضافتي لمجموعتك⚡",
                url=f"https://t.me/{app.username}?startgroup=true"),
                ],

            ]

        ),

    )








@app.on_message(
    command(["المطور نور"])
    
    
)
async def yas(client, message):
    usr = await client.get_chat("M_9_T")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"معلومات مطور السورس\n\n‍ ¦➻ 𝐍𝐀𝐌𝐄 :{name}\n\n ¦➻ 𝐔𝐒𝐄𝐑 :@{usr.username}\n\n ¦➻ 𝐈𝐃 :`{usr.id}`\n\n ¦➻ 𝐁𝐎𝐈 :{usr.bio}\n\nســورس ميــوزك العـالم", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["حكم" , "نور","مبرمج السورس"])
    
    
)
async def yas(client, message):
    usr = await client.get_chat("M_9_T")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"معلومات مطور السورس.\n\n¦➻ 𝐍𝐀𝐌𝐄 :{name}\n\n ¦➻ 𝐔𝐒𝐄𝐑 :@{usr.username}\n\n ¦➻ 𝐈𝐃 :`{usr.id}`\n\n ¦➻ 𝐁𝐎𝐈 :{usr.bio}\n\nسـورس مـيوزك العـالم", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )



@app.on_message(
    command(["مطور السورس" , "الحاكم","احمد"])
    
    
)
async def yas(client, message):
    usr = await client.get_chat("N_7_K")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"معلومات مبرمج السورس.\n\n¦➻ 𝐍𝐀𝐌𝐄 :{name}\n\n ¦➻ 𝐔𝐒𝐄𝐑 :@{usr.username}\n\n ¦➻ 𝐈𝐃 :`{usr.id}`\n\n ¦➻ 𝐁𝐎𝐈 :{usr.bio}\n\nسـورس مـيوزك الـعالم", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )



