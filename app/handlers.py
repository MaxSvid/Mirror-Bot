from aiogram import Bot, Dispatcher, F, Router, types
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup   # Finite State Machine
from aiogram.fsm.context import FSMContext

import app.keyboards as keyboard
import logging

# Gemini Itegration 
from app.ai.chat import npc_agent_reply

# All handlers should be attached to the Router (or Dispatcher)
router = Router()

# FSM
class NPCState(StatesGroup):
    waiting_for_msg = State()

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

# ------- CHANGING FROM GEMINI TO LLAMA llama/chat.py -------

# Llama AI menu: this function is an incoming callback query from a callback button in an inline keyboard
@router.callback_query(F.data == 'menu_llama')
async def gemini_menu(callback: CallbackQuery) -> None:
    await callback.message.edit_text(
        'Chat with Agent',
        reply_markup=keyboard.gemini_options,
        parse_mode="Markdown"
        )
    await callback.answer()

# Gemini Start Chat callback
@router.callback_query(F.data == 'llama_chat')
async def start_gemini_chat(callback: CallbackQuery, state: FSMContext) -> None:
    # Set the user into NPC state
    await state.set_state(NPCState.waiting_for_msg)
    
    await callback.message.edit_text(
        "**NPC Chat Mode: ON**\n\nI'm ready. Talk to me! \n(Type 'exit' or click 'Back' to stop)",
        reply_markup=keyboard.back_button, # Use your back button here
        parse_mode="Markdown"
    )
    await callback.answer()

# NEW: Handle text while in NPC state
@router.message(NPCState.waiting_for_msg)
async def handle_npc_messages(message: Message, state: FSMContext, bot: Bot):
    # Check if user wants to quit
    if message.text.lower() in ["exit", "stop", "back"]:
        await state.clear()
        await message.answer("NPC: Goodbye! Back to the main menu.", reply_markup=keyboard.main)
        return

    # Show typing indicator
    await bot.send_chat_action(chat_id=message.chat.id, action="typing")
    
    try:
        # Get NPC response from Gemini
        npc_response = await npc_agent_reply(message.text)
        
        # Send response to user
        await message.answer(
            f"🤖 NPC Agent:\n\n{npc_response}",
            reply_markup=keyboard.back_button
        )
    except Exception as e:
        logging.error(f"Error processing NPC message: {e}")
        await message.answer(
            "Sorry, something went wrong. Please try again or check code.",
            reply_markup=keyboard.back_button
        )

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


