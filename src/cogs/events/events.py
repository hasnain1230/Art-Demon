from discord.ext import commands, tasks
from discord.ext.commands import CommandNotFound, MissingPermissions

from utilities.Drive import Drive


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = int('f03c3c', 16)
        self.drive_object = Drive()
        print('Authenticating Services')
        self.drive_object.auth()
        self.GDrive_Refresh.start()

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Logged In {self.bot.user}')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, CommandNotFound):
            await ctx.channel.send(
                'That command was not found and/or does not exist. Please use &help to get a list of commands!')
            return
        if isinstance(error, MissingPermissions):
            await ctx.channel.send('Hey! >:( you have don\'t have permission to do that!')
        raise error

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

    @tasks.loop(hours=6)
    async def GDrive_Refresh(self):
        self.drive_object.get_files_from_id('1c5T1EHN0aWefDiV7c_zEPICQDXcLgCBX')
        self.drive_object.download_files_from_json('assets/Palettes/downloaded.json')

    @commands.command()
    async def logout(self, ctx):
        if ctx.author.id == 693089171002097724:
            await ctx.channel.send('Going Offline')
            await self.bot.logout()
        else:
            await ctx.channel.send('You do not have the permission to do that!')
            # raise MissingPermissions() ?? Need to figure out what to pass in.


def setup(bot):
    bot.add_cog(Events(bot))
