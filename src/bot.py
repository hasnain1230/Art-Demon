from utilities import config
from discord.ext import commands

bot = commands.Bot(command_prefix='&')
extensions = ('src.cogs.events.events', 'src.cogs.aesthetic.aesthetic', 'src.cogs.creatures.creatures',
              'src.cogs.f_respects.f', 'src.cogs.palette.palette', 'src.cogs.person.person', 'src.cogs.prompts.prompts')


if __name__ == '__main__':
    print('Loading commands...')
    for ext in extensions:
        bot.load_extension(ext)

TOKEN = config.DISCORD_SECRET_TOKEN
bot.run(TOKEN)

'''
@bot.command()
async def embedded(ctx):  # This is just for testing purposes of embedding. Ignore.
    embed = discord.Embed(
        title='Test Title',
        description='Test Description',
        colour=discord.Colour(color)
    )

    file = discord.File('galaxy.jpg', filename='image.jpg')

    embed.set_footer(text='This is a footer')
    embed.set_image(url='attachment://image.jpg')
    embed.set_footer(text='This is a footer')
    embed.set_thumbnail(url='attachment://image.jpg')
    embed.set_author(name='Meee! :D', icon_url='attachment://image.jpg')
    embed.add_field(name='Field Name', value='Field Value1', inline=True)
    embed.add_field(name='Field Name', value='Field Value2', inline=True)
    embed.add_field(name='Field Name', value='Field Value3', inline=False)

    await ctx.channel.send(file=file, embed=embed)
'''
