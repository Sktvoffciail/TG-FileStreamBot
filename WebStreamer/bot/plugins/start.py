# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

from pyrogram import filters
from pyrogram.types import Message
from WebStreamer.bot import StreamBot


@StreamBot.on_message(filters.command(["start"]))
async def start(_, m: Message):
    await m.reply(
        f'Hello send or send any video, document, file, audio we will upload on our website and give you the link\n Powered By Jdisk.in'
    )
