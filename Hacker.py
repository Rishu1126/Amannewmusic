"""
MIT License

Copyright (c) 2022 LEGEND RAJ

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import os
import glob
import json
import logging
import asyncio
from pytube import YouTube
from youtube_search import YoutubeSearch
from pytgcalls import PyTgCalls, idle
from pytgcalls import StreamType
from pytgcalls.types import Update
from pytgcalls.types import AudioPiped, AudioVideoPiped
from pytgcalls.types.stream import StreamAudioEnded, StreamVideoEnded
from pytgcalls.types import (
    HighQualityAudio,
    HighQualityVideo,
    LowQualityVideo,
    MediumQualityVideo
)
from pyrogram import Client, filters
from pyrogram.raw.base import Update
from pyrogram.errors import UserAlreadyParticipant, UserNotParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, Message
from HackerPlugins.queues import QUEUE, add_to_queue, get_queue, clear_queue, pop_an_item
from HackerPlugins.admin_check import *

bot = Client(
    "Music Stream Bot",
    bot_token = os.environ["6779657648:AAGMt7ibLk1StGURuvqPCfOXCEgk3EHx818"],
    api_id = int(os.environ["25543673"]),
    api_hash = os.environ["4a6a881b368c8a2a03f6426267f55e62"]
)

client = Client(os.environ["BQCuFJG9TZMW-U1FxGQzKa5GXN6GpUAlXQCiwWSL_xrAbGZ3R3U_thlNO6zAqfhZN0EI4w0U3t7OUt_hGZvUfS9LPyJEXt19ikTDIwlESC5oEtlVxkyJm8Zw_x0owXLI2Okh-NQZOgyqDE4YFXWc1qySwXkB9nc8KcXwtAn98A-cHoKpi41nM0fA7SW4s37B7nPm5mk1gNmEsT9tQytc3CsWtR3k6Zc5UEz-Ux4OlYLBJ-KfYVqFoDlwxjKeSWBDvxo84TnjlNjHqm9hAsNwCuhUBtag2aByiEb2LtDVeayyMPeAsKWhFJqAkeJr1Mj9E8QKwmkhl7RcDGCoY1M903jjAAAAAaIrsyYA"], int(os.environ["25543673"]), os.environ["4a6a881b368c8a2a03f6426267f55e62"])

app = PyTgCalls(client)

OWNER_ID = int(os.environ["6587731758"])

BOT_USERNAME = os.environ["Testing01918272bot"]

LIVE_CHATS = []

START_TEXT = """
━━━━━━━━━━━━━━━━━━━━━━━━
🚩🇮🇳 𝙃𝙚𝙡𝙡𝙤, <b>{}</b> 𝙄 𝘼𝙢 𝙎𝙪𝙥𝙚𝙧 𝙁𝙖𝙨𝙩 𝙈𝙪𝙨𝙞𝙘 𝙋𝙡𝙖𝙮𝙚𝙧
𝘽𝙤𝙩 𝙁𝙤𝙧 𝙏𝙚𝙡𝙚𝙜𝙧𝙖𝙢 𝙂𝙧𝙤𝙪𝙥𝙨 𝘼𝙡𝙡𝙤𝙬𝙨 𝙔𝙤𝙪 𝙏𝙤 𝙋𝙡𝙖𝙮 𝙈𝙪𝙨𝙞𝙘 𝘼𝙣𝙙 𝙑𝙞𝙙𝙚𝙤𝙨 𝙊𝙣 𝙂𝙧𝙤𝙪𝙥𝙨 𝙏𝙝𝙧𝙤𝙪𝙜𝙝 𝙏𝙝𝙚 𝙉𝙚𝙬 𝙏𝙚𝙡𝙚𝙜𝙧𝙖𝙢 𝙑𝙞𝙙𝙚𝙤 𝘾𝙝𝙖𝙩𝙨...
┏━━━━━━━━━━━━━━━━━┓
┣★
┣★ 𝘾𝙧𝙚𝙖𝙩𝙤𝙧 : [𝘼𝙈𝘼𝙉](https://t.me/itzamanrajput)
┣★
┣★ 𝙎𝙪𝙥𝙥𝙤𝙧𝙩 : [𝙃𝙀𝙍𝙀](https://t.me/india_chat_00)
┣★
┗━━━━━━━━━━━━━━━━━┛
━━━━━━━━━━━━━━━━━━━━━━━━
"""

START_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("🚩 𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 🚩", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
            InlineKeyboardButton("📝 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬", callback_data="cbcmds"),
            InlineKeyboardButton("🇮🇳 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫", url="https://t.me/itzamanrajput")
        ],
        [
            InlineKeyboardButton("❤️ 𝐒𝐮𝐩𝐩𝐨𝐫𝐭", url="https://t.me/india_chat_00"),
            InlineKeyboardButton("💫  𝐟𝐨𝐫 𝐚𝐧𝐲 𝐡𝐞𝐥𝐩 𝐂𝐨𝐧𝐭𝐚𝐜𝐭", url="https://t.me/itzamanrajput")
        ],
        [
            InlineKeyboardButton("🔥❤️ 𝐒𝐨𝐮𝐫𝐜𝐞 𝐂𝐨𝐝𝐞", url="https://telegra.ph/file/cb2aedcd34865a018235a.jpg")
        ]
    ]
)

BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="• 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 •", url="https://t.me/india_chat_00"),
            InlineKeyboardButton(text="• 𝐎𝐰𝐧𝐞𝐫 •", url="https://t.me/itsamanrajput")
        ]
    ]
)

async def skip_current_song(chat_id):
    if chat_id in QUEUE:
        chat_queue = get_queue(chat_id)
        if len(chat_queue) == 1:
            await app.leave_group_call(chat_id)
            clear_queue(chat_id)
            return 1
        else:
            title = chat_queue[1][0]
            duration = chat_queue[1][1]
            link = chat_queue[1][2]
            playlink = chat_queue[1][3]
            type = chat_queue[1][4]
            Q = chat_queue[1][5]
            thumb = chat_queue[1][6]
            if type == "Audio":
                await app.change_stream(
                    chat_id,
                    AudioPiped(
                        playlink,
                    ),
                )
            elif type == "Video":
                if Q == "high":
                    hm = HighQualityVideo()
                elif Q == "mid":
                    hm = MediumQualityVideo()
                elif Q == "low":
                    hm = LowQualityVideo()
                else:
                    hm = LowQualityVideo()
                await app.change_stream(
                    chat_id, AudioVideoPiped(playlink, HighQualityAudio(), hm)
                )
            pop_an_item(chat_id)
            await bot.send_photo(chat_id, photo = thumb,
                                 caption = f"▶️ <b>𝐍𝐨𝐰 𝐩𝐥𝐚𝐲𝐢𝐧𝐠:</b> [{title}]({link}) | `{type}` \n\n⏳ <b>Duration:</b> {duration}",
                                 reply_markup = BUTTONS)
            return [title, link, type, duration, thumb]
    else:
        return 0


async def skip_item(chat_id, lol):
    if chat_id in QUEUE:
        chat_queue = get_queue(chat_id)
        try:
            x = int(lol)
            title = chat_queue[x][0]
            chat_queue.pop(x)
            return title
        except Exception as e:
            print(e)
            return 0
    else:
        return 0


@app.on_stream_end()
async def on_end_handler(_, update: Update):
    if isinstance(update, StreamAudioEnded):
        chat_id = update.chat_id
        await skip_current_song(chat_id)


@app.on_closed_voice_chat()
async def close_handler(client: PyTgCalls, chat_id: int):
    if chat_id in QUEUE:
        clear_queue(chat_id)
        

async def yt_video(link):
    proc = await asyncio.create_subprocess_exec(
        "yt-dlp",
        "-g",
        "-f",
        "best[height<=?720][width<=?1280]",
        f"{link}",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate()
    if stdout:
        return 1, stdout.decode().split("\n")[0]
    else:
        return 0, stderr.decode()
    

async def yt_audio(link):
    proc = await asyncio.create_subprocess_exec(
        "yt-dlp",
        "-g",
        "-f",
        "bestaudio",
        f"{link}",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate()
    if stdout:
        return 1, stdout.decode().split("\n")[0]
    else:
        return 0, stderr.decode()


@bot.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.answer("Commands Menu")
    await query.edit_message_text(
        f"""🇮🇳 𝐇𝐞𝐥𝐥𝐨 » **𝐋𝐢𝐬𝐭𝐭 𝐎𝐟 𝐀𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 🇮🇳**
» /play (Song Name/Link) - Play Music
» /vplay (video name/link) - Play Video
» /pause - Pause The Song
» /resume - Resume The Song
» /skip - switch to next Song
» /end - Stop The Streaming
» /join - Invite Assistant To Your Group
» /mute - Mute The Assistant On Voice Chat
» /unmute - UnMute The Assistant On Voice Chat
» /playlist - Show You The Playlist
» /restart - Restart The Bot
⚡ __🚩🇮🇳𝗣𝗼𝘄𝗲𝗿𝗲𝗱 𝗕𝘆 𝗔𝗺𝗮𝗻 𝗥𝗮𝗷𝗽𝘂𝘁 🚩🇮🇳__""")


@bot.on_message(filters.command("start") & filters.private)
async def start_private(_, message):
    msg = START_TEXT.format(message.from_user.mention)
    await message.reply_photo(photo="https://telegra.ph/file/b27e6357f421e7dc0eb41.jpg",
                             caption = msg,
                             reply_markup = START_BUTTONS)
    

@bot.on_message(filters.command(["join", "join@{BOT_USERNAME}"]) & filters.group)
async def join_chat(c: Client, m: Message):
    chat_id = m.chat.id
    try:
        invitelink = await c.export_chat_invite_link(chat_id)
        if invitelink.startswith("https://t.me/+"):
            invitelink = invitelink.replace(
                "https://t.me/+", "https://t.me/joinchat/"
            )
            await client.join_chat(invitelink)
            return await client.send_message(chat_id, "✅ 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝐉𝐨𝐢𝐧𝐞𝐝 𝐓𝐡𝐞 𝐜𝐡𝐚𝐭 ")
    except UserAlreadyParticipant:
        return await client.send_message(chat_id, "✅ 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝐀𝐥𝐫𝐞𝐚𝐝𝐲 𝐢𝐧 𝐭𝐡𝐞 𝐂𝐡𝐚𝐭")


@bot.on_message(filters.command("start") & filters.group)
async def start_group(_, message):
    await message.reply_photo(photo="https://telegra.ph/file/b27e6357f421e7dc0eb41.jpg",
                              caption = f"𝐇𝐞𝐥𝐥𝐨 🥰 {message.from_user.mention} 🎧 𝐌𝐮𝐬𝐢𝐜 𝐏𝐥𝐚𝐲𝐞𝐫 𝐈𝐬 𝐑𝐮𝐧𝐧𝐢𝐧𝐠.",
                              reply_markup = BUTTONS)


@bot.on_message(filters.command(["play", "vplay"]) & filters.group)
async def video_play(_, message):
    await message.delete()
    user_id = message.from_user.id
    state = message.command[0].lower()
    try:
        query = message.text.split(None, 1)[1]
    except:
        return await message.reply_text(f"<b>Usage:</b> <code>/{state} [query]</code>")
    chat_id = message.chat.id

    m = await message.reply_text("🔄 𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠...")
    if state == "play":
        damn = AudioPiped
        ded = yt_audio
        doom = "Audio"
    elif state == "vplay":
        damn = AudioVideoPiped
        ded = yt_video
        doom = "Video"
    if "low" in query:
        Q = "low"
    elif "mid" in query:
        Q = "mid"
    elif "high" in query:
        Q = "high"
    else:
        Q = "0"
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        thumb = results[0]["thumbnails"][0]
        duration = results[0]["duration"]
        yt = YouTube(link)
        cap = f"▶️ <b>𝐍𝐨𝐰 𝐏𝐥𝐚𝐲𝐢𝐧𝐠:</b> [{yt.title}]({link}) | `{doom}` \n\n⏳ <b>Duration:</b> {duration}"
        try:
            ydl_opts = {"format": "bestvideo[height<=720]+bestaudio/best[height<=720]"}
            ydl = yt-dlp.YoutubeDL(ydl_opts)
            info_dict = ydl.extract_info(link, download=True)
            p = json.dumps(info_dict)
            a = json.loads(p)
            playlink = a['formats'][1]['manifest_url']
        except:
            ice, playlink = await ded(link)
            if ice == "0":
                return await m.edit("❗️YTDL ERROR !!!")               
    except Exception as e:
        return await m.edit(str(e))
    
    try:
        if chat_id in QUEUE:
            position = add_to_queue(chat_id, yt.title, duration, link, playlink, doom, Q, thumb)
            caps = f"#️⃣ [{yt.title}]({link}) <b>𝐪𝐮𝐞𝐮𝐞𝐝 𝐚𝐭 𝐩𝐨𝐬𝐢𝐭𝐢𝐨𝐧 {position}</b> \n\n⏳ <b>Duration:</b> {duration}"
            await message.reply_photo(thumb, caption=caps, reply_markup=BUTTONS)
            await m.delete()
        else:            
            await app.join_group_call(
                chat_id,
                damn(playlink),
                stream_type=StreamType().pulse_stream
            )
            add_to_queue(chat_id, yt.title, duration, link, playlink, doom, Q, thumb)
            await message.reply_photo(thumb, caption=cap, reply_markup=BUTTONS)
            await m.delete()
    except Exception as e:
        return await m.edit(str(e))


@bot.on_message(filters.command("skip") & filters.group)
@is_admin
async def skip(_, message):
    await message.delete()
    chat_id = message.chat.id
    if len(message.command) < 2:
        op = await skip_current_song(chat_id)
        if op == 0:
            await message.reply_text("☹️ 𝐍𝐨𝐭𝐡𝐢𝐧𝐠 𝐢𝐧 𝐭𝐡𝐞 𝐪𝐮𝐞𝐮𝐞 𝐓𝐨 𝐬𝐤𝐢𝐩.")
        elif op == 1:
            await message.reply_text("🙁 𝐄𝐦𝐩𝐭𝐲 𝐪𝐮𝐞𝐮𝐞, 𝐒𝐭𝐨𝐩𝐩𝐞𝐝 𝐒𝐭𝐫𝐞𝐚𝐦𝐢𝐧𝐠🙁🚩.")
    else:
        skip = message.text.split(None, 1)[1]
        out = "🗑 <b>𝐑𝐞𝐦𝐨𝐯𝐞𝐝 𝐭𝐡𝐞 𝐅𝐨𝐥𝐥𝐨𝐰𝐢𝐧𝐠 𝐒𝐨𝐧𝐠(s) 𝐅𝐫𝐨𝐦 𝐭𝐡𝐞 𝐪𝐮𝐞𝐮𝐞:</b> \n"
        if chat_id in QUEUE:
            items = [int(x) for x in skip.split(" ") if x.isdigit()]
            items.sort(reverse=True)
            for x in items:
                if x == 0:
                    pass
                else:
                    hm = await skip_item(chat_id, x)
                    if hm == 0:
                        pass
                    else:
                        out = out + "\n" + f"<b>#️⃣ {x}</b> - {hm}"
            await message.reply_text(out)
            
            
@bot.on_message(filters.command(["playlist"]) & filters.group)
@is_admin
async def playlist(_, message):
    chat_id = message.chat.id
    if chat_id in QUEUE:
        chat_queue = get_queue(chat_id)
        if len(chat_queue) == 1:
            await message.delete()
            await message.reply_text(
                f"▶️ <b>𝐍𝐨𝐰 𝐏𝐥𝐚𝐲𝐢𝐧𝐠:</b> [{chat_queue[0][0]}]({chat_queue[0][2]}) | `{chat_queue[0][4]}`",
                disable_web_page_preview=True,
            )
        else:
            out = f"<b>📃 𝐏𝐥𝐚𝐲𝐞𝐫 𝐪𝐮𝐞𝐮𝐞:</b> \n\n▶️ <b>𝐍𝐨𝐰 𝐏𝐥𝐚𝐲𝐢𝐧𝐠:</b> [{chat_queue[0][0]}]({chat_queue[0][2]}) | `{chat_queue[0][4]}` \n"
            l = len(chat_queue)
            for x in range(1, l):
                title = chat_queue[x][0]
                link = chat_queue[x][2]
                type = chat_queue[x][4]
                out = out + "\n" + f"<b>#️⃣ {x}</b> - [{title}]({link}) | `{type}` \n"
            await message.reply_text(out, disable_web_page_preview=True)
    else:
        await message.reply_text("🙁 𝐍𝐨𝐭𝐡𝐢𝐧𝐠 𝐢𝐬 𝐏𝐥𝐚𝐲𝐢𝐧𝐠.")
    

@bot.on_message(filters.command("end") & filters.group)
@is_admin
async def end(_, message):
    await message.delete()
    chat_id = message.chat.id
    if chat_id in QUEUE:
        await app.leave_group_call(chat_id)
        clear_queue(chat_id)
        await message.reply_text("⏹ 𝐒𝐭𝐨𝐩𝐞𝐝 𝐒𝐭𝐫𝐞𝐚𝐦𝐢𝐧𝐠❤️🚩.")
    else:
        await message.reply_text("🙁 𝐍𝐨𝐭𝐡𝐢𝐧𝐠 𝐢𝐬 𝐏𝐥𝐚𝐲𝐢𝐧𝐠.")
        

@bot.on_message(filters.command("pause") & filters.group)
@is_admin
async def pause(_, message):
    await message.delete()
    chat_id = message.chat.id
    if chat_id in QUEUE:
        try:
            await app.pause_stream(chat_id)
            await message.reply_text("⏸ 𝐏𝐚𝐮𝐬𝐞𝐝 𝐒𝐭𝐫𝐞𝐚𝐦𝐢𝐧𝐠.")
        except:
            await message.reply_text("🙁 𝐍𝐨𝐭𝐡𝐢𝐧𝐠 𝐢𝐬 𝐩𝐥𝐚𝐲𝐢𝐧𝐠.")
    else:
        await message.reply_text("🙁 𝐍𝐨𝐭𝐡𝐢𝐧𝐠 𝐢𝐬 𝐏𝐥𝐚𝐲𝐢𝐧𝐠.")
        
        
@bot.on_message(filters.command("resume") & filters.group)
@is_admin
async def resume(_, message):
    await message.delete()
    chat_id = message.chat.id
    if chat_id in QUEUE:
        try:
            await app.resume_stream(chat_id)
            await message.reply_text("⏸ 𝐑𝐞𝐬𝐮𝐦𝐞𝐝 𝐒𝐭𝐫𝐞𝐚𝐦𝐢𝐧𝐠.")
        except:
            await message.reply_text("🙁 𝐍𝐨𝐭𝐡𝐢𝐧𝐠 𝐢𝐬 𝐏𝐥𝐚𝐲𝐢𝐧𝐠.")
    else:
        await message.reply_text("🙁 𝐍𝐨𝐭𝐡𝐢𝐧𝐠 𝐢𝐬 𝐏𝐥𝐚𝐲𝐢𝐧𝐠.")
        
        
@bot.on_message(filters.command("mute") & filters.group)
@is_admin
async def mute(_, message):
    await message.delete()
    chat_id = message.chat.id
    if chat_id in QUEUE:
        try:
            await app.mute_stream(chat_id)
            await message.reply_text("🔇 𝐌𝐮𝐭𝐞𝐝 𝐒𝐭𝐫𝐞𝐚𝐦𝐢𝐧𝐠.")
        except:
            await message.reply_text("🙁 𝐍𝐨𝐭𝐡𝐢𝐧𝐠 𝐢𝐬 𝐏𝐥𝐚𝐲𝐢𝐧𝐠.")
    else:
        await message.reply_text("🙁 𝐍𝐨𝐭𝐡𝐢𝐧𝐠 𝐢𝐬 𝐏𝐥𝐚𝐲𝐢𝐧𝐠.")
        
        
@bot.on_message(filters.command("unmute") & filters.group)
@is_admin
async def unmute(_, message):
    await message.delete()
    chat_id = message.chat.id
    if chat_id in QUEUE:
        try:
            await app.unmute_stream(chat_id)
            await message.reply_text("🔊 𝐔𝐧𝐦𝐮𝐭𝐞𝐝 𝐒𝐭𝐫𝐞𝐚𝐦𝐢𝐧𝐠.")
        except:
            await message.reply_text("🙁 𝐍𝐨𝐭𝐡𝐢𝐧𝐠 𝐢𝐬 𝐏𝐥𝐚𝐲𝐢𝐧𝐠.")
    else:
        await message.reply_text("🙁 𝐍𝐨𝐭𝐡𝐢𝐧𝐠 𝐢𝐬 𝐏𝐥𝐚𝐲𝐢𝐧𝐠.")
        
        
@bot.on_message(filters.command("restart"))
async def restart(_, message):
    user_id = message.from_user.id
    if user_id != OWNER_ID:
        return
    await message.reply_text("🛠 <i>𝐑𝐞𝐬𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐌𝐮𝐬𝐢𝐜 𝐏𝐥𝐚𝐲𝐞𝐫...</i>")
    os.system(f"kill -9 {os.getpid()} && python3 app.py")
            

app.start()
bot.run()
idle()
