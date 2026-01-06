import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
load_dotenv()

from config import settings
from app.handlers import router

# All handlers should be attached to the Router (or Dispatcher)

# Polling bot
async def main() -> None:
    bot = Bot(token=settings.BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        logging.basicConfig(
                        level=logging.INFO,
                        stream=sys.stdout
                        )
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot turned off...')