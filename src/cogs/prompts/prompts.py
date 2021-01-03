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
        self.active_prompt = False

    @commands.command()
    async def prompt(self, ctx, *prompt_type: str):
        if prompt_type:
            if prompt_type[0].lower() == 'people':
                prompts = file_open_read('assets/Prompts/People Prompts.txt')

                embed = discord.Embed(title='People Prompt', description=random.choice(prompts),
                                      colour=discord.Colour(self.color))
                embed.set_footer(text='Happy Drawing >:)')

                await ctx.channel.send(embed=embed)
            elif prompt_type[0].lower() == 'animal':
                prompts = file_open_read('assets/Prompts/Animal Prompts.txt')

                embed = discord.Embed(title='Animal Prompt', description=random.choice(prompts),
                                      colour=discord.Colour(self.color))
                embed.set_footer(text='Happy Drawing >:)')

                await ctx.channel.send(embed=embed)
            elif prompt_type[0].lower() == 'oc':
                OCs = file_open_read('assets/Prompts/OC.txt')
                response = random.choice(OCs)
                embed = discord.Embed(title='OC Prompt', description=response, colour=discord.Colour(self.color))
                embed.set_footer(text='Happy Drawing >:)')

                await ctx.channel.send(embed=embed)

            elif prompt_type[0].lower() == 'nature':
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

    '''
    With this command, I am concerned if the datetime is being handled correctly with the passed in time value. I don't
    know if there is a better way to properly setup the timer. Additionally, in concern to asynchronous programming, I 
    am not sure what the best way to set the timer is and if I need to even build in functionality to see if there is an
    active prompt. Definitely more research needs to be done for sure.  
    '''
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def dailyprompt(self, ctx, arbitrary_prefix, channel: discord.TextChannel,
                          time_to_run, *role: discord.Role):  # I'm not sure if this is the best way to do this. I have to do some research. =/
        if arbitrary_prefix == 'set':
            if self.active_prompt is False:
                await ctx.channel.send('Daily Prompt has been set! [Though it is not fully functional right now.]')

                time_zone = pytz.timezone('EST')

                now = datetime.now(time_zone)
                time_to_run = f'{str(now.date())} {time_to_run}'
                time_to_run = datetime.strptime(time_to_run, '%Y-%m-%d %H:%M').astimezone(time_zone)
                print(time_to_run)
                delay = (time_to_run - now).total_seconds()
                ctx.channel = channel

                self.active_prompt = True
                await asyncio.sleep(delay)
                await self.prompt(ctx)
                self.active_prompt = False

                if role:
                    await ctx.channel.send(role[0].mention)
            else:
                await ctx.channel.send('There is currently an active dailyprompt. Please disable that one to set a new one!')

        else:
            raise CommandNotFound


def setup(bot):
    bot.add_cog(Prompts(bot))
