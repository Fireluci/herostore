import asyncio
import config
from bot import Bot

# Auto collect BOT_TOKEN1, BOT_TOKEN2, etc.
BOT_TOKENS = []

for attr in dir(config):
    if attr.startswith("BOT_TOKEN"):
        token = getattr(config, attr)
        if token:
            BOT_TOKENS.append(token)

if not BOT_TOKENS:
    raise ValueError("No BOT_TOKEN variables found in config.py")

bots = []

for index, token in enumerate(BOT_TOKENS, start=1):
    bots.append(Bot(bot_token=token, session_name=f"Bot_{index}"))


async def main():
    for bot in bots:
        await bot.start()

    await asyncio.Event().wait()


asyncio.run(main())
