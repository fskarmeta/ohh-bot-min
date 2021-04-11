import requests
import re
import random
import discord

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    print(message.author)
    if message.author == client.user:
        return

    args = message.content.split(" ")
    saludos = ("hola", "holi", "buenas", "hello")

    if any(saludo in args for saludo in saludos):
        if str(message.author) == 'Trucho#6631':
            await message.channel.send('esa truchazo usted sabe, py love for you :hearts:')
        else:
            await message.channel.send('buenas buenas!')

    if str(message.author) == 'Chukao#9321' and message.content.startswith('!p'):
        await message.channel.send('denuevo anda poniendo música este perkin ql del mati')

    if message.content.startswith('$dic') and len(args) == 2:
        word = args[1]
        data = requests.get('http://dle.rae.es/srv/search?w=' + word)
        rawHTML = data.text[:1000]
        description = re.findall(
            r'name="description" content="(.*?)\">', rawHTML)[0]
        await message.channel.send(description)

    if str(message.author) == 'Báfian#7700':
        if (random.uniform(1, 100) > 90):
            await message.channel.send('me encanta como escribe el Báf')

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


client.run('ODMwNjE5MzIyNTMwNTI5MzMw.YHJUhg.MtAZNWbtffwJ7cVIK-umT4tQtpk')
