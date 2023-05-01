import os
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@bot.command()
async def ping(ctx):
    """Check the bot's latency."""
    await ctx.send(f"Pong! Latency: {round(bot.latency * 1000)}ms")


@bot.event
async def on_ready():
    try:
        await bot.load_extension('oretweaker')  # Load the OreTweaker extension
        await bot.load_extension('worldgen')  # Load the Worldgen extension
    except Exception as e:
        print(f"Failed to load extension 'oretweaker': {e}")
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name="!help"
        )
    )
    print(f"Bot connected as {bot.user.name}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    bot.run(os.getenv("secret"))
