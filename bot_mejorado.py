import discord
from discord.ext import commands
import os, random
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
    
@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

@bot.command(name='list')
async def _list(ctx, arg):
    pass

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

imagenes = os.listdir('images')
print(os.listdir('images'))

@bot.command()
async def mem(ctx): 
   img_name = random.choice(imagenes)
   with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
   await ctx.send(file=picture)

animals = os.listdir('animals')
print(os.listdir('animals'))

@bot.command()
async def animal(ctx): 
   img_name = random.choice(animals)
   with open(f'animals/{img_name}', 'rb') as f:
            picture = discord.File(f)
   await ctx.send(file=picture)


bot.run("")
