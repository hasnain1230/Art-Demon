import glob
import random

import discord
from discord.ext import commands


class Palette(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = int('f03c3c', 16)

    @commands.command()
    async def palette(self, ctx):
        palettes = tuple(glob.glob('assets/Palettes/*.png'))
        random_pal_file = random.choice(palettes)
        file = discord.File(random_pal_file, filename="image.png")
        embed = discord.Embed(colour=discord.Colour(self.color))
        embed.set_image(url="attachment://image.png")
        await ctx.channel.send(file=file, embed=embed)


async def setup(bot):
    await bot.add_cog(Palette(bot))
