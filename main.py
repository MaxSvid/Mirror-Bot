import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
load_dotenv()

from app.config import settings
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
        logging.info('Running Mirror Bot...')
        asyncio.run(main())
        print('Running Mirror Bot...')
    except KeyboardInterrupt:
        print('Bot turned off...')