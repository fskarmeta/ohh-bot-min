import discord
from discord.ext import commands
import requests
import re
import random
import urllib.parse
from os import environ

intents = discord.Intents.default()  # Allow the use of custom intents
intents.members = True

bot = commands.Bot(command_prefix='#', case_insensitive=True, intents=intents)



@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


# @bot.event
# async def on_message(message: discord.Message):
#     baf = bot.get_user(215721755380154369)
#     if message.guild is None and not message.author.bot:
#         await baf.send(message.content)
#     await bot.process_commands(message)
                
# cuando urre entra al canal de truchaaa
@bot.event
async def on_voice_state_update(member, before, after):
    channel = bot.get_channel(399419563625676831)
    if str(member) == "Trucho#6631" and str(after.channel.id) == "785246386408128605":
        urre = ("esa truchazo que se va a jugar hoy", "que rico tenerte aca truchita", "llego el master dic", "que onda urre su lol o codeo hoy?", "wena urre", "a no!")
        mensaje = random.choice(urre)
        await channel.send(mensaje)
    if str(member) == "Báfian#7700" and str(after.channel.id) == "785246386408128605":
        await channel.send("wena llego el baf")
    if str(member) == "Chukao#9321" and str(after.channel.id) == "785246386408128605":
        mati = ("yupiii llegó el mati", "llegó el breaking bad", ":pill: llegó toda la química al canal :D", "que onda mati, sea of thieves, rocket, o lolcito?", "cómo estuvo el lab bro?", "wena rucio ql", "saquense uno que llegó el matiiiiii", "hi mister matias")
        mensaje = random.choice(mati)
        await channel.send(mensaje)

## Lectura de mensajes
@bot.event
async def on_message(message):
    
    ## Si mensaje es el mismo bot
    if message.author == bot.user:
        return

    ## pin pong   
    if message.content == "ping":
        await message.channel.send('pong')


    #llamar medico
    if message.content == "medic!":
        await message.channel.send('@aweonaoql @Gallardo necesitamos un doctoorrrrrrrr :medical_symbol: !!')


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
        
        if random.uniform(1, 100) > 60:	
            heart = '\U0001f496'
            await message.add_reaction(heart)

        if random.uniform(1, 100) < 5:
            await message.channel.send('Mati son pocas veces las que digo algo así, pero la verdad es que te amo y por eso te molesto :hearts:')

    ## Especial para el baf
    if str(message.author) == 'Báfian#7700':
        
        emoji = '\U0001f44d'
        await message.add_reaction(emoji)
        
        if (random.uniform(1, 100) > 95):
            await message.channel.send('me encanta como escribe el Báf')


    ## Saludo genérico que no se usará realmente creo lol
    if message.content.startswith('$hello'):
        await message.channel.send('Hola humano!')


    baf = bot.get_user(215721755380154369)
    if message.guild is None and not message.author.bot:
        await baf.send(str(message.author) + " me dijo: " + message.content)


    await bot.process_commands(message)



# Comandos
@bot.command()
async def espejo(ctx,arg):
    await ctx.send(arg)


@bot.command()
async def define(ctx, arg):
    search = urllib.parse.quote(arg)
    data = requests.get('http://dle.rae.es/srv/search?w=' + search)
    rawHTML = data.text[:1000]
    description = re.findall(
        r'name="description" content="(.*?)\">', rawHTML)[0]

    if description.split()[0] == "Versión":
        await ctx.send("Esa palabra no exíste aprende a escribir aweonaoql")
    else:
        await ctx.send(description)

@bot.command()
async def borrar(ctx, limit=5, member: discord.Member=None):
    await ctx.message.delete()
    msg = []
    usuario = member
    if not member:
        usuario = bot.user
    try:
        limit = int(limit)
    except:
        return await ctx.send("Pasa un número como primer argumento y el nombre como segundo")
    async for m in ctx.channel.history():
        if not member:
            if len(msg) == limit:
                break
            if m.author == bot.user:
                msg.append(m)
            await ctx.channel.delete_messages(msg)
        else:
            if len(msg) == limit:
                break
            if m.author == member:
                    msg.append(m)
            await ctx.channel.delete_messages(msg)
    await ctx.send(f"Se han borrado los últimos {limit} mensajes de {usuario}", delete_after=3)

@bot.command()
async def lol(ctx, arg):
    baf = bot.get_user(215721755380154369)
    mati = bot.get_user(289241705989799946)
    urre = bot.get_user(308080160068861953)
    blame = bot.get_user(317878217086074882)
    hazer = bot.get_user(438518298129334284)

    if str(arg) == "baf":
        await baf.send('el baf te esta invitando a jugar lol :d')
        await mati.send('el baf te esta invitando a jugar lol :d')
        await urre.send('el baf te esta invitando a jugar lol :d')
        await blame.send('el baf te esta invitando a jugar lol :d')
        await hazer.send('el baf te esta invitando a jugar lol :d')
    
    if str(arg) == "elo":
        role = discord.utils.get(ctx.message.guild.roles, name="EloBooster")
        target = role.members
        for person in target:
            await person.send('los cabres en el lolete te están invitando a jugar :d')

    # if str(arg) == "test":
    #     await baf.send('👀')

## Correr server con nuestro token
bot.run(environ.get('TOKEN'))

