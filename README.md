# Anime & Multporn Bot

A Telegram bot that provides anime information and can scrape images from Multporn.net. This bot combines two functionalities:

1. **Anime Information**: Get details about anime titles with different quality and format options
2. **Multporn Image Scraper**: Send a Multporn.net URL to get all images from that page

## Features

- Search for anime information using AniList API
- Select quality options (480p, 720p, 1080p)
- Choose between different format templates (Otaku, Hanime)
- Fetch and download images from Multporn.net
- User authorization system

## Deployment on Render.com

This bot is ready to be deployed on Render.com as a web service.

### Prerequisites

You need the following for the bot to function:
- Telegram Bot Token (from @BotFather)
- Telegram API ID and API Hash

### How to deploy

1. Fork/Clone this repository
2. Create a new Web Service on Render.com
3. Connect your GitHub repository
4. Set the environment variables:
   - `API_ID`: Your Telegram API ID
   - `API_HASH`: Your Telegram API Hash
   - `BOT_TOKEN`: Your Telegram Bot Token
5. Deploy the service

### Environment Variables

Configure these in the Render dashboard:

| Variable | Description |
|----------|-------------|
| API_ID | Telegram API ID (numeric) |
| API_HASH | Telegram API Hash (string) |
| BOT_TOKEN | Telegram Bot Token from BotFather |

## Usage

### Commands

- `/start` - Start the bot
- `/anime` - Begin anime search process

### Anime Search Flow

1. Send `/anime` command
2. Send the anime name
3. Select the desired quality
4. Choose a format template (Otaku or Hanime)
5. Receive formatted anime information with image

### Multporn Image Scraping

1. Send a URL from multporn.net
2. Wait for the bot to fetch and send all images

## Authorization

The bot is restricted to authorized users only. Default authorized users:
- 1557539460
- 6667553516

## Maintenance

If you need to modify the allowed users, you'll need to update the `ALLOWED_USERS` set in the code.
