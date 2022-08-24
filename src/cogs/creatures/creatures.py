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
        try:
            if creature_type[0].lower() == 'realistic':
                color = random.choice(CreatureCharacteristics.CreatureRealistic.color)
                covering = random.choice(CreatureCharacteristics.CreatureRealistic.covering)
                eye_color = random.choice(CreatureCharacteristics.CreatureRealistic.eye_color)
                size = random.choice(CreatureCharacteristics.CreatureRealistic.size)
                body_type = random.choice(CreatureCharacteristics.CreatureRealistic.body_type)
                habitat = random.choice(CreatureCharacteristics.CreatureRealistic.habitat)
                feature_1 = random.choice(CreatureCharacteristics.CreatureRealistic.feature_1)
                feature_2 = random.choice(CreatureCharacteristics.CreatureRealistic.feature_2)

                response = f'This creature has **{color}** **{covering}**, and **{eye_color}** eyes. It is **{size}** and has a ' \
                           f'**{body_type}** body. It lives in the **{habitat}**. It has **{feature_1}** and **{feature_2}**.'

                embed = discord.Embed(title='Draw a Creature - Realistic', description=response,
                                      color=discord.Colour(self.color))
                embed.set_footer(text='Happy Drawing >:)')

                await ctx.channel.send(embed=embed)

            elif creature_type[0].lower() == 'fantasy':
                color = random.choice(CreatureCharacteristics.CreatureFantasy.color)
                covering = random.choice(CreatureCharacteristics.CreatureFantasy.covering)
                eye_color = random.choice(CreatureCharacteristics.CreatureFantasy.eye_color)
                size = random.choice(CreatureCharacteristics.CreatureFantasy.size)
                body_type = random.choice(CreatureCharacteristics.CreatureFantasy.body_type)
                habitat = random.choice(CreatureCharacteristics.CreatureFantasy.habitat)
                feature_1 = random.choice(CreatureCharacteristics.CreatureFantasy.feature_1)
                feature_2 = random.choice(CreatureCharacteristics.CreatureFantasy.feature_2)

                response = f'This creature has **{color}** **{covering}**, and **{eye_color}**. It is **{size}** and has a **{body_type}** body. ' \
                           f'It lives in **{habitat}**. It has **{feature_1}** and **{feature_2}**.'

                embed = discord.Embed(title='Draw a Creature - Fantasy', description=response,
                                      color=discord.Colour(self.color))
                embed.set_footer(text='Happy Drawing >:)')

                await ctx.channel.send(embed=embed)

        except IndexError:
            random_prompt = random.randint(1, 2)

            if random_prompt == 1:
                await self.creature(ctx, 'realistic')
            else:
                await self.creature(ctx, 'fantasy')


async def setup(bot):
    await bot.add_cog(Creatures(bot))
