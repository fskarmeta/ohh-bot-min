## About

Ohh Bot ! Es un bot para la pequeña comunidad de amigos del canal "El lolete" en discord. Empecé a trabajar en el Bot a comienzos de Abril.
Esta escrito sobre la librería discord.py, corre en un servidor de Heroku y usa MongoDB Atlas como base de datos.


## Instrucciones básicas para hacerlo correr localmente.

1) Crear carpeta en tu pc, entrar a ese path y clonar projecto:
`$ git clone <url> `

2) Crear documento local ".env" e ingresar los siguientes campos:  

`TOKEN = '' //Token de tu bot en discord`    
`DB_USER = '' //Nombre de usuario MongoDB`  
`DB_PASS = '' //Clave usuario MongoDB`  
`DB_CLUSTER = '' //Cluster en MongoDB`    
`DB_DB = '' //Base de datos MongoDB`

Recomiendo tener un server de testeo/dev en discord con estos campos dedicado especialmente a ello. Y a su vez, tener los campos para producción como variables ambientales en el servidor.


3) Empezar shell del ambiente virtual:
`pipenv shell`

4) Instalar librerías que se usan en el projecto del Pipfile:
`pipenv install`

5) Se puede correr el código con `pipenv run python app.py` pero hay un shortcut:
`pipenv run start`


Con esto se debería levantar el test Bot en el test server

## Agregar librerías

Si deseas agregar alguna librería e importarla es necesario instalarla, por ejemplo:
`pipenv install pandas`


## Cometer el código a producción

Si se agregaron librerías nuevas es importante actualizar el requirements.txt para que el server los instale, esto es correr:
`pipenv lock -r > requirements.txt`

Asegurar que tu código este al día y resolver conflictos antes del commit
`git pull origin master`

Si todo esta bien:
`git add .`
`git commit -m "tu mensaje"`
`git push origin master`



## Extra

Para correr FFmpeg en Herouko se incluyeron dos custom builds aparte del build de python, en este orden:

https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest.git  
heroku/python  
https://github.com/xrisk/heroku-opus.git

## Otros

Agunos canales del script están hardcodeados y pensandos solo para el canal en el que corre el bot actualmente.
Contribuciones son bienvenidas, si tienes dudas o quieres sumarte al proyecto, me puedes encontrar en discord bajo "Báfian#7700"

English version coming soon.


# Commandos

## Música
#join | entra al canal de voz
#leave | sale del canal de voz
#play url_de_youtube | toca canción de youtube
#stop para canción
#pause detiene canción
#resume continúa reproducción

## Scripts

#define una_palabra | trae una defición de la palabra desde la rae con un web scraping  

#tiempo | consume una api para crear un dibujo del clima con un .txt más los datos.  

#ranking | entrega el ranking de puntos actual de los usuarios  

#lol baf | Invita a amigos más cercanos de Báfian -yo- a jugar.  

#lol elo | Invita a todos los usuarios pertenecientes de una categoría a jugar.  

#premios | Indica información sobre premios por cantidad de puntos.  

#borrar X | Donde X es un numero: Borrará los últimos X mensajes del bot en el chat.  

#borrar X Y | Donde X es un numero y Y el nombre de un usuario: Borrar los últimos X mensajes de usuario Y en el chat.  

#cachipun | Empieza un juego de cachipun contra el bot  

#puntos | te da la cantidad de puntos que tienes  

#precio btc | Trae el precio en dolares de alguna criptomeda. Ej: btc, eth, ada  

#cambio CLP2USD | Pedir el tipo de cambio, puede ser cualquier moneda. Ej: EUR2USD  

#convertir 120000 CLP2USD | Covertir una cantidad de dinero a otra moneda. 

#covid pais | Data de covid, donde pais es el nombre de cualquier país en ingles.  


## Custom

El bot tiene scripts personalizador pasa saludar a usuarios específicos de distinta maneras.  

Saluda a las personas respondiendo a distintos tipos de saludos.  

Mencionar a cualquier usuario, o varios a la vez, y agregando "++" al final de mensaje de le dará un punto a el/los usuario/s. No sé puede dar más de un punto a un mismo usuario en un tiempo limite de 45 minutos.
Ejemplo: @Báfian ++