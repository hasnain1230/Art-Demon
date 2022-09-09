import asyncio
import csv
import random
from datetime import datetime, timedelta

import discord
import pytz
from discord.ext import commands

from utilities.file_data_reader import file_open_read

from assets.Prompts import word
from assets.Prompts import keywords


def format_time_correctly(time_to_run):
    if len(time_to_run) == 5 and time_to_run[0:2].isnumeric() and time_to_run[2] == ':' and time_to_run[3:5].isnumeric():
        return True

    return False


class Prompts(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = int('f03c3c', 16)
        self.bot.active_tasks = dict()

    async def sleep_cancel_safe(self, delay, guild_id, result=None):
        coro = asyncio.sleep(delay, result=result)
        task = asyncio.ensure_future(coro)

        self.bot.active_tasks[guild_id] = task

        try:
            return await task
        except asyncio.CancelledError:
            return result
        finally:
            del self.bot.active_tasks[guild_id]

    @classmethod
    def can_cancel(cls, guild_id, user_id):
        with open('src/cogs/prompts/Daily_Prompt.log', 'r') as csvfile:
            reader = csv.reader(csvfile)

            for row in reader:
                if int(row[0]) == guild_id:
                    if int(row[2]) == user_id:
                        return True
                    else:
                        return False

            return None

    @classmethod
    def check_active(cls, guild_id):
        with open('src/cogs/prompts/Daily_Prompt.log', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if int(row[0]) == guild_id:
                    if row[4] == 'Active':
                        return True
                    else:
                        return False

    @classmethod
    def update_log(cls, guild_id):
        lines = list()
        with open('src/cogs/prompts/Daily_Prompt.log', 'r') as csvfile:
            reader = csv.reader(csvfile)

            for row in reader:
                if int(row[0]) == guild_id:
                    row[4] = 'Inactive'
                lines.append(row)

        with open('src/cogs/prompts/Daily_Prompt.log', 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(lines)

        csvfile.close()

    @classmethod
    def check_for_duplicates(cls, guild_id):
        lines = list()
        duplicate_status = False
        with open('src/cogs/prompts/Daily_Prompt.log', 'r') as csvfile:
            reader = csv.reader(csvfile)

            for row in reader:
                if int(row[0]) == guild_id and row[4] == 'Active':
                    duplicate_status = True
                    lines.append(row)
                elif int(row[0]) == guild_id and row[4] == 'Inactive':
                    continue
                else:
                    lines.append(row)

            csvfile.close()

        with open('src/cogs/prompts/Daily_Prompt.log', 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(lines)

        csvfile.close()
        return duplicate_status

    @classmethod
    def log_daily_prompt(cls, ctx, channel, user_id, time_to_run):
        with open('src/cogs/prompts/Daily_Prompt.log', 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([ctx.message.guild.id, channel.id, user_id, time_to_run, "Active"])

        csvfile.close()

    async def restart_prompts(self):
        with open('src/cogs/prompts/Daily_Prompt.log', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[4] == 'Active':
                    channel = self.bot.get_channel(int(row[1]))
                    await self.dailyprompt(self, None, 'set', channel=channel, time_to_run=row[3], prompt=False,
                                           restart=True, guild_id=int(row[0]))

    @commands.command()
    async def prompt(self, ctx, *args, dp=False): # When this function was written, sub commands were not a thing yet, so messy code like this had to be written. It will be updated in a later iteration
        if args:
            if args[0].lower() == 'people':
                prompts = file_open_read('assets/Prompts/People Prompts.txt')

                embed = discord.Embed(title='People Prompt', description=random.choice(prompts),
                                      colour=discord.Colour(self.color))
                embed.set_footer(text='Happy Drawing >:)')

                await ctx.send(embed=embed)
            elif args[0].lower() == 'animal':
                prompts = file_open_read('assets/Prompts/Animal Prompts.txt')

                embed = discord.Embed(title='Animal Prompt', description=random.choice(prompts),
                                      colour=discord.Colour(self.color))
                embed.set_footer(text='Happy Drawing >:)')

                await ctx.send(embed=embed)
            elif args[0].lower() == 'oc':
                OCs = file_open_read('assets/Prompts/OC.txt')
                response = random.choice(OCs)
                embed = discord.Embed(title='OC Prompt', description=response, colour=discord.Colour(self.color))
                embed.set_footer(text='Happy Drawing >:)')

                await ctx.send(embed=embed)

            elif args[0].lower() == 'nature':
                nature_prompts = file_open_read('assets/Prompts/Nature Prompts.txt')
                response = random.choice(nature_prompts)
                embed = discord.Embed(title='Nature Prompt', description=response, color=discord.Colour(self.color))
                embed.set_footer(text='Happy Drawing >:)')

                await ctx.send(embed=embed)

            elif args[0].lower() == 'word':  # Uses .py files to read data rather than lists. Intended to be changed in a later iteration.
                response = word.response[0]
                embed = discord.Embed(title='Word Prompt', description=response, color=discord.Colour(self.color))
                embed.set_footer(text='Happy Drawing >:)')
                await ctx.send(embed=embed)

            elif args[0].lower() == 'keywords':
                words = random.sample(keywords.keywords, 3)
                response = f'Here are your three keywords: **{words[0]}**, **{words[1]}**, **{words[2]}**.'
                embed = discord.Embed(title='Keywords Prompt', description=response, colour=discord.Colour(self.color))
                await ctx.send(embed=embed)

            else:
                raise discord.ext.commands.CommandNotFound

        else:  # Fixing needs to be done here.
            all_prompts = file_open_read('assets/Prompts/OC.txt') + file_open_read(
                'assets/Prompts/Animal Prompts.txt') + \
                          file_open_read('assets/Prompts/People Prompts.txt') + file_open_read(
                'assets/Prompts/Nature Prompts.txt') + word.response + keywords.response

            response = random.choice(all_prompts)

            if dp:
                title = f'Daily Prompt {datetime.now(tz=pytz.timezone("America/New_York")).strftime("%A, %B %d, %Y")}'
            else:
                title = 'Art Prompt'

            embed = discord.Embed(title=title, description=response, color=self.color)

            await ctx.send(embed=embed)

    @commands.command(aliases=['dp'])
    @commands.has_permissions(administrator=True)
    async def dailyprompt(self, ctx, arbitrary_prefix='', channel: discord.TextChannel = None, time_to_run: str = None, *, args=None,
                          prompt=True, restart=False, repeat=False, guild_id=None):  # This command seriously needs a database to run more efficiently. For now though, I just want it working.
        if not format_time_correctly(time_to_run) or args:
            await ctx.channel.send('Time Format Error: Did you mean `dailyprompt set [#channel] [time HH:MM]`?')
            return

        if arbitrary_prefix.lower() == 'set' and channel is not None and time_to_run is not None:
            if not restart and not repeat:
                guild_id = ctx.message.guild.id
                duplicates = self.check_for_duplicates(ctx.message.guild.id)
                if duplicates:
                    response = "Sorry, you already have a daily prompt active. You can only have one active at a time! If you " \
                               "believe this is an error, please report it to Indigo. [Note: If this bot gets more use, " \
                               "or has a ton of bugs, we'll develop a form where bugs can be reported.]"
                    embed = discord.Embed(title='*Error* Daily Prompt Admin *Error*', description=response,
                                          color=self.color)
                    await ctx.channel.send(embed=embed)
                    return

            time_zone = pytz.timezone('America/New_York')

            now = datetime.now(time_zone)

            datetime_to_run = f'{str(now.date())} {time_to_run}'
            datetime_to_run = datetime.strptime(datetime_to_run, '%Y-%m-%d %H:%M').astimezone(time_zone)
            difference = (datetime_to_run - now).total_seconds()

            if difference < 0:
                datetime_to_run += timedelta(hours=24)
                difference = (datetime_to_run - now).total_seconds()
                if difference < 0:
                    await ctx.send('Please input a valid time.')
                    raise ValueError
            # i want daily prompt header to say “Daily Prompt (day of week) (date) (year)

            if prompt:
                response = f'You have a set a daily prompt for **{datetime_to_run.time()} EST**. It is set to begin at ' \
                           f'**{datetime_to_run.strftime("%A, %B %d, %Y")} at {datetime_to_run.time()}**. ' \
                           f'If you encounter any errors, please contact **Indigo#7177** and tell them to yell at me. xP'

                title = f'Daily Prompt Admin Notification'

                embed = discord.Embed(title=title, description=response, color=self.color)
                await ctx.send(embed=embed)

            if not restart and not repeat:
                self.log_daily_prompt(ctx, channel, ctx.author.id, time_to_run)

            await self.sleep_cancel_safe(difference, guild_id, result=None)

            ctx = channel

            if self.check_active(guild_id):
                if restart:
                    await self.prompt(self, ctx, dp=True)
                    await self.dailyprompt(self, ctx, 'set', channel=channel, time_to_run=time_to_run, prompt=False,
                                           restart=restart, repeat=True, guild_id=guild_id)
                else:
                    await self.prompt(ctx, dp=True)
                    await self.dailyprompt(ctx, 'set', channel=channel, time_to_run=time_to_run, prompt=False,
                                           restart=restart, repeat=True, guild_id=guild_id)

        elif arbitrary_prefix.lower() == 'cancel':
            try:
                task = self.bot.active_tasks[int(ctx.message.guild.id)]
            except KeyError:
                await ctx.send("Error: You do not have a daily prompt active, or we could not find one.")
                return

            if self.can_cancel(ctx.message.guild.id, ctx.author.id):
                response = "Your dailyprompt has been cancelled! Congrats!"
                embed = discord.Embed(title='Daily Prompt Admin Notification', description=response, color=self.color)
                await ctx.author.send(embed=embed)

                self.update_log(ctx.message.guild.id)
                task.cancel()
            else:
                await ctx.channel.send("Sorry, you cannot cancel a daily prompt that you did not start")
        else:
            await ctx.channel.send('Did you mean `dailyprompt set [#channel] [time HH:MM]`?')


async def setup(bot):
    await bot.add_cog(Prompts(bot))
