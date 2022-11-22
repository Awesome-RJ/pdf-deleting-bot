import os
import asyncio

from pyrogram import filters, Client
from pyrogram.types import Message
from os import getenv

api_id = int(getenv("API_ID"))
api_hash = getenv("API_HASH")
bot_token = getenv("BOT_TOKEN")

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

@pgram.on_message(filters.photo & filters.video & filters.document)
async def media_files(client: Client, message: Message):
    await asyncio.sleep(1)
    await message.delete()

pgram.run()
