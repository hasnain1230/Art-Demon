import random

import discord
from discord.ext import commands


class f(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = int('f03c3c', 16)

    @commands.command()
    async def f(self, ctx, *, args=None):  # Optional to pass various arguments.
        hearts = (':heart:', ':orange_heart:', ':yellow_heart:',
                  ':green_heart:', ':blue_heart:', ':purple_heart:')

        if not args:  # If arguments have not been passed.
            response = f'**{ctx.author.name}** has paid their respects. {random.choice(hearts)}'
        else:
            response = f'**{ctx.author.name}** has paid their respects for {args}. {random.choice(hearts)}'

        embed = discord.Embed(description=response, colour=discord.Colour(self.color))

        await ctx.channel.send(embed=embed)  # Response


async def setup(bot):
    await bot.add_cog(f(bot))
