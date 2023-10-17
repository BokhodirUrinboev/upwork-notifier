import asyncio
import logging
import sys
from os import getenv
from aiogram import Bot, types
import feedparser
from aiogram.enums import ParseMode
from dotenv import load_dotenv

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

load_dotenv()

# Retrieve environment variables
BOT_TOKEN = str(getenv("TELEGRAM_BOT_TOKEN"))
TELEGRAM_CHAT_ID = getenv("TELEGRAM_CHAT_ID")
UPWORK_RCC_FIGMA_TO_WEBSITE_URL = str(getenv("UPWORK_RCC_FIGMA_TO_WEBSITE_URL"))
UPWORK_RSS_REACT_URL = str(getenv("UPWORK_RSS_REACT_URL"))
UPWORK_RSS_HTML_CSS_URL = str(getenv("UPWORK_RSS_HTML_CSS_URL"))

bot = Bot(BOT_TOKEN, parse_mode=ParseMode.MARKDOWN)


async def send_job_listings(category_name, rss_url):
    # Parse the Upwork RSS feed
    feed = feedparser.parse(rss_url)

    # Loop through the feed entries and send job listings to Telegram
    for entry in feed.entries:
        job_title = entry.title
        job_link = entry.link

        inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="View Job", url=job_link)]])

        # Customize the message format as per your preferences
        message = f"🚀 New {category_name} job on Upwork 🚀\n Title: {job_title}\n 🔗 [View Job]({job_link})"

        # Send the message with the inline button
        await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message,
                               reply_markup=inline_keyboard)
        break

# Define a periodic job to fetch and send job listings


async def periodic_job():
    while True:
        await send_job_listings("Figma to Website", UPWORK_RCC_FIGMA_TO_WEBSITE_URL)
        await send_job_listings("React", UPWORK_RSS_REACT_URL)
        await send_job_listings("HTML/CSS", UPWORK_RSS_HTML_CSS_URL)
        await asyncio.sleep(60)  # Repeat every hour (adjust the interval as needed)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    loop = asyncio.get_event_loop()
    loop.create_task(periodic_job())

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
