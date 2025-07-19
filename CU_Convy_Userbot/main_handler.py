import asyncio
import os
import waitlist
from telethon import events

import file_converter
from configs import client, DOWNLOAD_DIR, placeholder_video_path

#incoming=True,
@client.on(events.NewMessage(incoming=True))
async def handler(event):
    print("Caught incoming message:", event.text)

    if event.file and event.file.name: #yep it's needed this way idk why
        file_name = event.file.name.lower()
        if file_name.endswith('.webm'):
            print("Caught incoming webm file:", event.text)
            chat_id = event.chat_id
            user_id = event.sender_id
            waitlist.add_user(chat_id,user_id, event.id)
            print("Caught outgoing message:", user_id, event.id)


async def queue_handler():
    # Infinite loop: keeps checking for new tasks forever
    while True:
        #  get the next item from the waitlist (a queue of tasks)
        # Each item is a tuple (user_id, message_id)
        values = waitlist.pop_da_next()

        # If the queue has any value and we got a task
        if values:
            chat_id, user_id, message_id = values  # Extract the user's ID
            # and the message ID to process

            try:
                # Use the Telethon client to fetch the original message object
                # using chat ID and message ID
                msg = await client.get_messages(chat_id, ids=message_id)

                # If the message was successfully identified(msg has any value)
                if msg:
                    # Reply to that message with _placeholder video
                    placeholder_obj = await msg.reply("Uploading...", file=placeholder_video_path)

                    # Call the file download and conversion function,
                    # passing the message and the placeholder
                    await process_the_file(msg, placeholder_obj)

            except Exception as e:
                # If something fails (e.g., message fetch, reply, or conversion),
                # prints the error to console
                print(f"Processing error {message_id}: {e}")

        else:
            # If no task was found, wait 1 second before checking again
            # to avoid tight looping
            await asyncio.sleep(1)












async def process_the_file(event, placeholder):
    webm_video = 'raw_video.webm'
    mp4_video = 'converted_video.mp4'
    download_path = os.path.join(DOWNLOAD_DIR, webm_video)
    output_path = os.path.join(DOWNLOAD_DIR, mp4_video)


    await event.download_media(file=download_path)

    returncode = await file_converter.Converter.webm2mp4(download_path, output_path)
    try:
        if returncode == 0:
            file2b_sent = output_path


            chat_id = event.chat_id

            await client.edit_message(chat_id, placeholder,text="Here’s your converted video 🎥", file=file2b_sent)


        else:
            print('something went wrong')
            await placeholder.edit("❌ Conversion failed.")


    except Exception as e:
            await event.reply(f'Something went wrong: {e}')
    finally:
        os.remove(download_path)
        os.remove(output_path)







