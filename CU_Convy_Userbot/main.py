import asyncio
from telethon import TelegramClient
from configs import client
from main_handler import queue_handler


#TODO do the main


async def main():
    await client.start()
    asyncio.create_task(queue_handler())

    me = await client.get_me()
    print(f"🤖 Userbot is running: @{me.username}")
    await client.run_until_disconnected()

if __name__ == '__main__':
    client.loop.run_until_complete(main())