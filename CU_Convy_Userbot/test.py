from telethon import events
from configs import client, my_own_account


me = client.get_me()
username = me.username


@client.on(events.NewMessage(incoming=True, outgoing=True))
async def handler(event):
    if my_own_account == False: # otherwise your account may act as a bot
        sender = await event.get_sender
        senderID = sender.id
        senderUSRNM = sender.username
        if f"@{username}" in event.raw_text:
            if event.out:  # outgoing
                await event.edit(f" @{username}bot is online!")
            else:  # incoming
                await event.reply(f'{senderUSRNM}[{senderID}] was so gentle to check if i was all good. thanks for asking <3, yes I am')

