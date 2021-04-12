import discord
from discord.ext import commands
import requests
import re
import random
from os import environ

# client = discord.Client()
bot = commands.Bot(command_prefix='#')


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

                
# cuando urre entra al canal de truchaaa
@bot.event
async def on_voice_state_update(member, before, after):
    if str(member) == "Trucho#6631" and str(after.channel.id) == "785246386408128605":
        urre = ("esa truchazo que se va a jugar hoy", "que rico tener aca truchita", "llego el master dic", "que onda urre su lol o codeo hoy?", "wena urre", "a no!")
        mensaje = random.choice(urre)
        await member.guild.system_channel.send(mensaje)

## Lectura de mensajes
@bot.event
async def on_message(message):
    
    ## Si mensaje es el mismo bot
    if message.author == bot.user:
        return

    ## pin pong   
    if message.content == "ping":
        await message.channel.send('pong')


    ## Operaciones sobre el contenido
    content = message.content.split(" ")
    ## Procesamientos del cotenido
    saludos = ("hola", "holi", "buenas", "hello", "qué tal", "wena")

    ### Saludos
    if any(saludo in content for saludo in saludos):
        if str(message.author) == 'Trucho#6631':
            await message.channel.send('esa truchazo usted sabe, py love for you :hearts:')
        else:
            await message.channel.send('buenas buenas!')


    ## Huevear al mati
    if str(message.author) == 'Chukao#9321':
        if message.content.startswith('!p'):
            await message.channel.send('denuevo anda poniendo música este perkin ql del mati')

        emoji = '\U0001f44e'
        await message.add_reaction(emoji)

        if (random.uniform(1, 100) < 5):
            await message.channel.send('Mati son pocas veces las que digo algo así, pero la verdad es que te amo y por eso te molesto :hearts:')

    ## Especial para el baf
    if str(message.author) == 'Báfian#7700':
        
        emoji = '\U0001f44d'
        await message.add_reaction(emoji)
        
        if (random.uniform(1, 100) > 90):
            await message.channel.send('me encanta como escribe el Báf')


    ## Saludo genérico que no se usará realmente creo lol
    if message.content.startswith('$hello'):
        await message.channel.send('Hola humano!')

    await bot.process_commands(message)



# Comandos
@bot.command()
async def espejo(ctx,arg):
    await ctx.send(arg)


@bot.command()
async def define(ctx, arg):
    data = requests.get('http://dle.rae.es/srv/search?w=' + arg)
    rawHTML = data.text[:1000]
    description = re.findall(
        r'name="description" content="(.*?)\">', rawHTML)[0]
    await ctx.send(description)





## Correr server con nuestro token
bot.run(environ.get('TOKEN'))

