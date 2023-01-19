## NPM 
Instalacion de Node Js 

1. node -v
2. npm -v

***Actualiza a la ultima version***
~~~
npm install npm@latest -g 
~~~

## actualizamos Python a la version 3.10

> actualizando pip

~~~
python3 -m pip install --upgrade pip
~~~

~~~
python -m pip install -U pip 
~~~

debemos de descargar la version desde la pagina 3.10 

1. luego debemos descomprimir 
2. tar xf python-3.10
3. entramos a la carpeta
4. ./configure
5. make
6. sudo make install

### Iniciar un proyecto 
dentro de nuestra carpeta local 

1. git init (que inicializara git)
2. npm init (inicializamos nuestro proyecto)
3. configuramos

~~~
    New major version of npm available! 6.14.4 → 7.6.3       
  Changelog: https://github.com/npm/cli/releases/tag/v7.6.3 
            Run npm install -g npm to update!
~~~

Shortcuts
1. npm init -y (agrega configuracion minima)

Agregar datos de configuracion por defecto <br> 
cada vez que iniciemos algun proyecto
1. npm set init.author.email "0sound@gmail.com" 
2. npm set init.author.name "CRKJ"
3. npm set init.license "MIT"

### Instalacion de dependencias 
raiz del proyecto
1. src/index.js

flag
--save (En produccion) <br>
--save-dev (En desarrollo) <br> ***(dependencia de desarrollo)***

agregamos nuestro primer paquete, manejador de fechas <br>
apartir de la version 5 todos los package viene por defecto como dependencia de produccion

- npm install moment

que crea nuestra dependencia

1. node_modules
	- se instalaran los modules que estamos utilizando en nuestro proyecto
	- debemos ignorarla apenas se crea, ya que no debe ser enviada a ningun repositorios
	- .gitignore => node_modules/
	- npm i moment -S (dependencia)
	- npm i moment -D (desarrollo)

2. package-lock.js

#### Instalacion de paketes de forma global
paquete requerido de forma global

- nodemon
- npm i -g nodemon
- npm install eslint -O ***(-O opcional)***

para ver la lista de todos los paquetes instalados usamos, y la profundidad
~~~
npm list -g --depth 0
npm install eslint -O
~~~

para ver
- npm fund ***muestra que son fundaciones que requieren financiamiento***

### Instalacion de dependencias con force

esta forma me informa que podria instalar el paquete
- npm install react --dry-run

forzar la instalacion
- npm install webpack force
- npm install webpack -f

Vuelve a installar todo lo que este en package.json
- npm install

Si vamos a instalar la version especifica de un paquete 
- npm install json-server@0.15.0

### Actualizar dependencias 
listar los paquetes del proyecto
- npm list

Mirar que package esta desactualizado
- npm outdate

outdate mas detallada
- npm outdate --dd

actualizar la ultima version
npm json-server@latest

Desinstalar el paquete, y quita todos los archivos del proyecto
- npm uninstall json-server

Desinstalar pero sin quitarlo del package.json
- npm uninstall webpack --no-save

valida la instalacion de paquetes y avisa si no esta instalado
npm egamma 

### versionado semantico y package-lock.json

git clone https://github.com/pinkylin/script.git

versionado
3 9 2 -> 
clasificacion del versionado
3 major => cambios mayores
9 minor => actualizacion menores
2 patch => parches o bugfix

^ este carete se debe eliminar para que este siempre estable nuestro proyecto

### Ejecutar tareas 

Los script son comandos para ejecutar desde consola <br>
ejemplo:
~~~
"Scripts" : {
	"Hola" : "node",
	"deploy" : "npm run format && npm run build "
}
~~~
Ejecuto en consola 
~~~
npm run hola
~~~
Esto hace la funcion de alias acortando los comandos que necesitemos ejecutar
___

### Solucion a problemas
Errores de configuracion, espacios, typo, mal configurado de .json

Como Solucionar?

podemos ver con este comando detalladamente los que va ejecutando, modo verbose
~~~
npm run build --dd
~~~
con esto podemos debuggear, para saber donde esta el error

~~~
A complete log of this run can be found in:
> /user/crkj/.npm/_logs/2019-11-20T16_48_30_499Z-debug.log
~~~

#### eliminar el cache de la consola 
Limpieza de cache 
- npm cache clean --force

Verificamos el cache
- npm cache verify

Si no estan bien instaladas las dependencias lo mejor es borrar las dependencias, en node_modules, con el comando
- rm -rf node_modules

luego volvermos a ejecutar npm install y volvera a instalar los paquetes

Desintalacion eliminando la carpeta de node_modules <br> con el paquete de forma global con rimraf <br> para todos los sistemas operativos

~~~
sudo npm install -g rimraf
~~~

Otra forma de eliminar, con rimraf
~~~
rimraf node_modules
~~~

### Seguridad
la seguridad depende de nosotros, y depende de nosotros que nuestro proyecto cumpla el estandar

auditoria:
~~~
npm audit
~~~

en formato json
~~~
npm audit --json
~~~

Actualizar el package que tiene vulneravilidad, ejemplo eslint-utils
~~~
npm update selint-utils --depth 2
~~~

Comando para reparar de una vez todos los packages de npm
~~~
npm audit fix
~~~

### Crear un paquete para NPM

random de mensajes

1. mkdir random-messages
2. git init
3. npm init
4. entry point: (index.js) src/index.js
5. src/index.js

>### index.js
~~~
const messages = [
	"Oscar",
	"Ana",
	"Jessica",
	"Nicolas",
	"Laura"
];

const randomMsg = () => {
	const message = messages[Math.floor(Math.random() * messages.length)];
	console.log(message);
};

module.exports = { randomMsg };
~~~

6. vamos crear una nueva carpeta bin
 
> ### global.js

~~~
#!/usr/bin/env node

let random = require('../src/index.js');

random.messageMsg();
~~~

7. en package.json

creamo un apartado 
~~~
{
	"bin":{
		"random-msg" : "./bin/global.js"
	},
	"preferGlobal" : true,
}
~~~

### Publicar el paquete en NPM

debemos comprobar de manera local

/random-messages
~~~
sudo npm link
~~~
1. debemos crear una cuenta para publicar
2. inicia sesion
3. desde la terminal
4. npm adduser
user: <br>
pass: <br>
5. npm publish
6. listo
7. en la cuenta en lo packages, ya podemos ver el paquete

### Paquetes privados
debemos crear un buen README.md <br>
se debe tener el proyecto en el repositorio <br>
debe estar en el estandar en ingles <br>
pruebas unitarias con jest <br>
npm init, cuando ya esta configurado en el repositorio <br>
npm version patch, cuando actualizamos <br>

cursos recomendados
1. Backend con Node
2. Prework y buenas practicas
