from aiogram import Bot, Dispatcher, F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

# All handlers should be attached to the Router (or Dispatcher)
router = Router()

# Command handlers
@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    await message.answer("Hello! I'm Mirror NPC.")

@router.message(Command('help'))
async def cmd_help(message: Message) -> None:
    await message.answer("Command help, there is no help...")

@router.message(F.text == 'Окей')
async def cmd_reply(message: Message) -> None:
    await message.answer("Ага okay okay поговори")