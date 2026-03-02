import logging

from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

import app.keyboards as keyboard
from job_reports.reports import fetch_djinni_jobs, format_jobs_message

router = Router()

MENU_MESSAGE = "Hello! I'm Mirror bot"


@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    logging.info(f"user_id={message.from_user.id}")
    await message.answer(MENU_MESSAGE, reply_markup=keyboard.main)


@router.message(Command("help"))
async def cmd_help(message: Message) -> None:
    await message.answer("Available commands: /start, /help, /clear")


@router.message(Command("clear"))
async def cmd_clear(message: Message) -> None:
    await message.answer("Menu cleared.", reply_markup=None)


@router.callback_query(F.data == "menu_back")
async def menu_back(callback: CallbackQuery) -> None:
    await callback.message.edit_text(MENU_MESSAGE, reply_markup=keyboard.main)
    await callback.answer()


# --- Job Reports ---

@router.callback_query(F.data == "reports_menu")
async def reports_menu(callback: CallbackQuery) -> None:
    await callback.message.edit_text("Job Report Options", reply_markup=keyboard.reports_options)
    await callback.answer()


@router.callback_query(F.data == "dev_reports")
async def dev_reports(callback: CallbackQuery) -> None:
    await callback.message.edit_text("Fetching developer jobs from Djinni...")
    try:
        jobs = await fetch_djinni_jobs(limit=10)
        text = format_jobs_message(jobs, source="Djinni")
    except Exception as e:
        logging.error(f"Scraper error: {e}")
        text = "Failed to fetch jobs. Try again later."
    await callback.message.edit_text(
        text,
        reply_markup=keyboard.back_button,
        parse_mode="Markdown",
        disable_web_page_preview=True,
    )
    await callback.answer()


@router.callback_query(F.data == "dsa_reports")
async def dsa_reports(callback: CallbackQuery) -> None:
    await callback.message.edit_text("DS/DA reports coming soon.", reply_markup=keyboard.back_button)
    await callback.answer()


@router.callback_query(F.data == "uk_reports")
async def uk_reports(callback: CallbackQuery) -> None:
    await callback.message.edit_text("UK job reports coming soon.", reply_markup=keyboard.back_button)
    await callback.answer()


# --- Games ---

@router.callback_query(F.data == "menu_games")
async def games_menu(callback: CallbackQuery) -> None:
    await callback.message.edit_text("Play Tic-Tac-Toe", reply_markup=keyboard.game_options)
    await callback.answer()


@router.callback_query(F.data == "newgame_command")
async def start_new_tictactoe_game(callback: CallbackQuery, state: FSMContext) -> None:
    await callback.answer("Game starting... (not implemented yet)")


# --- Settings ---

@router.callback_query(F.data == "menu_settings")
async def settings_menu(callback: CallbackQuery) -> None:
    await callback.message.edit_text("Settings", reply_markup=keyboard.settings_options)
    await callback.answer()
