import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
load_dotenv()

from app.config import settings
# All handlers or replies should be attached to the Router (or Dispatcher)
from app.handlers import router as main_router
from app.replies import router as replies_router

# Polling bot
async def main() -> None:
    bot = Bot(token=settings.BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(main_router)
    dp.include_router(replies_router)

    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        logging.basicConfig(
                        level=logging.INFO,
                        stream=sys.stdout
                        )
        logging.info('Running Mirror Bot...')
        asyncio.run(main())
        print('Running Mirror Bot...')
    except KeyboardInterrupt:
        print('Bot turned off...')