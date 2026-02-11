import asyncio
import os
from bot import Bot
from pyrogram import idle

BOT_TOKENS = []

for key, value in os.environ.items():
    if key.startswith("BOT_TOKEN") and value:
        BOT_TOKENS.append(value)

if not BOT_TOKENS:
    raise ValueError("No BOT_TOKEN variables found.")

bots = []

for index, token in enumerate(BOT_TOKENS, start=1):
    bots.append(Bot(bot_token=token, session_name=f"Bot_{index}"))

async def main():
    for bot in bots:
        await bot.start()

    print("All bots started.")

    await idle()   # 🔥 THIS IS CRITICAL

    for bot in bots:
        await bot.stop()

asyncio.run(main())
