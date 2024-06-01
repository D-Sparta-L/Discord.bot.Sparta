import discord
from discord.ext import commands
import random
import os
import requests

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='.', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def rest(ctx, left: int, right: int):
    await ctx.send(left - right)

@bot.command()
async def mult(ctx, left: int, right: int):
    await ctx.send(left * right)

@bot.command()
async def divi (ctx, left: int, right: int):
    await ctx.send(left / right)



@bot.command()
async def mem(ctx):

    imagen = random.choice(os.listdir("imagenes"))

    with open(f'imagenes/{imagen}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def memc(ctx):

    print(os.listdir('imagenes'))

    with open('imagenes/meme.jpg', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url_d = get_duck_image_url()
    await ctx.send(image_url_d)

def get_dog_image_url():    
    url_d = 'https://random.dog/woof.json'
    res_d = requests.get(url_d)
    data_d = res_d.json()
    return data_d['url']


@bot.command('dog')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url_d = get_dog_image_url()
    await ctx.send(image_url_d)

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')


@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')




bot.run('TOKEN')
