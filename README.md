

## Instrucciones.

1) Clonar Projecto:
`$ git clone <url> `

2) Crear documento local ".env" e ingresar:
`TOKEN = 'ODMwOTI3MTY0NTg0MDk5ODcw.YHNzOQ.2ZO98fsCaiINfDWDMtOU53nlvJs'`

3) Empezar shell el ambiente virtual:
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



