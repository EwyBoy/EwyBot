import discord
from discord.ext import commands


class OreTweaker(commands.Cog):
    @commands.group(name='oretweaker', aliases=['ot'], invoke_without_command=True)
    async def oretweaker(self, ctx):
        """Main command for OreTweaker."""
        subcommands = [command.name for command in self.oretweaker.commands]
        subcommands_list = '\n'.join([f"• {subcommand}" for subcommand in subcommands])
        await ctx.send(f"Available sub-commands:\n```{subcommands_list}```")

    @oretweaker.command(name='info', aliases=['information'])
    async def info(self, ctx):
        """Info command for OreTweaker."""
        await ctx.send(
            "OreTweaker is a mod for Minecraft Forge that allows you to modify the ore generation of "
            "Minecraft."
        )

    @oretweaker.command(name='wiki', aliases=['docs', 'documentation'])
    async def wiki(self, ctx):
        """Wiki command for OreTweaker."""
        await ctx.send("https://github.com/EwyBoy/OreTweaker/wiki")

    @oretweaker.command(name='download', aliases=['dl', 'downloads'])
    async def download(self, ctx):
        """Download command for OreTweaker."""
        await ctx.send("https://legacy.curseforge.com/minecraft/mc-mods/ore-tweaker/files/all")

    @oretweaker.command(name='source', aliases=['src', 'github'])
    async def source(self, ctx):
        """Source command for OreTweaker."""
        await ctx.send("https://github.com/EwyBoy/OreTweaker")

    @oretweaker.command(name='json', aliases=['jsons', 'format', 'formats', 'formatting', 'malformed'])
    async def json(self, ctx):
        """JSON command for OreTweaker."""
        await ctx.send("https://github.com/EwyBoy/OreTweaker/wiki/Validating-JSON-File")

    @oretweaker.command(name='distribution', aliases=['dist'])
    async def distribution(self, ctx):
        """Distribution command for OreTweaker."""
        file_path = "assets/distribution.png"
        text = """\
            Vanilla Minecraft's Distribution is showed here:
            
            - Triangle represents sideways pyramids. *(More likely to spawn in the center between your minY and maxY)*
            
            - Uniform represents square towers. *(Uniform distribution between minY and maxY)*
            """

        try:
            with open(file_path, "rb") as file:
                image = discord.File(file)
                embed = discord.Embed(description=text)
                embed.set_image(url=f"attachment://{file_path}")
                await ctx.send(file=image, embed=embed)

        except FileNotFoundError:
            await ctx.send(f"Image file '{file_path}' not found.")

    @oretweaker.group(name='example', aliases=['examples'], invoke_without_command=True)
    async def example(self, ctx):
        """Example command for OreTweaker."""
        await ctx.send("Available sub-commands:\n```2\n3```")

    @example.command(name='2', aliases=['ot2', 'oretweaker2', 'oretweaker 2', 'ore-tweaker2', 'ore-tweaker 2', '1.16'])
    async def example_2(self, ctx):
        """Example 2 command for OreTweaker."""
        file_path = "examples/ot2.json"
        try:
            with open(file_path, "r") as file:
                json_data = file.read()
            code_block = f"```json\n{json_data}\n```"
            await ctx.send(code_block)
        except FileNotFoundError:
            await ctx.send(f"File '{file_path}' not found.")

    @example.command(name='3', aliases=['ot3', 'oretweaker3', 'oretweaker 3', 'ore-tweaker3', 'ore-tweaker 3', '1.18'])
    async def example_3(self, ctx):
        """Example 3 command for OreTweaker."""
        file_path = "examples/ot3.json"
        try:
            with open(file_path, "r") as file:
                json_data = file.read()
            code_block = f"```json\n{json_data}\n```"
            await ctx.send(code_block)
        except FileNotFoundError:
            await ctx.send(f"File '{file_path}' not found.")


async def setup(bot):
    await bot.add_cog(OreTweaker())
