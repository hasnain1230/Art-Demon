import random

import discord
from discord.ext import commands

from utilities.file_data_reader import file_open_read


class Animal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = int('f03c3c', 16)

    @commands.command()
    async def animal(self, ctx):
        animals = file_open_read('assets/animals.txt')

        response = 'Here is a random animal: **%s**!' % animals[random.randint(0, len(animals) - 1)]
        embed = discord.Embed(description=response, colour=discord.Colour(self.color))

        await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Animal(bot))
