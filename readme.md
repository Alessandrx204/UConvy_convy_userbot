
## 💕 UConvy – Your Webm-to-MP4 Bot 🎀

Because every .webm deserves a glow-up ✨

 Welcome to UConvy, a Telegram userbot I made as a self-project while learning Python 🐍
(Yes, I’m just 3 months in – not so proud but thriving! 👩‍💻🌸)

UConvy takes your .webm videos and lovingly turns them into .mp4s and resends them as previews – smoother, prettier, and more compatible with all Telegram clients across OSs.
Think of it as your digital video fairy godmother. Just drop a .webm, and poof – it’s MP4 time! 🎬✨

⸻

🎀 IMPORTANT: Safety First!!

Before we dive into anything technical, here’s a super serious and sparkly PSA:

✨ PLEASE use this bot only from a dedicated Telegram account!!
Otherwise, it might reply to every .webm in every chat – even that one group full of weirdos from 10 years ago 😱
Telegram and group admins may see this as spammy behaviour and restrict or ban your account.

So:
	•	📱 Use a secondary phone number or a VOIP number
	•	❌ Don’t run this from your main account, ok babe? 💋

This is a fun-learning project – not a spam bot. We do not condone bad bot behaviour! 🙅‍♀️

⸻

✨ What Does UConvy Do?

Here’s the cute lil’ routine when you send a .webm:
	1.	Notices your message
	2.	📝 Adds the video to a JSON to-do list (a queue!)
	3.	🎞️ Downloads the video
	4.	🪄 Converts it to .mp4 using FFmpeg
	5.	📤 Uploads the converted video as a reply
	6.	🧹 Deletes all temp files

⸻

🗂 Project Files Explained (Technical)

File	What it Does ✨
main_handler.py	The core fairy. Listens to messages, queues tasks, coordinates the magic.
file_converter.py	The actual magic wand – calls FFmpeg for the video glow-up.
waitlist.py	Keeps track of videos waiting to be converted.
configs.py	Where secrets live (Telegram API keys, paths). Keep it safe 🔐
test.py	A sweet bonus to check if your bot is alive 💬


⸻

💖 How Do I Make It Work? (Beginner Girlie Deep Dive)

💌 Step 1: Listening for Messages

Uses Telethon:

@client.on(events.NewMessage(incoming=True))

Checks if the message has a .webm, then adds it to the queue (with sender’s ID).

⸻

⏳ Step 2: The Waitlist Queue

Defined in waitlist.py.
A while True loop runs in the background, checking for tasks.

⸻

📥 Step 3: Downloading the Video

await event.download_media(file=download_path)

Saves as raw_video.webm in your defined folder (DOWNLOAD_DIR).

⸻

🧙‍♀️ Step 4: Video Conversion

FFmpeg does the real work:

ffmpeg -i raw_video.webm -c:v libx264 converted_video.mp4

Before that, ffprobe checks resolution:

ffprobe -show_entries stream=width,height -of csv=p=0

Handled in file_converter.py. Sets audio, scales, and aspect ratio 💖

⸻

📤 Step 5: Upload the Final Video

Replies to your original message:

await client.edit_message(chat_id, placeholder, text="Here’s your converted video 🎥", file=output_path)


⸻

🧼 Step 6: Clean-Up

Deletes both original .webm and .mp4 to save storage 🌸

⸻

🛠 How to Set It Up

Step-by-step for beginner babes 💕
	1.	✅ Install Python 3.8+
	2.	✅ Install dependencies:

pip install -r requirements.txt

	3.	✅ Install FFmpeg
	•	macOS: brew install ffmpeg
	•	Linux: sudo apt install ffmpeg
	•	Windows: Download from ffmpeg.org
	4.	✅ Get Telegram API credentials from my.telegram.org
Save them in configs.py:

api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
DOWNLOAD_DIR = 'downloads/'
placeholder_video_path = 'placeholder.mp4'

	5.	✅ Run the bot:

python main_handler.py

It’ll log in via Telegram and then it’s live!

⸻

💬 How do i use Uconvy?
	•	Send a .webm to the bot (or to a chat with the bot)
	•	It’ll reply with a placeholder (“Uploading…”)
	•	When done, it’ll replace it with the converted .mp4
	•	Enjoy 🎀

⸻

🧸 Troubleshooting

Issue	What to Do
No reply from bot	Make sure you’re logged in and running the script
Video didn’t convert	Check terminal logs – maybe try a smaller file
Bot replying everywhere	❌ Stop it immediately! Use a dedicated account only


⸻

💕 Future Ideas
	•	Support for more formats (.mov maybe?)
	•	Add a UI or command list?
	•	Count how many videos were converted
	•	Optional support for commands by others 👀

⸻

🎀 Final Words

This project is:
	•	My first serious Python self-project 💕
	•	Built with love, curiosity, and lots of Googling
	•	A mix of learning async code, Telegram bots, and subprocess handling
	•	Proof that even if you’re just starting – you can make magic 🌟

Thanks for checking it out!
Feel free to ⭐ star it, fork it, or just say hi 💌

⸻

Love,
alessandrx & UConvy 🌸
🧚‍♀️ .webm ➜ .mp4 with sparkle and love

⸻

ReadMe made with ChatGPT aid only because I’m terrible at explaining stuff lol 😅

credits:
music of the placeholder video: 
shushubobo - (song name)
[no copyright music] (https://youtu.be/7PvYu-1iEbY)
