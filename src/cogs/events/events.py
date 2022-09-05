import asyncio
import threading

import discord.ext.commands.errors
from discord.ext import commands, tasks

from src.cogs.prompts.prompts import Prompts
from discord.ext.commands import CommandNotFound, MissingPermissions

from utilities.Drive import Drive


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = int('f03c3d', 16)
        print('Authenticating Services')
        self.drive_object = Drive()
        self.drive_object.auth()
        self.GDrive_Refresh.start()

    async def start_dailyprompts(self):
        prompts = Prompts(self.bot)
        asyncio.run_coroutine_threadsafe(prompts.restart_prompts(), self.bot.loop)

    @commands.Cog.listener()
    async def on_ready(self):
        # channel = self.bot.get_channel(796201038881095694)
        t = threading.Thread(target=asyncio.run, args=(self.start_dailyprompts(),))
        print("Starting new thread for daily prompts")
        t.start()
        print('Done and Ready!')
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Indigo Draw"))
        t.join()

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, CommandNotFound):
            await ctx.channel.send('That command was not found and/or does not exist. Please use &help to get a list '
                                   'of commands!')
            print(error)
            return
        if isinstance(error, MissingPermissions):
            await ctx.channel.send('Hey! >:( you have don\'t have permission to do that!')

        if isinstance(error, discord.ext.commands.errors.ChannelNotFound):
            await ctx.channel.send("Invalid channel")

        raise error

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

    @commands.command()
    async def logout(self, ctx):
        if ctx.author.id == 693089171002097724 or ctx.author.id == 214935867859402752:
            await ctx.channel.send('Going Offline')
            await self.bot.close()
        else:
            await ctx.channel.send('You do not have the permission to do that!')
            raise MissingPermissions(MissingPermissions)

    @tasks.loop(hours=6)
    async def GDrive_Refresh(self):
        self.drive_object.get_files_from_id('1c5T1EHN0aWefDiV7c_zEPICQDXcLgCBX')
        self.drive_object.download_files_from_json('assets/Palettes/downloaded.json')


async def setup(bot):
    await bot.add_cog(Events(bot))
