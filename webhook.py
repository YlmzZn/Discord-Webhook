import discord
from discord.ext import commands
import asyncio
import requests
from bs4 import BeautifulSoup
import traceback

bot = commands.Bot(command_prefix="<", intents=discord.Intents.all())

webhook_url = "webhook_url"
website_url = 'website_url'

previous_article_text = ""

async def fetch_updates():
    global previous_article_text
    while True:
        try:
            response = requests.get(website_url, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"})
            
            soup = BeautifulSoup(response.content, 'lxml')

            # You can use another way to catch any text.
            # Watch out the "soup.select('div > ol > li > a')". You have to adjust it with respect to yourself.
            article_text = soup.select('div > ol > li > a')

            # Check the new or old content.
            if article_text != previous_article_text:
                data = {
                    "content": f"# [New notification]({website_url})"
                }

                requests.post(webhook_url, data=data)
                previous_article_text = article_text

        except Exception:
            err = traceback.format_exc()
            print(err)
        
        # Check the website every 5 seconds.
        await asyncio.sleep(5)

@bot.event
async def on_ready():
    print("Bot is ready")
    asyncio.create_task(fetch_updates())

bot.run("token")
