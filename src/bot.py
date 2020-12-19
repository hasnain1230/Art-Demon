import glob
import sys

import discord
import random
from utilities import config
from utilities.file_data_reader import file_open_read
from discord.ext import commands
from discord.ext.commands import CommandNotFound, MissingPermissions, ExpectedClosingQuoteError

from utilities.Drive import Drive
from utilities.person import Person

print('Authenticating Services...')
drive_object = Drive()
drive_object.auth()

bot = commands.Bot(command_prefix='=')

color = int('f03c3c', 16)

palettes = tuple(glob.glob('assets/Palettes/*.png'))


@bot.event
async def on_ready():
    print('Logged In {}'.format(bot.user))
    # Would like to learn how to send a message to all channels.


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    await bot.process_commands(message)


@bot.command()
async def person(ctx, *args):
    if args:
        if args[0] == 'fantasy':
            hair_texture = file_open_read('assets/Person Characteristics/Fantasy/Hair Texture.txt')
            hair_color = file_open_read('assets/Person Characteristics/Fantasy/Hair Color.txt')
            eye_color = file_open_read('assets/Person Characteristics/Fantasy/Eye Color.txt')
            skin_tone = file_open_read('assets/Person Characteristics/Fantasy/Skin Tone.txt')
            body_type = file_open_read('assets/Person Characteristics/Fantasy/Body Type.txt')
            gender_age = file_open_read('assets/Person Characteristics/Fantasy/Gender & Age.txt')
            features = file_open_read('assets/Person Characteristics/Fantasy/Features.txt')

            fantasy_person = Person(hair_texture, hair_color, eye_color, skin_tone, body_type, gender_age, features)

            prompt = 'This person has **{0}** **{1}** hair, and **{2}** colored eyes. They have a ' \
                     '**{3}** skin tone and **{4}** build. They are **{5}** and their distinguishing ' \
                     'feature is their **{6}**.'.format(fantasy_person.get_random_from_list(hair_color),
                                                        fantasy_person.get_random_from_list(hair_texture),
                                                        fantasy_person.get_random_from_list(eye_color),
                                                        fantasy_person.get_random_from_list(skin_tone),
                                                        fantasy_person.get_random_from_list(body_type),
                                                        fantasy_person.get_random_from_list(gender_age),
                                                        fantasy_person.get_random_from_list(features))

            embed = discord.Embed(title='Draw A Person - Fantasy', description=prompt, colour=discord.Colour(color))
            embed.set_footer(text='Happy Drawing >:)')

            await ctx.channel.send(embed=embed)

        elif args[0] == 'realistic':
            hair_texture = file_open_read('assets/Person Characteristics/Real/Hair Texture.txt')
            hair_color = file_open_read('assets/Person Characteristics/Real/Hair Color.txt')
            eye_color = file_open_read('assets/Person Characteristics/Real/Eye Color.txt')
            skin_tone = file_open_read('assets/Person Characteristics/Real/Skin Tone.txt')
            body_type = file_open_read('assets/Person Characteristics/Real/Body Type.txt')
            gender_age = file_open_read('assets/Person Characteristics/Real/Gender & Age.txt')
            features = file_open_read('assets/Person Characteristics/Real/Features.txt')

            real_person = Person(hair_texture, hair_color, eye_color, skin_tone, body_type, gender_age, features)

            prompt = 'This person has **{0}** **{1}** hair, and **{2}** colored eyes. They have a **{3}**' \
                     ' skin tone and **{4}** build. They are **{5}** and their distinguishing feature is their' \
                     ' **{6}**.'.format(real_person.get_random_from_list(hair_texture),
                                        real_person.get_random_from_list(hair_color),
                                        real_person.get_random_from_list(eye_color),
                                        real_person.get_random_from_list(skin_tone),
                                        real_person.get_random_from_list(body_type),
                                        real_person.get_random_from_list(gender_age),
                                        real_person.get_random_from_list(features))

            embed = discord.Embed(title='Draw A Person - Realistic', description=prompt, colour=discord.Colour(color))
            embed.set_footer(text='Happy Drawing >:)')

            await ctx.channel.send(embed=embed)
    else:
        probability = random.uniform(0, 1)

        if probability < .49:
            await person(ctx, 'realistic')
        else:
            await person(ctx, 'fantasy')


@bot.command()
async def prompt(ctx, *args):
    if args:
        if args[0].lower() == 'people':
            prompts = file_open_read('assets/Prompts/People Prompts.txt')

            embed = discord.Embed(title='People Prompt', description=random.choice(prompts),
                                  colour=discord.Colour(color))
            embed.set_footer(text='Happy Drawing >:)')

            await ctx.channel.send(embed=embed)
        elif args[0].lower() == 'animal':
            prompts = file_open_read('assets/Prompts/Animal Prompts.txt')

            embed = discord.Embed(title='Animal Prompt', description=random.choice(prompts),
                                  colour=discord.Colour(color))
            embed.set_footer(text='Happy Drawing >:)')

            await ctx.channel.send(embed=embed)
        elif args[0].lower() == 'oc':
            OCs = file_open_read('assets/Prompts/OC.txt')
            response = random.choice(OCs)
            embed = discord.Embed(title='OC Prompt', description=response, colour=discord.Colour(color))
            embed.set_footer(text='Happy Drawing >:)')

            await ctx.channel.send(embed=embed)

        elif args[0].lower() == 'nature':
            nature_prompts = file_open_read('assets/Prompts/Nature Prompts.txt')
            response = random.choice(nature_prompts)
            embed = discord.Embed(title='Nature Prompt', description=response, color=discord.Colour(color))
            embed.set_footer(text='Happy Drawing')

            await ctx.channel.send(embed=embed)

    else:
        all_prompts = file_open_read('assets/Prompts/OC.txt') + file_open_read('assets/Prompts/Animal Prompts.txt') + \
                      file_open_read('assets/Prompts/People Prompts.txt') + file_open_read('assets/Prompts/Nature Prompts.txt')
        response = random.choice(all_prompts)

        embed = discord.Embed(title='Art Prompt', description=response, color=color)

        await ctx.channel.send(embed=embed)


@bot.command()
async def animal(ctx):
    animals = file_open_read('assets/animals.txt')

    response = 'Here is a random animal: **%s**!' % animals[random.randint(0, len(animals) - 1)]
    embed = discord.Embed(description=response, colour=discord.Colour(color))

    await ctx.channel.send(embed=embed)


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


@bot.command()
async def f(ctx, *, args=None):  # Optional to pass various arguments.
    hearts = (':heart:', ':orange_heart:', ':yellow_heart:',
              ':green_heart:', ':blue_heart:', ':purple_heart:')

    if not args:  # If arguments have not been passed.
        response = f'**{ctx.author.name}** has paid their respects. {random.choice(hearts)}'
    else:
        response = f'**{ctx.author.name}** has paid their respects for {args}. {random.choice(hearts)}'

    embed = discord.Embed(description=response, colour=discord.Colour(color))

    await ctx.channel.send(embed=embed)  # Response


@bot.command()
async def aesthetic(ctx):
    aesthetics = file_open_read(
        'assets/aesthetics.txt')  # My own function to read in files more quickly for random stuff since it's done frequently.
    random_aesthetic = random.choice(aesthetics)  # Random - built in.
    response = 'Here is a random aesthetic: the **{}** aesthetic!'.format(random_aesthetic)
    embed = discord.Embed(description=response, colour=discord.Colour(color))

    await ctx.channel.send(embed=embed)  # Response


@bot.command()
async def palette(ctx):  # Not working right now.
    drive_object.get_files_from_id('1c5T1EHN0aWefDiV7c_zEPICQDXcLgCBX')
    drive_object.download_files_from_json('assets/Palettes/downloaded.json')
    random_pal_file = random.choice(palettes)
    file = discord.File(random_pal_file, filename="image.png")
    embed = discord.Embed(colour=discord.Colour(color))
    embed.set_image(url="attachment://image.png")
    await ctx.channel.send(file=file, embed=embed)


@bot.command(name='exit')
@commands.has_permissions(administrator=True)
async def exit(ctx):
    print(bot.guilds.members)
    await ctx.channel.send('Going Offline')
    sys.exit('Going offline.')


TOKEN = config.DISCORD_SECRET_TOKEN
bot.run(TOKEN)
