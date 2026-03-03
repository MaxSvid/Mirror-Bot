import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from dotenv import load_dotenv
load_dotenv()

from app.config import settings
from app.handlers import router as main_router
from app.leaderboard import format_leaderboard, get_weekly_stats
from app.replies import router as replies_router


async def post_weekly_leaderboard(bot: Bot) -> None:
    try:
        stats = await get_weekly_stats()
        text = format_leaderboard(stats)
        await bot.send_message(int(settings.CHAT_ID), text, parse_mode="Markdown")
    except Exception as e:
        logging.error(f"Weekly leaderboard post failed: {e}")


# Polling bot
async def main() -> None:
    bot = Bot(token=settings.BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(main_router)
    dp.include_router(replies_router)

    scheduler = AsyncIOScheduler()
    scheduler.add_job(post_weekly_leaderboard, "cron", day_of_week="mon", hour=9, args=[bot])
    scheduler.start()

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