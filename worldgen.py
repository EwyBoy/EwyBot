import discord
from discord.ext import commands


class Worldgen(commands.Cog):
    @commands.group(name='worldgen', invoke_without_command=True)
    async def worldgen(self, ctx):
        """Main command for Worldgen."""
        subcommands = [command.name for command in self.worldgen.commands]
        subcommands_list = '\n'.join([f"• {subcommand}" for subcommand in subcommands])
        await ctx.send(f"Available sub-commands:\n```{subcommands_list}```")

    @worldgen.command(name='nether')
    async def nether(self, ctx):
        """Example 2 command for OreTweaker."""
        file_path = "assets/worldgen/nether.png"
        try:
            with open(file_path, "rb") as file:
                image = discord.File(file)
                await ctx.send(file=image)
        except FileNotFoundError:
            await ctx.send(f"File '{file_path}' not found.")

    @worldgen.group(name='overworld', invoke_without_command=True)
    async def overworld(self, ctx):
        """Main command for Overworld."""
        subcommands = [command.name for command in self.overworld.commands]
        subcommands_list = '\n'.join([f"• {subcommand}" for subcommand in subcommands])
        await ctx.send(f"Available sub-commands:\n```{subcommands_list}```")

    @overworld.command(name='1.16')
    async def v1_16(self, ctx):
        file_path = "assets/worldgen/overworld/1.16.png"
        try:
            with open(file_path, "rb") as file:
                image = discord.File(file)
                await ctx.send(file=image)
        except FileNotFoundError:
            await ctx.send(f"File '{file_path}' not found.")

    @overworld.command(name='1.17')
    async def v1_17(self, ctx):
        file_path = "assets/worldgen/overworld/1.17.png"
        try:
            with open(file_path, "rb") as file:
                image = discord.File(file)
                await ctx.send(file=image)
        except FileNotFoundError:
            await ctx.send(f"File '{file_path}' not found.")

    @overworld.command(name='1.18')
    async def v1_18(self, ctx):
        file_path = "assets/worldgen/overworld/1.18.png"
        try:
            with open(file_path, "rb") as file:
                image = discord.File(file)
                await ctx.send(file=image)
        except FileNotFoundError:
            await ctx.send(f"File '{file_path}' not found.")


async def setup(bot):
    await bot.add_cog(Worldgen())
