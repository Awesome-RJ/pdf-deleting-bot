import os
import asyncio
from os import getenv

from pyrogram import filters, Client
from pyrogram.types import Message

api_id = 26782911
api_hash = "ba45b57921555f5293691197e2310516"
bot_token = "5977762644:AAFN9heMxFQXgBTLS7sdFutigMeVDix7DUk"

PyroGram = bot_token.split(":")[0]
pgram = Client(
    name=PyroGram,
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token
)
print("Bot starting")

@pgram.on_message(filters.command(["start", f"start@copyrightblockerbot"]))
async def start(client: Client, message: Message) -> None:
    await message.reply("Hello, Bot is Alive✨\n\n made by @Awesome_RJ")

@pgram.on_message(filters.document, group=2)
async def media_files(client: Client, message: Message) -> None:
    await asyncio.sleep(1)
    await message.delete()

pgram.run()
