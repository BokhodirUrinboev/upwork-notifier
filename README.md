# Upwork Job Notifier for Telegram

This is a Python script that periodically sends job listings from Upwork to a specified Telegram channel. Each job listing is sent as a message with a clickable "View Job" button using the Telegram Bot API and the aiogram library.

## Features

- Periodically fetches job listings from Upwork RSS feeds.
- Sends job listings as Telegram messages with inline buttons for easy access.
- Supports multiple job categories (e.g., React, HTML/CSS).

## Prerequisites

Before using this script, you'll need to:

1. Create a Telegram bot using [BotFather](https://core.telegram.org/bots#botfather) and obtain the bot token.

2. Identify the Telegram chat ID where you want to send job listings. You can use a personal chat or create a dedicated channel or group for this purpose.

3. Set up the necessary environment variables in a `.env` file with the following variables:

   - `TELEGRAM_BOT_TOKEN`: Your Telegram bot token.
   - `TELEGRAM_CHAT_ID`: Your Telegram chat ID.
   - `UPWORK_RSS_REACT_URL`: The Upwork RSS feed URL for the React category.
   - `UPWORK_RSS_HTML_CSS_URL`: The Upwork RSS feed URL for the HTML/CSS category.
