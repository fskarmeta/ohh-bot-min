import discord
import requests
import re
import random
from os import environ

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))



## Lectura de mensajes
@client.event
async def on_message(message):
    
    ## Si mensaje es el mismo bot
    if message.author == client.user:
        return

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

    ## Definición de diccionario
    if message.content.startswith('$dic') and len(content) == 2:
        word = content[1]
        data = requests.get('http://dle.rae.es/srv/search?w=' + word)
        rawHTML = data.text[:1000]
        description = re.findall(
            r'name="description" content="(.*?)\">', rawHTML)[0]
        await message.channel.send(description)
    
    ## Especial para el baf
    if str(message.author) == 'Báfian#7700':
        if (random.uniform(1, 100) > 90):
            await message.channel.send('me encanta como escribe el Báf')


    ## Saludo genérico que no se usará realmente creo lol
    if message.content.startswith('$hello'):
        await message.channel.send('Hola humano!')


## Correr server con nuestro token
client.run(environ.get('TOKEN'))

