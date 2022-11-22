import os
import asyncio

from pyrogram import filters, Client
from os import getenv

api_id = int(getenv("API_ID"))
api_hash = getenv("API_HASH")
bot_token = getenv("BOT_TOKEN")

PyroGram = bot_token.split(":")[0]
pgram = Client(
    name=PyroGram,
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token
)
print("Bot starting")

@pgram.on_message(filters.photo & filters.video & filters.document, group=2)
async def media_files(client, message) -> None:
    await asyncio.sleep(1)
    await message.delete()

pgram.run()
