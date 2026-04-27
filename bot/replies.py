import random
import json
import os
from aiogram import F, Router
from aiogram.types import Message

router = Router()

# Loading JSON file function
def load_replies():
    pass

# Funny reply on окей message
@router.message(F.text == "окей")


# TikTok Links reply
@router.message(F.text.contains("tiktok.com"))


# YouTube Links reply
@router.message(F.text.contains("youtube.com/shorts"))


# Instagram Reels Links reply
@router.message(F.text.contains("instagram.com/reel/"))

