import random

import discord
from discord.ext import commands

from utilities.file_data_reader import file_open_read


class Aesthetic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = int('f03c3c', 16)

    @commands.command()
    async def aesthetic(self, ctx):
        aesthetics = file_open_read(
            'assets/aesthetics.txt')  # My own function to read in files more quickly for random stuff since it's done frequently.
        random_aesthetic = random.choice(aesthetics)  # Random - built in.
        response = 'Here is a random aesthetic: the **{}** aesthetic!'.format(random_aesthetic)
        embed = discord.Embed(description=response, colour=discord.Colour(self.color))

        await ctx.channel.send(embed=embed)  # Response


async def setup(bot):
    await bot.add_cog(Aesthetic(bot))
