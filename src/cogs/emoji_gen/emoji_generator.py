import random

import emoji
import discord
from discord.ext import commands
from src.cogs.emoji_gen import all_emojis

class EmojiGenerator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = int('f03c3c', 16)

    @commands.command("emoji")
    async def emoji(self, ctx):
        emoji_dict = all_emojis.filtered_emoji_dict
        emoji_to_generate = random.randint(2, 4)
        emoji_string = ""

        for x in range(emoji_to_generate):
            random_emo = emoji.emojize(random.choice(list(emoji_dict.values()))['en'])
            emoji_string += random_emo
            emoji_string += " "

        title = "Emoji Prompt"
        description = f"Draw something based off these emojis: {emoji_string}"
        embed = discord.Embed(title=title, description=description, color=self.color)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(EmojiGenerator(bot))