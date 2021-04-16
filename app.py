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
        await message.channel.send('@aweonaoql @Gallardo necesitamos un doctoorrrrrrrr :medical_symbol !!: ')


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
        
        if (random.uniform(1, 100) > 95):
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
    if str(arg) == "baf":
        baf = '<@215721755380154369>'
        mati = '<@308080160068861953>'
        urre = '<@308080160068861953>'
        blame = '<@317878217086074882>'
        hazer = '<@438518298129334284>'
        await ctx.send("a jugar un aramcillo cabres " + baf " " + mati + " "  + urre + " " + blame + " " + hazer)
    
    if str(arg) == "elo":
        role = discord.utils.get(ctx.message.guild.roles, name="EloBustiado")
        target = role.members
        for person in target:
            await ctx.send("a jugar lolcillo " +  person.mention)




## Correr server con nuestro token
bot.run(environ.get('TOKEN'))

