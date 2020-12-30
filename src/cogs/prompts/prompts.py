import asyncio
import random
from datetime import datetime

import discord
import pytz
from discord.ext import commands
from discord.ext.commands import CommandNotFound

from utilities.file_data_reader import file_open_read


class Prompts(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = int('f03c3c', 16)

    @commands.command()
    async def prompt(self, ctx, *args):
        if args:
            if args[0].lower() == 'people':
                prompts = file_open_read('assets/Prompts/People Prompts.txt')

                embed = discord.Embed(title='People Prompt', description=random.choice(prompts),
                                      colour=discord.Colour(self.color))
                embed.set_footer(text='Happy Drawing >:)')

                await ctx.channel.send(embed=embed)
            elif args[0].lower() == 'animal':
                prompts = file_open_read('assets/Prompts/Animal Prompts.txt')

                embed = discord.Embed(title='Animal Prompt', description=random.choice(prompts),
                                      colour=discord.Colour(self.color))
                embed.set_footer(text='Happy Drawing >:)')

                await ctx.channel.send(embed=embed)
            elif args[0].lower() == 'oc':
                OCs = file_open_read('assets/Prompts/OC.txt')
                response = random.choice(OCs)
                embed = discord.Embed(title='OC Prompt', description=response, colour=discord.Colour(self.color))
                embed.set_footer(text='Happy Drawing >:)')

                await ctx.channel.send(embed=embed)

            elif args[0].lower() == 'nature':
                nature_prompts = file_open_read('assets/Prompts/Nature Prompts.txt')
                response = random.choice(nature_prompts)
                embed = discord.Embed(title='Nature Prompt', description=response, color=discord.Colour(self.color))
                embed.set_footer(text='Happy Drawing')

                await ctx.channel.send(embed=embed)

        else:
            all_prompts = file_open_read('assets/Prompts/OC.txt') + file_open_read(
                'assets/Prompts/Animal Prompts.txt') + \
                          file_open_read('assets/Prompts/People Prompts.txt') + file_open_read(
                'assets/Prompts/Nature Prompts.txt')
            response = random.choice(all_prompts)

            embed = discord.Embed(title='Art Prompt', description=response, color=self.color)

            await ctx.channel.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def dailyprompt(self, ctx, arbitrary_prefix, channel: discord.TextChannel,
                          time_to_run):  # I'm not sure if this is the best way to do this. I have to do some research. =/
        if arbitrary_prefix == 'set':
            await ctx.channel.send('Daily Prompt has been set! [Though it is not fully functional right now.]')

            time_zone = pytz.timezone('EST')

            now = datetime.now(time_zone)
            time_to_run = f'{str(now.date())} {time_to_run}'
            time_to_run = datetime.strptime(time_to_run, '%Y-%m-%d %H:%M').astimezone(time_zone)
            delay = (time_to_run - now).total_seconds()
            ctx.channel = channel

            await asyncio.sleep(delay)
            await self.prompt(ctx)
        else:
            raise CommandNotFound


def setup(bot):
    bot.add_cog(Prompts(bot))
