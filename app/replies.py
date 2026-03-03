import logging
import random

from aiogram import F, Router
from aiogram.types import Message

from app.database.connection import get_connection

router = Router()


async def record_link(user_id: int, username: str | None, link_type: str) -> None:
    try:
        async with await get_connection() as conn:
            await conn.execute(
                "INSERT INTO link_stats (user_id, username, link_type) VALUES (%s, %s, %s)",
                (user_id, username, link_type),
            )
    except Exception as e:
        logging.error(f"Failed to record link stat: {e}")


# Funny reply on окей message
@router.message(F.text == "окей")
async def cmd_reply(message: Message) -> None:
    await message.answer("Ага okay okay поговори")


# TikTok Links reply
@router.message(F.text.contains("tiktok.com"))
async def tiktok_reply(message: Message) -> None:
    tiktok_replies = [
        "Опять говно тиктоки...",
        "Бесполезную фигню отправил снова с ТикТока",
        "Ну ты дебил",
    ]
    await message.reply(random.choice(tiktok_replies))
    await record_link(message.from_user.id, message.from_user.username, "tiktok")


# YouTube Links reply
@router.message(F.text.contains("youtube.com/shorts"))
async def youtube_reply(message: Message) -> None:
    youtube_replies = [
        "Опять эти ютуб шорты...",
        "Хватит эти шорты скидывать",
        "Это бред полный",
    ]
    await message.answer(random.choice(youtube_replies))
    await record_link(message.from_user.id, message.from_user.username, "youtube_shorts")


# Instagram Reels Links reply
@router.message(F.text.contains("instagram.com/reel/"))
async def insta_reply(message: Message) -> None:
    insta_replies = [
        "Снова инста рилсы...",
        "Хватит в инсте сидеть все время",
        "Перестань тратить время на рилсы",
    ]
    await message.answer(random.choice(insta_replies))
    await record_link(message.from_user.id, message.from_user.username, "instagram")
