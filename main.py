import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
load_dotenv()

from bot.config import settings
from bot.handlers import router as main_router
from bot.replies import router as replies_router

# Polling bot
async def main() -> None:
    bot = Bot(token=settings.BOT_TOKEN, parse_mode = "HTML")
    dp = Dispatcher()

    dp.include_router(main_router)
    dp.include_router(replies_router)

    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        logging.info("Starting running bot...")
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot turned off...")