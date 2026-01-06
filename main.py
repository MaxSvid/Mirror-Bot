import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command


from dotenv import load_dotenv

from config import settings

load_dotenv()

bot = Bot(token=settings.BOT_TOKEN)
# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()

# Command handler
@dp.message()
async def command_start_handler(message: Message) -> None:
    await message.answer("Hello! I'm a bot created with aiogram.")

async def main() -> None:
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        logging.basicConfig(level=logging.INFO,
                        stream=sys.stdout)
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot shut down')