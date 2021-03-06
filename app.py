import discord
from discord.ext import commands
import requests
import re
import json
import random
import urllib.parse
import youtube_dl
import os
import time
from helpers import get_or_create_user, update_timestamp, decir_puntaje, compute_score, compute_winner
import datetime
import pymongo
import pycountry
from pymongo import MongoClient
from os import environ

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='#', case_insensitive=True, intents=intents)

db_connection_string = f"mongodb+srv://{environ.get('DB_USER')}:{environ.get('DB_PASS')}@{environ.get('DB_CLUSTER')}.wppvi.mongodb.net/{environ.get('DB_DB')}?retryWrites=true&w=majority"


@bot.event
async def on_ready():
    print(discord.version_info)
    print('We have logged in as {0.user}'.format(bot))


@bot.event
async def on_message(message: discord.Message):
    baf = bot.get_user(215721755380154369)
    if message.guild is None and not message.author.bot:
        await baf.send(message.content)
    await bot.process_commands(message)
                
#cuando urre entra al canal de truchaaa
# @bot.event
# async def on_voice_state_update(member, before, after):
#     channel = bot.get_channel(399419563625676831)
#     if str(member) == "Trucho#6631" and str(after.channel.id) == "785246386408128605":
#         urre = ("esa truchazo que se va a jugar hoy", "que rico tenerte aca truchita", "llego el master dic", "que onda urre su lol o codeo hoy?", "wena urre", "a no!", "dic")
#         mensaje = random.choice(urre)
#         await channel.send(mensaje)
#     # if str(member) == "Báfian#7700" and str(after.channel.id) == "785246386408128605":
#     #     await channel.send("wena llego el baf")
#     if str(member) == "Chukao#9321" and str(after.channel.id) == "785246386408128605":
#         mati = ("yupiiii llegó el mati", "llegó el breaking bad", ":pill: llegó toda la química al canal :D", "que onda mati, sea of thieves, rocket, o lolcito?", "cómo estuvo el lab bro?", "wena rucio ql", "saquense uno que llegó el matiiiiii", "hi mister matias")
#         mensaje = random.choice(mati)
#         await channel.send(mensaje)

## Lectura de mensajes
@bot.event
async def on_message(message):

    # dar puntos
    mentioned = message.mentions
    if mentioned:
        if ("++" in message.content):
            waiting_time = 2700
            client = MongoClient(db_connection_string, ssl=True)
            db = client['discord']
            collection = db['users']
            currentUser = get_or_create_user(collection, str(message.author.id))
            for member in mentioned:
                if str(message.author.id) != str(member.id):
                    user = collection.find_one({"_id": str(member.id)})
                    if user:
                        last_time = currentUser['points_given'].get(str(member.id), 0)
                        if last_time:
                            current_time = time.time()
                            dif = current_time - last_time
                            if dif < waiting_time:
                                value = datetime.datetime.fromtimestamp(dif)
                                await message.channel.send(f"Han pasado {value.strftime('%M:%S')} minutos desde que diste el último like a {str(member.name)}, espera 45 minutos amigue.")
                            else:
                                collection.update_one({"_id": str(member.id)}, {"$inc": { "points" : 1} }, upsert=True)
                                await message.channel.send(f"{str(member.name)} tiene {user['points'] + 1} puntos ahora!")
                                update_timestamp(currentUser,str(message.author.id),str(member.id), collection)
                        else:
                            collection.update_one({"_id": str(member.id)}, {"$inc": { "points" : 1} }, upsert=True)
                            await message.channel.send(f"{str(member.name)} tiene {user['points'] + 1} puntos ahora!")
                            update_timestamp(currentUser,str(message.author.id),str(member.id), collection)
                    else:
                        collection.update_one({"_id": str(member.id)}, {"$inc": { "points" : 1}, "$set": { 'points_given': {} } }, upsert=True)
                        await message.channel.send(f"{str(member.name)} tiene su primer punto :d!")
                        update_timestamp(currentUser,str(message.author.id),str(member.id), collection)
                else:
                    await message.channel.send("el loco barsa")
            client.close()



    
    ## Si mensaje es el mismo bot
    if message.author == bot.user:
        return

    ## pin pong   
    if message.content == "ping":
        await message.channel.send('pong')


    #llamar medico
    if message.content == "medic!":
        aweonao = bot.get_user(339136505723224066)
        gallardo = bot.get_user(341719443258343434)
        await message.channel.send(f"{aweonao.mention} {gallardo.mention} necesitamos un doctoorrrrrrrrr :medical_symbol: !!")


    ## Operaciones sobre el contenido
    content = message.content.split(" ")
    ## Procesamientos del cotenido
    saludos = ("hola", "holi", "buenas", "hello", "qué tal", "wena")

    ### Saludos
    if any(saludo in content for saludo in saludos):
        if str(message.author) == 'Trucho#6631':
            await message.channel.send('esa truchazo usted sabe, py love for you :hearts:')
        else:
            await message.channel.send('buenas buenas! :d')


    ## Huevear al mati
    if str(message.author) == 'Chukao#9321':
        if message.content.startswith('!p'):
            await message.channel.send('denuevo anda poniendo música este perkin')

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


    if message.content == "piedra" or message.content == "tijera" or message.content == "papel":
        id = str(message.author.id)
        username = str(message.author.name)
        player_choice = message.content
        opts = ['piedra', 'papel', 'tijera']
        try:
            game_finished = False
            with open(f'game_{id}.txt') as json_file:
                game = json.load(json_file)
                bot_pick = random.choice(opts)
                await message.channel.send(f"El bot seleccionó {bot_pick}, {username} seleccionó {player_choice}")
                updatedGame = compute_score(bot_pick, player_choice, game)
                await message.channel.send(decir_puntaje(updatedGame))
                winner = compute_winner(updatedGame)
                if (winner):
                    client = MongoClient(db_connection_string, ssl=True)
                    db = client['discord']
                    collection = db['users']
                    currentUser = get_or_create_user(collection, str(message.author.id))
                    if (winner == "Bot"):
                        collection.update_one({"_id": id}, {"$inc": { "points" : -1} }, upsert=True)
                        await message.channel.send(f"Gané, perdiste {username}. Te quité un punto :rofl:")
                    else:
                        collection.update_one({"_id": id}, {"$inc": { "points" : 1} }, upsert=True)
                        await message.channel.send(f"Has ganado {username}!!! Te he dado un punto :D :star:")
                    game_finished = True
                    client.close()
                else:
                    with open(f'game_{id}.txt', 'w') as outfile:
                        json.dump(updatedGame, outfile)
            if game_finished:
                os.remove(f'game_{id}.txt')
        except:
            await message.channel.send(f"{username} no tienes un cachipun andando, empieza uno con #cachipun")


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
        await ctx.send("Esa palabra no exíste, aprende a escribir.")
    else:
        await ctx.send(description)

@bot.command()
async def precio(ctx, arg):
    resp = requests.get(f'https://api.kraken.com/0/public/Ticker?pair={arg.upper()}USD')
    data = resp.json()
    if len(data['error']) > 0:
        await ctx.send("No encontré esa criptomoneda bro.")
    else:
        lista = list(data["result"].keys())[0]
        price = data["result"][lista]['a'][0]
        await ctx.send(f"${float(price)}")

@bot.command()
async def cambio(ctx, arg):
    coins = arg.split('2')
    if len(coins) != 2:
        await ctx.send('Formato incorrecto bra. Ejemplo correcto: #cambio USD2CLP')
    else:
        resp = requests.get(f"https://free.currconv.com/api/v7/convert?q={coins[0].upper()}_{coins[1].upper()}&compact=ultra&apiKey={environ.get('CCA_TOKEN')}")
        data = resp.json()
        if data:
            await ctx.send(str(list(data.values())[0]))
        else:
            await ctx.send("Una de esas monedas no existe my bro")

@bot.command()
async def convertir(ctx, *arg):
    if len(arg) != 2:
        await ctx.send('Formato incorrecto bra. Ejemplo: #convertir 120000 CLP2USD')
    coins = arg[1].split('2')
    try:
        amount = float(arg[0])
        resp = requests.get(f"https://free.currconv.com/api/v7/convert?q={coins[0].upper()}_{coins[1].upper()}&compact=ultra&apiKey={environ.get('CCA_TOKEN')}")
        data = resp.json()
        if data:
            await ctx.send(str(round((float(list(data.values())[0]) * amount), 2)) + str(coins[1].upper()))
        else:
            await ctx.send("Una de esas monedas no existe my bro")
    except:
        await ctx.send('Formato incorrecto bra. Ejemplo: #convertir 120000 CLP2USD. Probablemente el monto que pusiste conllevó al error.')

@bot.command()
async def covid(ctx, arg):
    country = arg.capitalize()
    try:
        iso = ''
        try:
            iso = pycountry.countries.get(common_name=country).alpha_3
        except:
            iso = pycountry.countries.get(name=country).alpha_3
        url = f"https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/npm-covid-data/country-report-iso-based/{country}/{iso}"
        headers = {
            'x-rapidapi-key': environ.get('X_RAPI_KEY'),
            'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
            }
        response = requests.request("GET", url, headers=headers)
        data = response.json()[0]
        await ctx.send(f"""
        ```
        Pais: {data['Country']}
        Población: {data['Population']}
        Positividad: {data['Infection_Risk']}%
        Tasa de Fatalidad: {data['Case_Fatality_Rate']}%
        Porcentaje de Testeo: {data['Test_Percentage']}%
        Porcentaje Personas Recuperadas: {data['Recovery_Proporation']}%
        Casos Totales: {data['TotalCases']}
        Casos Nuevos: {data['NewCases']}
        Muertes Totales: {data['TotalDeaths']}
        Muertes Nuevas: {data['NewDeaths']}
        Total de Recuperados: {data['TotalRecovered']}
        Nuevos Recuperados: {data['NewRecovered']}
        Casos Activos: {data['ActiveCases']}
        Cantidad de Testeos: {data['TotalTests']}
        Un Caso Cada X Personas: {data['one_Caseevery_X_ppl']}
        Una Muerte Cada X Personas: {data['one_Deathevery_X_ppl']}
        Una Test Cada X Personas: {data['one_Testevery_X_ppl']}
        Muertes por Millon de Personas: {data['Deaths_1M_pop']}
        Personas Seriamente Críticas: {data['Serious_Critical']}
        Test por Millon de Personas: {data['Tests_1M_Pop']}
        Total de Casos por Millon de Personas: {data['TotCases_1M_Pop']}
        Datos recopilados desde: https://vaccovid.live/
        ```
        """)
    except:
        await ctx.send("Pais no existe, formato incorrecto bra o error de servidor. Prueba #covid chile")



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
async def tiempo(ctx):
    headers_dict = {'Accept': '*/*', 'User-Agent': 'curl/7.43.0'}
    data = requests.get('http://wttr.in/$santiago.chile?m', headers=headers_dict)

    def strip_ansi_codes(s):
        return re.sub('\033\\[([0-9]+)(;[0-9]+)*m', '', s)

    with open("weather.txt", "w", encoding="utf-8") as file:
        file.write(strip_ansi_codes(data.text))

    with open("weather.txt", "rb") as file:
        await ctx.send("El tiempo en santiago:", file=discord.File(file, "tiempo.txt"))


@bot.command()
async def lol(ctx, arg):
    baf = bot.get_user(215721755380154369)
    mati = bot.get_user(289241705989799946)
    urre = bot.get_user(308080160068861953)
    blame = bot.get_user(317878217086074882)
    hazer = bot.get_user(438518298129334284)
    newton = bot.get_user(234510282079207424)

    if str(arg) == "baf":
        await baf.send('el baf te esta invitando a jugar lol :d')
        await mati.send('el baf te esta invitando a jugar lol :d')
        await urre.send('el baf te esta invitando a jugar lol :d')
        await blame.send('el baf te esta invitando a jugar lol :d')
        await hazer.send('el baf te esta invitando a jugar lol :d')
        await newton.send('el baf te esta invitando a jugar lol :d')
    
    if str(arg) == "elo":
        role = discord.utils.get(ctx.message.guild.roles, name="EloBooster")
        target = role.members
        for person in target:
            await person.send('los cabres en el lolete te están invitando a jugar :d')


@bot.command()
async def mati(ctx, arg):
    if str(arg) == 'test':
        await ctx.send('Primer codigo del mati')

@bot.command()
async def premios(ctx):
        await ctx.send(f'Premio n°1: Al alcanzar 100 puntos te dare una merecida recompensa, top secret. Esto es 100% real! ')

@bot.command()
async def ranking(ctx):
        l = ["Primer lugar", "Segundo Lugar", "Tercer Lugar", "Cuarto Lugar", "Quinto Lugar"]
        client = MongoClient(db_connection_string, ssl=True)
        db = client['discord']
        collection = db['users']
        docs = collection.find()[:5].sort('points', pymongo.DESCENDING)
        i = 0
        for doc in docs:
            user = bot.get_user(int(doc['_id']))
            await ctx.send(l[i] + ": " + str(user.name) + " con " + str(doc['points']) + " puntos.")
            i+=1
        client.close()
        

#Para que el bot pueda entrar a un canal de voz usando el comando #join
@bot.command(pass_context = True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("No estas en un canal de voz, debes estar en un canal de voz para usar este comando")

#Para que el bot pueda salir del canal de voz suando el comando #leave
@bot.command(pass_context = True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send("No estoy en un canal de voz")
        


@bot.command()
async def play(ctx, url: str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            print("Hay canción")
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Espera que termine la canción o usa el commando #stop")
        return

    voiceChannel = ctx.message.author.voice.channel
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice is None or not voice.is_connected():
        await voiceChannel.connect()
    

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],  
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            print("Encontro file .mp3")
            os.rename(file, "song.mp3")

    voice.play(discord.FFmpegPCMAudio("song.mp3"))


@bot.command()
async def pause(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send('No hay audio sonando.')

@bot.command()
async def resume(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send('E audio no esta en pausa.')

@bot.command()
async def stop(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    voice.stop()


@bot.command()
async def cachipun(ctx):
    id = str(ctx.message.author.id)
    username = str(ctx.message.author.name)
    try:
        with open(f'game_{id}.txt') as json_file:
            await ctx.send(f"Ya tienes un juego andando {username}! Dí piedra, papel o tijera")
    except:
        await ctx.send(f"Empezando un nuevo cachipun contra {username}! Escribe papel, piedra o tijera")
        game = {}
        game['player'] = 0
        game['bot'] = 0
        print(decir_puntaje(game))
        with open(f'game_{id}.txt', 'w') as outfile:
            json.dump(game, outfile)


@bot.command()
async def puntos(ctx):
    id = str(ctx.message.author.id)
    username = str(ctx.message.author.name)
    client = MongoClient(db_connection_string, ssl=True)
    db = client['discord']
    collection = db['users']
    user = collection.find_one({"_id": id})
    if user:
        await ctx.send(f"{username} tiene {user['points']} puntos!")
    else:
        await ctx.send(f"No haber registro para {ctx.message.author.name}")
    client.close()
## Correr server con nuestro token
bot.run(environ.get('TOKEN'))