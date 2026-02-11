import asyncio
import os
import config
from bot import Bot

BOT_TOKENS = []

# 1️⃣ Collect from config.py
for attr in dir(config):
    if attr.startswith("BOT_TOKEN"):
        token = getattr(config, attr)
        if token:
            BOT_TOKENS.append(token)

# 2️⃣ Collect from environment variables (Koyeb)
for key, value in os.environ.items():
    if key.startswith("BOT_TOKEN"):
        BOT_TOKENS.append(value)

# Remove duplicates
BOT_TOKENS = list(set(BOT_TOKENS))

if not BOT_TOKENS:
    raise ValueError("No BOT_TOKEN variables found in config or environment.")

bots = []

for index, token in enumerate(BOT_TOKENS, start=1):
    bots.append(Bot(bot_token=token, session_name=f"Bot_{index}"))

async def main():
    for bot in bots:
        await bot.start()

    await asyncio.Event().wait()

asyncio.run(main())
