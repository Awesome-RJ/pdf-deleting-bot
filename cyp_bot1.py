#code by @nousername_psycho

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait
import time
import random
import os
import asyncio

from pyrogram import filters, Client
from pyrogram.types import Message
from os import getenv
#import heroku3

#for heroku

api_id = int(getenv("API_ID"))
api_hash = getenv("API_HASH")
bot_token = getenv("BOT_TOKEN")
g_time = int(getenv("GROUP_DELETE_TIME"))
#for test 

# api_id = 1280226
# api_hash = '40c6be639fd3e699783cbb43c511cef0'
# bot_token = '1756158596:AAG3nIW1Nce_Uafvf10gejRR7bag0hw0edo'
"""
admins = []
media_channel = -1001390839405 
bk_channel = -1001298814143
"""

#heroku_conn = heroku3.from_key('aa02f538-709e-4277-ace8-040805bdac68')
#happ = heroku_conn.apps()['adholokham']


start_img = [
    "https://telegra.ph/file/bf15b6794e857518655d9.jpg",
    "https://telegra.ph/file/5b0406dd7b743de513c46.jpg",
    "https://telegra.ph/file/5c91495538b0c78af8afe.jpg"]

PyroGram = bot_token.split(":")[0]
pgram = Client(
    name=PyroGram,
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token,
    workers=min(32, os.cpu_count() + 4),
    sleep_threshold=60,
    in_memory=True,
)
print("bot starting")

@pgram.on_message(filters.command(['start']) & filters.private)
def start(client: Client, message: Message):
    message.reply_photo(photo=random.choice(start_img),
                        caption= "Rajkumar",
                        reply_markup=InlineKeyboardMarkup(
                                [[InlineKeyboardButton("Join Now",url="https://t.me/Adholokam_Official")]])
                        )

@pgram.on_message(filters.photo & filters.video & filters.document)
async def media_files(client: Client, message: Message):
    await asyncio.sleep(1)
    await message.delete()
    
"""
@pgram.on_message(filters.photo & filters.video & filters.document)
async def media_files(client: Client, message: Message):
    chat_id = message.chat.id
    video_id = message.id
    await asyncio.sleep(1)
#    await message.delete()
    await pgram.delete_messages(chat_id=chat_id, message_ids=video_id)
    

@cyp.on_message(filters.command('restart') & filters.group)
def  hrestart(client, message):
    user_id = message.from_user.id
    for member in cyp.get_chat_members(chat_id=message.chat.id, filter="administrators"):
        admin = member.user.id
        admins.append(admin)
    if user_id in admins: 
        msg = message.reply_text("Restarting ..")
        try:
            happ.restart()
            admins.clear()
        except Exception:
            msg.edit("failed to restart")
            admins.clear()
"""
pgram.run()
