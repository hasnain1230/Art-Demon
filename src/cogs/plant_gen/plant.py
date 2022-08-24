import random

import discord
from discord.ext import commands
from src.cogs.plant_gen import fantasy_plant as fp
from src.cogs.plant_gen import realistic_plant as rp


class Plant(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = int('f03c3c', 16)

    @commands.command(name="plant")
    async def plant(self, ctx, *args):
        if args:
            if args[0].lower() == 'fantasy':
                title = 'Draw A Plant - Fantasy'
                response = f'This plant is **{random.choice(fp.type_of_plant)}**. It is **{random.choice(fp.color)}** ' \
                           f'with **{random.choice(fp.part1)}** and **{random.choice(fp.part2)}**. It ' \
                           f'is a **{random.choice(fp.size)}** plant ' \
                           f'that grows in **{random.choice(fp.place)}** and **{random.choice(fp.detail)}**.'

                embed = discord.Embed(title=title, description=response, color=self.color)
                await ctx.channel.send(embed=embed)
            elif args[0].lower() == 'realistic':
                title = 'Draw A Plant - Realistic'
                response = f'This plant is **{random.choice(rp.type_of_plant)}**. It is **{random.choice(rp.color)}**' \
                           f' with **{random.choice(rp.part1)}** and **{random.choice(rp.part2)}**. It ' \
                           f'is a **{random.choice(rp.size)}** plant ' \
                           f'that grows in **{random.choice(rp.place)}** and **{random.choice(rp.detail)}**.'

                embed = discord.Embed(title=title, description=response, color=self.color)
                await ctx.channel.send(embed=embed)
        else:
            await self.plant(ctx, random.choice(['fantasy', 'realistic']))


async def setup(bot):
    await bot.add_cog(Plant(bot))
