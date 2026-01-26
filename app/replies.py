from aiogram import Router, F
from aiogram.types import Message

# All handlers should be attached to the Router (or Dispatcher)
router = Router()

# Random Replies for Links
import random

# Funny reply on окей message
@router.message(F.text == 'окей')
async def cmd_reply(message: Message) -> None:
    await message.answer("Ага okay okay поговори")

# TikTok Links reply 
@router.message(F.text.contains("tiktok.com"))
async def tiktok_reply(message: Message) -> None:
    tiktok_replies = ["Опять говно тиктоки...",
                     "Бесполезную фигню отправил снова с ТикТока",
                     "Ну ты дебил"]
    await message.reply(random.choice(tiktok_replies))

# YouTube Links reply
@router.message(F.text.contains("youtube.com/shorts"))
async def youtube_reply(message: Message) -> None:
    youtube_replies = ["Опять эти ютуб шорты...",
                     "Хватит эти шорты скидывать",
                     "Это бред полный"]
    await message.answer(random.choice(youtube_replies))

# Instagram Reels Links reply
@router.message(F.text.contains("instagram.com/reel/"))
async def insta_reply(message: Message) -> None:
    insta_replies = ["Снова инста рилсы...",
                     "Хватит в инсте сидеть все время",
                     "Перестань тратить время на рилсы"]
    await message.answer(random.choice(insta_replies))