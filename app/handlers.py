from aiogram import Bot, Dispatcher, F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

import app.keyboards as keyboard
import logging

# All handlers should be attached to the Router (or Dispatcher)
router = Router()

# Command handlers
@router.message(CommandStart())
async def cmd_start(message: Message) -> None:

    user_id = message.from_user.id
    logging.info(f"user_id={user_id}")

    await message.answer("Hello! I'm Mirror NPC.🤖", 
                         reply_markup=keyboard.main)

@router.message(Command('help'))
async def cmd_help(message: Message) -> None:
    await message.answer("Command help, there is no help...")

@router.message(F.text == 'Окей')
async def cmd_reply(message: Message) -> None:
    await message.answer("Ага okay okay поговори")

# Gemini menu options
@router.message(F.text == 'GeminiAI')
async def gemini_menu(message: Message) -> None:
    await message.answer('Testing options keyboard', reply_markup=keyboard.gemini_options)