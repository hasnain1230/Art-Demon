import discord
import discord.ext
from discord.ext import commands


class HELP(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = int('f03c3c', 16)

    @commands.command('help')
    async def help(self, ctx):
        embed = discord.Embed(title="Art Demon Commands",
                              description="You can view all Art Demon commands [here](https://github.com/hasnain1230/Art-Demon/blob/main/HELP.md)",
                              color=self.color)

        await ctx.author.send(embed=embed)

    @commands.command('source')
    async def source(self, ctx):
        embed = discord.Embed(title="Art Demon Source Code",
                              description="You can view Art Demon's source code [here](https://github.com/hasnain1230/Art-Demon)",
                              color=self.color)

        await ctx.author.send(embed=embed)


async def setup(bot):
    await bot.add_cog(HELP(bot))
