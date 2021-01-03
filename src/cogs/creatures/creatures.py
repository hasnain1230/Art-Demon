import random

import discord
from discord.ext import commands

from utilities.file_data_reader import file_open_read
from assets.Creatures import CreatureCharacteristics


class Creatures(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = int('f03c3c', 16)

    @commands.command()
    async def animal(self, ctx):
        animals = file_open_read('assets/Creatures/animals.txt')

        response = 'Here is a random animal: **%s**!' % animals[random.randint(0, len(animals) - 1)]
        embed = discord.Embed(description=response, colour=discord.Colour(self.color))

        await ctx.channel.send(embed=embed)

    @commands.command()
    async def creature(self, ctx, *creature_type: str):
        color = random.choice(CreatureCharacteristics.color)
        covering = random.choice(CreatureCharacteristics.covering)
        eye_color = random.choice(CreatureCharacteristics.eye_color)
        size = random.choice(CreatureCharacteristics.size)
        body_type = random.choice(CreatureCharacteristics.body_type)
        habitat = random.choice(CreatureCharacteristics.habitat)
        distinguishing_feature = random.choice(CreatureCharacteristics.distinguishing_feature)

        response = f'This creature has **{color}** **{covering}**, and **{eye_color}** eyes. It is **{size}** in size and has a ' \
                   f'**{body_type}** body. It lives in the **{habitat}** and its distinguishing feature is its **{distinguishing_feature}**.'

        embed = discord.Embed(title='Draw a Creature - Realistic', description=response, color=discord.Colour(self.color))
        embed.set_footer(text='Happy Drawing >:)')

        await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Creatures(bot))