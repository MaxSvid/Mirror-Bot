import random
import json
from aiogram import F, Router
from aiogram.types import Message

router = Router()


def load_replies() -> dict:
    try:
        with open("bot/database/replies.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: The file 'replies.json' was not found.")
        return {}
    except PermissionError:
        print("Error: Permission denied, check the file path.")
        return {}
    except OSError as e:
        print(f"Error: OS error: {e}")
        return {}

# Funny reply on окей message
@router.message(F.text.lower() == "окей")
async def reply_okei(message: Message) -> None:
    replies = load_replies()
    await message.reply(random.choice(replies["ok_replies"]))


# TikTok Links reply
@router.message(F.text.contains("tiktok.com"))
async def reply_tiktok(message: Message) -> None:
    replies = load_replies()
    await message.reply(random.choice(replies["tiktok_replies"]))


# YouTube Links reply
@router.message(F.text.contains("youtube.com/shorts"))
async def reply_youtube(message: Message) -> None:
    replies = load_replies()
    await message.reply(random.choice(replies["youtube_replies"]))


# Instagram Reels Links reply
@router.message(F.text.contains("instagram.com/reel/"))
async def reply_instagram(message: Message) -> None:
    replies = load_replies()
    await message.reply(random.choice(replies["insta_replies"]))

