import os

from PIL import Image
import random
import discord
from discord.ext import commands


def generate_color_image(colors_to_generate):
    image_list = []
    hex_codes = []

    for x in range(colors_to_generate):
        color_int = random.getrandbits(24)
        hex_code = f'#{color_int:06x}'
        hex_codes.append(hex_code)
        image = Image.new("RGB", (100, 100), hex_code)
        image.save(f"src/cogs/color_generator/color{x}.png")
        image_list.append(Image.open(f"src/cogs/color_generator/color{x}.png"))

    total_width = colors_to_generate * 100
    total_height = 100

    combined_image = Image.new("RGB", (total_width, total_height))

    x_offset = 0

    for image in image_list:
        combined_image.paste(image, (x_offset, 0))
        x_offset += image.size[0]

    combined_image.save(f"src/cogs/color_generator/colors.png")

    for x in range(colors_to_generate):
        os.remove(f"src/cogs/color_generator/color{x}.png")

    return hex_codes


class ColorGenerator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = int('f03c3c', 16)

    @commands.command("colors")
    async def colors(self, ctx, *args):
        if args and args[0].isnumeric():
            if 2 <= int(args[0]) <= 6:
                hex_codes = generate_color_image(int(args[0]))

                file = discord.File(f"src/cogs/color_generator/colors.png", filename='image.jpg')
                description = f'Here is/are **{int(args[0])}** random color(s) with the following hex code(s): **{" ".join(hex_codes)}**'
                embed = discord.Embed(title='Random Colors', description=description, color=self.color)
                embed.set_image(url='attachment://image.jpg')
                await ctx.channel.send(file=file, embed=embed)

                os.remove('src/cogs/color_generator/colors.png')

            else:
                await ctx.channel.send("You can only select up to six colors. If you want one color, please use &color (without the s)")
        elif not args:
            colors_to_generate = random.randint(2, 6)
            hex_codes = generate_color_image(colors_to_generate)

            file = discord.File(f"src/cogs/color_generator/colors.png", filename='image.jpg')
            description = f'Here are **{colors_to_generate}** random colors with the following hex codes: **{" ".join(hex_codes)}**'
            embed = discord.Embed(title='Random Colors', description=description, color=self.color)
            embed.set_image(url='attachment://image.jpg')
            await ctx.channel.send(file=file, embed=embed)

            os.remove('src/cogs/color_generator/colors.png')
        else:
            await ctx.channel.send("Did you mean: `&colors` or `&colors {number of colors to generate}`")

    @commands.command("color")
    async def color(self, ctx):
        hex_codes = generate_color_image(1)

        file = discord.File(f"src/cogs/color_generator/colors.png", filename='image.jpg')
        description = f'Here is one random color with the following hex code: **{" ".join(hex_codes)}**'
        embed = discord.Embed(title='Random Colors', description=description, color=self.color)
        embed.set_image(url='attachment://image.jpg')
        await ctx.channel.send(file=file, embed=embed)

        os.remove('src/cogs/color_generator/colors.png')

    @commands.command("hex")
    async def hex(self, ctx, hex_code):
        if hex_code[0] == '#':
            hex_code = hex_code[1:]

        if len(hex_code) == 6:
            image = Image.new("RGB", (135, 135), f'#{hex_code}')
            image.save(f"src/cogs/color_generator/color.png")

            file = discord.File(f"src/cogs/color_generator/color.png", filename='image.jpg')
            description = f'Here is the color with the following hex code: **#{hex_code}**'
            embed = discord.Embed(title='Color Picker', description=description, color=self.color)
            embed.set_image(url='attachment://image.jpg')
            await ctx.channel.send(file=file, embed=embed)
            os.remove('src/cogs/color_generator/color.png')
        else:
            description = f'Please enter a valid hex code. Example: `&hex 000000` or `&hex #000000`'
            embed = discord.Embed(title='Color Picker Error', description=description, color=self.color)
            await ctx.channel.send(embed=embed)


async def setup(bot):
    await bot.add_cog(ColorGenerator(bot))
