from telethon import TelegramClient


# They can be found here: https://my.telegram.org
api_id = 'thy_api_id'
api_hash = 'thy_api_hash'

with TelegramClient('my_session', api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message('me', 'Userbot starterd'))

my_own_account = True #if you're using a dedicated account write 'False'

DOWNLOAD_DIR = 'video_cache' # edit the dir here

placeholder_video_path = 'video_cache/_placeholder.MP4'