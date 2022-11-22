import os
import asyncio
from os import getenv

from pyrogram import filters, Client

api_id = int(getenv("API_ID"))
api_hash = getenv("API_HASH")
bot_token = getenv("BOT_TOKEN")

PyroGram = bot_token.split(":")[0]
pgram = Client(
    name=PyroGram,
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token,
#    workers=min(32, os.cpu_count() + 4),
#    sleep_threshold=60,
#    in_memory=True,
)
print("Bot starting")

@pgram.on_message(filters.document, group=2)
async def media_files(client, message) -> None:
    await asyncio.sleep(1)
    await message.delete()
    await bot.send_message(message.chat.id, "Alert!\nmedia detected!")

pgram.run()
