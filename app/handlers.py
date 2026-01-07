from aiogram import Bot, Dispatcher, F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

# Idea for different replies options
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.state import FSMContext

import app.keyboards as keyboard
import logging

# All handlers should be attached to the Router (or Dispatcher)
router = Router()

# FSM
class Overall():
    pass

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

# Gemini menu options, 
@router.message(F.text == 'GeminiAI')
async def gemini_menu(message: Message) -> None:
    await message.answer('Chat with Agent', reply_markup=keyboard.gemini_options)

# This function is an incoming callback query from a callback button in an inline keyboard
@router.callback_query(F.data == 'gemini_chat')
async def gemini_chat(callback: CallbackQuery) -> None:
    await callback.answer('Chat with Agent')
