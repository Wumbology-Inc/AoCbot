import logging
from os import environ

from discord.ext import commands

AOCBOT_TOKEN = environ.get("AOCBOT_TOKEN")
log = logging.getLogger(__name__)

if AOCBOT_TOKEN:
    log.info(f"AoCbot token loaded")
else:
    log.error(f"AoCbot token not found in 'AOCBOT_TOKEN' environment variable!")

bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"))

log.info("Start loading extensions from ./bot/cogs/")

if __name__ == "__main__":
    cogs = ["adventofcode"]
    for extension in cogs:
        try:
            bot.load_extension(f"bot.cogs.{extension}")
            log.info(f"Successfully loaded extension: {extension}")
        except Exception:
            log.error(f"Failed to load extension {extension}")

bot.run(AOCBOT_TOKEN)
