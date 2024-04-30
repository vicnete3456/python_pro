import discord
from discord.ext import commands
import random
import os
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'Hemos iniciado sesion con {bot.user}')
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un {bot.user} y fui creado para dar consejos de la contaminacion!')
ideas_manualidades = [
    'Hacer porta macetas con papel',
    'hacer vasos con botellas de vidrio',
    "decorar botellas",
    "decorar tu casa o departamento con cosas reciclables"
]
consejos = [
    'Usa bolsas reutilizables para tus compras',
    'Evita los productos de un solo uso como sorbetes y cubiertos de plastico',
    'manualidades',
    "puedes en ves de conducir hacer deporte he ir en bicicleta"
]
@bot.command()
async def ideas(ctx):
    idea = random.choice(ideas_manualidades)
    await ctx.send(idea)
@bot.command()
async def consejo(ctx):
    consejo = random.choice(consejos)
    await ctx.send(consejo)
# Funcion que explica que es la contaminacion
@bot.command()
async def contaminacion(ctx):
    definicion = "La contaminación es la presencia de un constituyente, impureza o algún otro elemento indeseable que estropea, corrompe, infecta, inutiliza o degrada un material, cuerpo físico, entorno natural, lugar de trabajo, etc"
    await ctx.send(definicion)

manualidades = os.listdir('manualidades')
print(os.listdir('manualidades'))

@bot.command()
async def mano(ctx): 
   img_name = random.choice(manualidades)
   with open(f'manualidades/{img_name}', 'rb') as f:
            picture = discord.File(f)
   await ctx.send(file=picture)








bot.run("")
