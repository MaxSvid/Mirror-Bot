from aiogram import Bot, Dispatcher, F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

# Idea for different replies options
from aiogram.fsm.state import State, StatesGroup
#from aiogram.fsm.state import FSMContext

import app.keyboards as keyboard
import logging

# All handlers should be attached to the Router (or Dispatcher)
router = Router()

# FSM
class Overall():
    pass

# Command handlers
MENU_MESSAGE = "Hello! I'm Mirror NPC bot🤖"

@router.message(CommandStart())
async def cmd_start(message: Message) -> None:

    user_id = message.from_user.id
    logging.info(f"user_id={user_id}")

    await message.answer(MENU_MESSAGE, reply_markup=keyboard.main)
    
@router.callback_query(F.data == 'menu_back')
async def menu_back(callback: CallbackQuery) -> None:
    # shows main menu buttons, no need to change the message text
    await callback.message.edit_text(MENU_MESSAGE, reply_markup=keyboard.main)
    await callback.answer()

@router.message(Command('help'))
async def cmd_help(message: Message) -> None:
    await message.answer("Command help, there is no help lox xx")

# Clear command to add for shutting down menu
@router.message(Command('clear'))
async def cmd_clear(message: Message) -> None:
    await message.answer("It will clear something, not sure what yet...")

# Funny reply
@router.message(F.text == 'окей')
async def cmd_reply(message: Message) -> None:
    await message.answer("Ага okay okay поговори")

# Gemini menu: this function is an incoming callback query from a callback button in an inline keyboard
@router.callback_query(F.data == 'menu_gemini')
async def gemini_menu(callback: CallbackQuery) -> None:
    await callback.message.edit_text(
        'Chat with Agent',
        reply_markup=keyboard.gemini_options
        )
    await callback.answer()

# Job reports menu:
@router.callback_query(F.data == 'reports_menu')
async def settings_reports(callback: CallbackQuery) -> None:
    await callback.message.edit_text(
        'Job Report/Search Options',
        reply_markup=keyboard.reports_options
        )
    await callback.answer()

# Crypto alerts menu:
@router.callback_query(F.data == 'menu_alerts')
async def settings_reports(callback: CallbackQuery) -> None:
    await callback.message.edit_text(
        'Crypto prices and DeFi Updates',
        reply_markup=keyboard.alerts_options
        )
    await callback.answer()

# Setting menu
@router.callback_query(F.data == 'menu_settings')
async def settings_menu(callback: CallbackQuery) -> None:
    await callback.message.edit_text(
        'Avaliable Settings',
        reply_markup=keyboard.settings_options
        )
    await callback.answer()


