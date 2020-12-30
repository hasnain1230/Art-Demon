import random

import discord
from discord.ext import commands

from utilities.file_data_reader import file_open_read
from utilities.persondefinition import PersonDefinition


class Person(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = int('f03c3c', 16)

    @commands.command()
    async def person(self, ctx, *args):
        if args:
            if args[0] == 'fantasy':
                hair_texture = file_open_read('assets/Person Characteristics/Fantasy/Hair Texture.txt')
                hair_color = file_open_read('assets/Person Characteristics/Fantasy/Hair Color.txt')
                eye_color = file_open_read('assets/Person Characteristics/Fantasy/Eye Color.txt')
                skin_tone = file_open_read('assets/Person Characteristics/Fantasy/Skin Tone.txt')
                body_type = file_open_read('assets/Person Characteristics/Fantasy/Body Type.txt')
                gender_age = file_open_read('assets/Person Characteristics/Fantasy/Gender & Age.txt')
                features = file_open_read('assets/Person Characteristics/Fantasy/Features.txt')

                fantasy_person = PersonDefinition(hair_texture, hair_color, eye_color, skin_tone, body_type, gender_age, features)

                prompt = 'This person has **{0}** **{1}** hair, and **{2}** colored eyes. They have a ' \
                         '**{3}** skin tone and **{4}** build. They are **{5}** and their distinguishing ' \
                         'feature is their **{6}**.'.format(fantasy_person.get_random_from_list(hair_color),
                                                            fantasy_person.get_random_from_list(hair_texture),
                                                            fantasy_person.get_random_from_list(eye_color),
                                                            fantasy_person.get_random_from_list(skin_tone),
                                                            fantasy_person.get_random_from_list(body_type),
                                                            fantasy_person.get_random_from_list(gender_age),
                                                            fantasy_person.get_random_from_list(features))

                embed = discord.Embed(title='Draw A Person - Fantasy', description=prompt, colour=discord.Colour(self.color))
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

                real_person = PersonDefinition(hair_texture, hair_color, eye_color, skin_tone, body_type, gender_age, features)

                prompt = 'This person has **{0}** **{1}** hair, and **{2}** colored eyes. They have a **{3}**' \
                         ' skin tone and **{4}** build. They are **{5}** and their distinguishing feature is their' \
                         ' **{6}**.'.format(real_person.get_random_from_list(hair_texture),
                                            real_person.get_random_from_list(hair_color),
                                            real_person.get_random_from_list(eye_color),
                                            real_person.get_random_from_list(skin_tone),
                                            real_person.get_random_from_list(body_type),
                                            real_person.get_random_from_list(gender_age),
                                            real_person.get_random_from_list(features))

                embed = discord.Embed(title='Draw A Person - Realistic', description=prompt,
                                      colour=discord.Colour(self.color))
                embed.set_footer(text='Happy Drawing >:)')

                await ctx.channel.send(embed=embed)
        else:
            probability = random.uniform(0, 1)

            if probability < .49:
                await self.person(ctx, 'realistic')
            else:
                await self.person(ctx, 'fantasy')


def setup(bot):
    bot.add_cog(Person(bot))
