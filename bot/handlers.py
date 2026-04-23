import logging

from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

import bot.keyboards as keyboard

router = Router()

MENU_MESSAGE = "Hello! I'm Mirror bot 🤖"

@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    logging.info(f"user_id={message.from_user.id}")
    await message.answer(MENU_MESSAGE, reply_markup=keyboard.main)


# --- Settings ---
@router.callback_query(F.data == "menu_settings")
async def settings_menu(callback: CallbackQuery) -> None:
    await callback.message.edit_text("Settings", reply_markup=keyboard.settings_options)
    await callback.answer()