# NodeJs by EDteam 2021

## Modulo 1 ¿Que es NodeJs
motor v8 de chrome para que corra fuera del navegador  
manejo de archivos desde el servidor  
un solo hilo de ejecucion, lo que permite mayor escalabilidad  
NPM manejador de paquetes  

### Instalación de NodeJs 
despues de la instalación  
node -v  
npm -v  

### Hola Mundo desde NodeJs
node index.js  
~~~ 
console.log("Hola Mundo")  
~~~
node  
2+2  

### NPM de NodeJs 
npmjs.com  
npm init --y  

### ejecutar con node y/o npm desde la consola
node index.js  
npm start  
~~~
"script": {
  start: "node index.js"
}
~~~

### Instalar un modulo
npm install hola-mundo-nodejs  
~~~
function mensaje() {
  return "Hola Mundo"
}
module.exports = {
  mensaje
}
~~~

### importar el modulo y ejecutar la funcion del modulo importado
~~~
const hola_mundo = require('./hola-mundo-nodejs')  
console.log( hola_mundo.mensaje() )
~~~

### modulo nodemon para desarrollo
modulo que reinicia el servidor, cuando detecta cambios en el archivo  
~~~
nmp install nodemon -D 
~~~

### Script para ejecutar nodemon
~~~
"script": {
  server: "nodemon index.js"
}
~~~

## Modulo 2 Servidor http con NodeJs
http es un protocolo que nos va a permitir el envio de archivos desde nuestro servidor al navegador  

### Crear Servidor desde cero SIN Express
servidor sin respuesta al navegador  
~~~
const http = require('http')
const server = http.createServer()
const port = 3000
server.listen(port)
console.log('servidor corriendo en el localhost:',port)
~~~

### Enviar una respuesta al navegador desde el servidor 

~~~
const http = require('http')
const server = http.createServer(onRequire)
server.listen(3000)
console.log('se levanta servidor desde cero')

function onRequire (require, response) {
  console.log('peticion al servidor')
}
~~~

# Require (req)
el contenido de ***require***, es toda la informacion de la petición que esta recibiendo el servidor   
~~~
console.log(require)
~~~
podemos ver a los diferentes metodos que tenemos de la peticion

|metodos||
|-|-|
|url|
|method|
|headers|
|headers|host|

Hay que seguir explorando los metodos que nos trae el require (req)  

# Response (res)
vamos a responder a las peticiones en la cabecera de la página, con texto plano  

### instrucciones
respondiendo con texto plano al navegador
~~~
function onRequire (require, response) {
  console.log('peticion al servidor')
  response.setHeader('Content-type', 'text/plain')
  response.write('Bienvenido a mi web desde nodeJs')
  response.end()
}
~~~

# Code en texto plano
entregamos texto plano, con los stylos del navegador
~~~
const http = require('http')
const server = http.createServer(onRequire)
const port = 3000

server.listen(port, () => {
  console.log(`se levanta servidor desde cero en http://localhost:${port}`)
})

function onRequire (req, res) {
  console.log('peticion al servidor')
  res.setHeader('Content-type', 'text/plain')
  res.write('Bienvenido a mi web desde nodeJs por el puerto: '+port)
  res.end()
}
~~~

# Code en HTML
entregamos el html en la peticion al servidor
~~~
const http = require('http')
const server = http.createServer(onRequire)
const port = 3000

server.listen(port, () => {
  console.log(`se levanta servidor desde cero en http://localhost:${port}`)
})

function onRequire (req, res) {
  console.log('peticion al servidor')
  res.setHeader('Content-type', 'text/html')
  res.write('<h1>Bienvenido a mi web desde nodeJs por el puerto: '+port+'</h1>')
  res.end()
}
~~~

# Enviando archivos HTML y manejo de errores con codigo
leyendo html externo, con el modulo fs que ya trae NodeJs  
manejamos el setStatus con los codigos http  

~~~
const http = require("http");
const server = http.createServer(onRequire);
const port = 3000;
const fs = require("fs");

server.listen(port, () => {
  console.log(`se levanta servidor desde cero en http://localhost:${port}`);
});

function onRequire(req, res) {
  console.log("peticion al servidor: " + req.url);

  fs.readFile("index.html", (error, contenido) => {
    if (req.url == "/") {
      if (error) {
        if (error.code == ENOENT) {
          res.setStatus = 404;
          console.log("archivo no encontrado setStatus 404");
        } else {
          res.setStatus = 500;
          console.log("error en el servidor setStatus 500");
        }
      } else {
        res.setStatus = 202;
        res.setHeader("Content-type", "text/html");
        res.write(contenido);
        res.end();
      }
    } else if (req.url == "/users") {
      res.setHeader("Content-type", "text/html");
      res.write("<h1>contenido de usuarios</h1>");
      res.end();
    }
  });
}
~~~

# Métodos GET, PUT, DELETE, POST
vamos a ver los metodos que se van a manejar con POSTMAN  
creamos una coleccion, generamos los metodos con los que vamos a trabajar  
~~~
const http = require("http");
const server = http.createServer(onRequire);
const port = 3000;
const fs = require("fs");

server.listen(port, () => {
  console.log(`se levanta servidor desde cero en http://localhost:${port}`);
});

function onRequire(req, res) {
  console.log("peticion al servidor: " + req.url);

  fs.readFile("index.html", (error, contenido) => {
    if (req.url == "/") {
      if (error) {
        if (error.code == ENOENT) {
          res.setStatus = 404;
          console.log("archivo no encontrado setStatus 404");
        } else {
          res.setStatus = 500;
          console.log("error en el servidor setStatus 500");
        }
      } else {
        res.setStatus = 202;
        res.setHeader("Content-type", "text/html");
        res.write(contenido);
        res.end();
      }
    } else if (req.url == "/users") {
      if (req.method == "GET") {
        res.setHeader("Content-type", "text/html");
        res.write("<h1>Mostrando usuarios GET</h1>");
        res.end();
      } else if (req.method == "POST") {
        res.setHeader("Content-type", "text/html");
        res.write("<h1>Insertando usuarios</h1>");
        res.end();
      } else if (req.method == "PUT") {
        res.setHeader("Content-type", "text/html");
        res.write("<h1>Modificando usuarios</h1>");
        res.end();
      } else if (req.method == "DELETE") {
        res.setHeader("Content-type", "text/html");
        res.write("<h1>Eliminando usuarios</h1>");
        res.end();
      }
    }
  });
}
~~~

# POSTMAN 
1. post  
body + x-www-form-urlencoded  
aqui vamos a enviar llaves ***clave : valor***  
name : CRKJ  

2. Modulo para interpretar los datos y convertirlos a string  
~~~
const qs = require('querystring')  
~~~
Método POST con querystring
~~~
else if (req.method == "POST") {
  var datos = "";
  req.on("data", (d) => {
    datos += d;
  });
  req.on("end", () => {
    var post = qs.parse(datos);
    res.end("Datos recibidos: " + post.name);
  });
} 

else if (req.method == "PUT") {
  var datos = "";
  req.on("data", (d) => {
    datos += d;
  });
  req.on("end", () => {
    var post = qs.parse(datos);
    res.end("Datos recibidos: " + post.name);
  });
} 

else if (req.method == "DELETE") {
  var datos = "";
  req.on("data", (d) => {
    datos += d;
  });
  req.on("end", () => {
    var post = qs.parse(datos);
    res.end("Datos recibidos: " + post.name);
  });
}
~~~
3. asi podemos comprobar que los datos enviados por POSTMAN estan siendo recibidos  
  
# modulo 3 Express Framework
Express es un framework que facilita la creacion de servidores  

#### Ventajas de usar express
1. express uno de los mas usado
2. servidores http de forma sencilla
3. soporte de diferentes verbos GET, POST, PUT, DELETE 
4. soporta vistas
5. soporta middlewares (funciones para comprobar)
6. se instala via NPM

### por qué usar Express 
1. construcción de aplicaciones web más fácil
2. creacion de aplicaciones modernas
3. extremadamente rapido
4. más control en las rutas, peticiones y respuestas 

### Instalacion Express
1. npm install express 
2. npm install nodemon
3. /src/index.js
4. 
~~~
"script": {
  "server" : "nodemon src/index.js"
},
~~~

# Express
Creación de un servidor con express
~~~
// console.log("Hola Mundo Express")

const express = require('express')
const app = express()
const port = 3000 

// Routes
app.get('/', (req, res) => {
  res.send('Bienvenidos desde Express')
})

app.get('/users', (req, res) => {
  res.send('Desde users')
})

app.listen(port, () => {
  console.log('Server on', port)
})
~~~

### levantar el servidor 
Ejecutamos el script para levantar el servidor  
~~~
npm run server
~~~

## Routes (rutas con express)
Manejo de rutas  
1. /routes/users.js
~~~
const express = require('express')
const router = express.Router()

router.get('/users', (req, res) => {
  res.send('Desde users')
})

module.exports = router
~~~
2. importando el archivo de users con el que estamos manejando las rutas de usuarios  
~~~
const express = require('express')
const app = express()
const port = 3000
const user = require('./routes/users')

// Routes
app.get('/', (req, res) => {
  res.send('Bienvenidos desde Express')
})

// llamado de rutas de users al CRUD
app.use('/user', user)

app.listen(port, () => {
  console.log('Server on', port)
})
~~~

## controller/
Debemos dividir nuestras funciones de nuestras rutas, con el fin de controllar de manera mas facil  
y tener las rutas separadas en nuestra aplicación  
Esto lo hacemos enviando las funciones callback a nuestro controller de users  

### estructura
1. /routes/users.js 

~~~
const express = require('express')
const router = express.Router()
const usersController = require('../controller/users')

router.get('/all', usersController.getUsers)

router.get('/create', usersController.createUser)

router.get('/update', usersController.updateUser)

router.get('/delete', usersController.deleteUser)

module.exports = router
~~~

2. /controller/users.js
~~~
const getUsers = (req, res) => {
  res.send('Desde users')
}

const createUser = (req, res) => {
  res.send('Create users')
}

const updateUser = (req, res) => {
  res.send('Update users')
}

const deleteUser = (req, res) => {
  res.send('Delete users')
}

module.exports = {getUsers, createUser, updateUser, deleteUser } 
~~~

# Middleware 
Es una funcion que es ejecuta entre la peticion del usuario y antes de que el servidor retorne una respuesta  
Ejemplo de uso: para validar si el usuario esta logeado o no, para que pueda hacer los cambios  

~~~
const my_middleware = (req, res, next) => {
  console.log('ejecutando el middleware')
  next()
}
~~~
#### permiso para usar con Express 
~~~
app.use(my_middleware)
~~~

### Middleware isLogged
funcion para validar si esta loggeado el usuario  
~~~
const isLogged = (req, res, next) => {
  const logged = false
  if (logged) {
    next()
  } else {
    res.send("Usuario debe logearse para acceder a las rutas CRUD")
  }
}
exports.isLogged = isLogged
~~~

usar el login para bloquear rutas sin acceso autorizado

~~~
// Rutas de uso
app.use(logged.isLogged)
app.use('/users', user)
~~~

# Archivos estaticos 
para trabajar con archivos estáticos debemos usar el middleware que ya trae express  
~~~
app.use(express.static())
~~~
Todos estos archivos estaticos (html, js, css, imágenes, etc) seran guardados en la carpeta ***public***  
Esta carpeta se debe configurar para express.static reconozca el directorio con __dirname concatenado con la carpeta public   
~~~
app.use(express.static(__dirname+'/public'))
~~~

### Modulo Path
Otra forma de vincular los archivos estaticos es con el modulo ***Path***  
~~~
const path = require('path')

app.use(express.static(path.join(__dirname, 'public'))
~~~

### entregando HTML con sendFile
creamos un html por cada ruta que vamos a mostrar    
formularios para hacer nuestras consultas CRUD  
cambiamos el ***send*** por ***sendFile()***, que recibe 2 parámetros  
el archivo .html y un { root: 'rutaDelPath' }  
asi vemos como se relaciona el path __dirname y el archivo .html  

~~~
const path = require('path')
const root = path.join(__dirname, '../public')

app.get('/', (req, res) => {
  res.sendFile('all_users.html', {root: root})
})
~~~

## Views Configuracion y motores de vista
las views van dentro de src, no dentro de public   
estableciendo configuraciones en nuestra aplicacion de express, (settings)  
con esta configuracion adaptamos los valores como si fueran variables  
El ***view engine*** es el motor de plantillas que vamos a trabajar, con el fin de agregarle funcionalidad javascript  
modulo ***npm install ejs***  
ya con el modulo instalado debmos cambiar la extension .html por .ejs en nuestras ***views***  
~~~
// Settings
app.set('title', 'Aplicacion hecha en Node.Js')
app.set('port', 3000)
~~~
# ejs
configuraciones del motor de plantilla ejs  
ya no enviamos los archivos con ***sendFile*** si no que ahora debemos renderizar con ***render***, ya que estamos renderizando las plantilla ejs  
~~~
// Settings
app.set('view engine', 'ejs') // motor de plantilla
app.set('view', path.join(__dirname, 'views')) // directorio de las vistas
~~~
## entrega de las funciones del archivo controller con render
en este momento que ya se empieza a trabajar con ejs, y se ha configurado las views de nuestro proyecto, debemos borrar el path y el objeto que apunta a la ruta  
ademas de quitarle el .html ya que estos archivos son .ejs
~~~
const getUsers = (req, res) => {
  res.render('all_users')
}

const createUser = (req, res) => {
  res.render('create_user')
}

const updateUser = (req, res) => {
  res.render('update_user')
}

const deleteUser = (req, res) => {
  res.render('delete_user')
}

module.exports = { getUsers, createUser, updateUser, deleteUser } 
~~~

# mostrando datos desde un array a nuestras plantillas
~~~
const users = [
  {id:1, name:'kenneth', age:3},
  {id:2, name:'jared', age:3},
  {id:3, name:'linda', age:40},
  {id:4, name:'cristian', age:39},
]

const getUsers = (req, res) => {
  res.render('all_users', {users:users})
}

const createUser = (req, res) => {
  res.render('create_user', {users:users})
}

const updateUser = (req, res) => {
  res.render('update_user', {users:users})
}

const deleteUser = (req, res) => {
  res.render('delete_user', {users:users})
}

module.exports = {getUsers, createUser, updateUser, deleteUser } 
~~~
# mostrar data dentro de ejs
vamos a mostrar una tabla de datos en nuestra plantilla de users.ejs  
son datos de un array que iremos iterando con forEach para mostrar el contenido del array  
tabla en html, y código Javascript entre ***<% %>***, para datos debemos agregarle un igual ***=***.  

~~~
<table>
  <tr>
    <td>ID</td>
    <td>Nombre</td>
    <td>Edad</td>
  </tr>
  <% users.forEach((indice)=>{ %>
    <tr>
      <td><%= indice.id %></td>
      <td><%= indice.name %></td>
      <td><%= indice.age %></td>
    </tr>
  <% }) %>
</table>
~~~

# CRUD
vamos a manejar el crud de controllers.js  
debemos cambiar el nombres de las variables ya que estaremos renderizando solo las vistas, y crearemos las funciones con las que registraremos los datos la data  

### funciones de nuestras rutas CRUD
~~~
const users = [
  {id:1, name:'kenneth', age:3},
  {id:2, name:'jared', age:3},
  {id:3, name:'linda', age:40},
  {id:4, name:'cristian', age:39},
]

const getUsers = (req, res) => {
  res.render('users', {users: users})
}

const getCreateUser = (req, res) => {
  res.render('create_user', {users: users})
}

const getUpdateUser = (req, res) => {
  res.render('update_user', {users: users})
}

const getDeleteUser = (req, res) => {
  res.render('delete_user', {users: users})
}

const createUser = (req, res) => {}
const updateUser = (req, res) => {}
const deleteUser = (req, res) => {}

module.exports = { 
  getUsers, 
  getCreateUser, 
  getUpdateUser, 
  getDeleteUser,
  createUser,
  updateUser,
  deleteUser,
}
~~~
### uso de nuestras funciones y los metodos CRUD
~~~
const express = require('express')
const router = express.Router()
const usersController = require('../controller/users')

// rutas de las vistas
router.get('/', usersController.getUsers)

router.get('/all', usersController.getUsers)

router.get('/create', usersController.getCreateUser)

router.get('/update', usersController.getUpdateUser)

router.get('/delete', usersController.getDeleteUser)

// registros post, put, delete

router.post('/create', usersController.createUser)

router.put('/update', usersController.updateUser)

router.delete('/delete', usersController.deleteUser)

module.exports = router
~~~

### mostrar datos que han sido enviados desde un formulario
~~~
const createUser = (req, res) => {
  console.log(req.body)
}
const updateUser = (req, res) => {
  console.log(req.body)
}
const deleteUser = (req, res) => {
  console.log(req.body)
}
~~~

### hagamos pruebas con POSTMAN
para poder enviar las consultas desde POSTMAN  
debemos crear un Middleware que nos decodifique nuestros datos  
asi ya podremos visualizar los datos que recibimos del cliente  
~~~
app.use(express.urlencoded({extended:false}))
~~~

### ya podemos agregar datos a nuestro array desde POSTMAN 
~~~
const createUser = (req, res) => {

  users.push(req.body)
  res.render('users', {users: users})

  console.log("entrega un objeto: ", req.body)
}
~~~

### actualizar y eliminar
para la actualizacion debemos agregar a la ruta el parametro de ***id***, para poderlo identificar y actualizar  
asi mismo con la ruta del delete, para poderlo eliminar por su ***id***  

~~~
router.put('/update/:id', usersController.updateUser)
router.delete('/delete/:id', usersController.deleteUser)
~~~

### funciones actualizar y eliminar
hay que recibir el parametro id, que es el que nos permite identificar al elemento a eliminar  

### funcion actualizar
1. almacenamos el id que viene como parametro de la url en una constante
2. iteramos el array 
3. validamos con if si el id almacenado coincide con el del array
4. actualizamos los campos de nuestro array de elementos
5. asignamos los datos a cambiar del array con los parametros nuevos
6. cortamos con break el ciclo y salimos, actualizadondo los datos
~~~
const updateUser = (req, res) => {
  const param = req.params.id
  for (let i = 0; i < users.length; i++) {
    if (param == users[i].id) {
      users[i].name = req.body.name
      users[i].age = req.body.age
      break
    }
  }
  res.render('users', {users: users})
  console.log(req.body)
}
~~~

### Funcion eliminar
lo que hace la funcion eliminar
1. guardamos el id en una constante
2. luego iteramos el array de datos
3. validamos que el id en la iteracion coincida con el almacenado
4. usamos splice para que en la iteracion i, desplace 1 elemento
5. elimiando de nuestro array el elemento que coincide con el id a eliminar
~~~
const deleteUser = (req, res) => {
  const param = req.params.id
  for (let i = 0; i < users.length; i++) {
    if (param == users[i].id) {
      users.splice(i,1)
      break
    }
  }
  res.render('users', {users: users})
  console.log(req.body)
}
~~~
# SQL
Modulo de coneccion Node con MySQL 
> npm install mysql

### My Database
1. MySQL
2. creamos DataBase
3. creamos tabla

~~~
CREATE TABLE users(
  id int AUTO_INCREMENT PRIMARY KEY,
  name varchar(50),
  age int(3)
)
~~~
### SQL Connection desde NodeJs
Modulo de configuracion  
~~~
module.exports = {
  mySQLConnect: {
    host: 'localhost',
    user: 'crkj',
    password: 'crkjalive',
    database: 'sale'
  }
}
~~~
### connection con la base de datos
1. requerimos el modulo mysql
2. traemos el modulo de mySQLConnect de nuestro archivo configuracion.js
3. creamos la conexion que recibe como parametros nuestros datos de conexion
4. conectamos nuestros datos y validamos la conexion 
5. .connect recibe 2 parametros error y la conexcion exitosa
6. returnamos el parametro de conexion
7. importamos este archivo en nuestro archivo principal de la app.js
~~~
const mysql = require('mysql')
const { mySQLConnect } = require('./configuracion')

const connection = mysql.createConnection(mySQLConnect)

connection.connect((err, conn)=>{
  if(err){
    console.log('Ha ocurrido un error: '+err)
  }else{
    console.log('Conexión exitosa')
    return conn
  }
})

module.exports = connection
~~~

# Consulta SQL de los registros de la tabla users
debemos importar nuestro archivo de ***connection*** en nuestro users controller  
en nuestra funcion ***getUsers*** vamos a implementar la consulta ***sql***  
con la funcion ***query***, que recibe 2 parametros  
la consulta ***sql***, y un ***callback***, que recibe 2 parametros  
err y result, err si ocurre un error, y result que son los registros obtenidos  
nos devuelve un array con los registros obtenidos de la base de datos    
### Code...
~~~
const connection = require('../connection')

const getUsers = (req, res) => {
  const sql = "SELECT * FROM users"
  connection.query(sql, (err, results)=>{
    if (err) {
      console.log('error en la consulta: '+err)
    } else {
      console.log(results)
      res.render('users', {users: results})
    }
  })
}
~~~

# Insert
vamos a añadir la funcionalidad para registrar un usuario 

### Insertar registros a nuestra base de datos
creamos el formulario para insertar datos a nuestra tabla, en nuestra vista de create  
en el ***action***, ponemos la ruta, y el metodo ***POST***  
al accionar el ***submit*** este ejecutara la ruta y esta a su vez la funcionalidad para insertar el registro  
~~~
<form action="/users/create" method="POST">
  <label for="name">Nombre</label>
  <input type="text" id="name" name="name" placeholder="ingresa el nombre">
  <br>
  <label for="age">Edad</label>
  <input type="text" id="age" name="age" placeholder="ingresa la edad">
  <br>
  <input type="submit" value="insertar">
</form>
~~~
funcionalidad para registrar  
creamos la consulta sql almacenandola y esta asu vez en el ***SET ?***  
va a cargar el data, que es el req.body que nos entrega un objeto con los datos del formulario  
***connection.query*** ejecuta el registro, y un callback err y result  
validamos el err y mostramos si existe algun error  
sino mostramos un mensaje de registro exitoso y redireccionamos a la vista principal  

~~~
const createUser = (req, res) => {
  const sql = 'INSERT INTO users SET ?'
  const data = req.body

  connection.query(sql, data, (err, result) => {
    if (err) {
      console.log("error al insertar: "+err)
    }
    else {
      console.log('Usuario registrado:'+result)
      res.redirect('/users') // redireccionamos a esta route
    }
  })
  // console.log(req.body) // mostrar lo que esta recibiendo
  // res.render('users', {users:users})
}
~~~

# Update o Eliminar
para ejecutar estas funciones en el formulario de crear  
creamos los botones para actualizar y eliminar, que nos dirigiran a nuestras rutas  

~~~
<div class="td"><a id="btn-update" href="/users/update/<%= indice.id %>">Update</a></div>
<div class="td"><a id="btn-delete" href="/users/delete/<%= indice.id %>">Delete</a></div>
~~~

routes 
~~~
router.post('/update/:id', usersController.updateUser)
router.post('/delete/:id', usersController.deleteUser)
~~~

formulario de actualización
~~~
<form action="/users/update/<%= user[0]['id'] %>" method="POST">
  <label for="name">Nombre</label>
  <input type="text" id="name" name="name" value="<%= user[0]['name'] %>">
  <label for="age">Edad</label>
  <input type="text" id="age" name="age" value="<%= user[0]['age'] %>">
  <input type="submit" value="update">
</form>
~~~

funcionalidad, actualizacion
~~~
const updateUser = (req, res) => {
  const param = req.params.id
  const sql = `UPDATE users SET name='${req.body.name}', age='${req.body.age}' WHERE id='${param}'`
  connection.query(sql, (err, result) => {
    if (err) {
      console.log('error al actualizar: '+err)
    }
    else {
      console.log('update: '+result)
      res.redirect('/users/all')
    }
  })
}
~~~

### Eliminar 
formulario que pregunta si queremos eliminar  
un boton ejecutara la accion, y el otro regresara a la vista usuarios  
~~~
<form action="/users/delete/<%= user[0]['id'] %>" method="POST">
  <h2>Desea eliminar este registro</h2>
  <input id="btn2-delete" type="submit" value="Sí Eliminar">
  <div class="contenedor_btn"><a id="btn2-update" href="/users/all">Cancelar</a></div>
</form>
~~~
 
Funcionalidad para la consulta sql delete  
~~~
const deleteUser = (req, res) => {
  const param = req.params.id
  const sql = `DELETE FROM users WHERE id='${param}'`
  connection.query(sql, (err, result) => {
    if (err) {
      console.log('error al eliminar: '+err)
    }
    else {
      console.log('delete: '+result)
      res.redirect('/users/all')
    }
  })
}
~~~
## Conclusiones 
las peticiones ***GET*** son la que se envian por la URL y se reciben por req.params.id~  
las peticiones ***POST*** son las que enviamos por debajo en el servidor y se reciben por req.body.id~  
debemos tener claro que cada ruta sea GET o POST va a ejecutar una funcionalidad  

# Modulo NoSQL 
1. instalar MongoDB (MongoDB Community Server)
2. CMD + ***mongod*** para levantar el server 
3. Sí No agregar Path (C:\Program Files\MongoDB\Server\4.4\bin)
4. ***mongo*** (para ejecutar comandos de mongodb) 

## Comandos 
1. show dbs

## Conexion a MongoDB 

#### config.js
~~~
module.exports = {
  mysql_database : {
    host: 'localhost',
    user: 'root', 
    password: '',
    database: 'mydb'
  },
  mongodb : {
    host: 'localhost',
    user: '', 
    password: '',
    database: 'mydb',
    port: 27017
  }
}
~~~

### modulo para mongodb 
con este modulo hacemos la conexion entre mongodb y NodeJs  

- npm install mongoose  

#### connection.js 
~~~
const mongoose = require('mongoose')
const { mongodb } = require('./config')

const connection = mongoose.connect(`mongodb://${mongodb.host}:${mongodb.port}/${mongodb.database}`)
.then( (db) => {
  console.log('Conexion Exitosa)
})
.catch( (err) => {
  console.log('Ha ocurrido un error: ' + err)
})

module.exports = connection
~~~

# CRUD con NodeJS y MongoDB
1. src/models
2. users.js

Mongodb usa colecciones en vez de tablas como SQL  
para esto debemos tener un esquema 

## esquema
users.js  
~~~
const mongoose = require('mongoose')
const Schema = mongoose.Schema

const UserSchema = new Schema({
  name: String,
  edad: Number
})

const User = mongoose.model('User', UserSchema)

module.exports = User
~~~

### controllers/users.js 
~~~
const User = require('../models/users')

// buscar
const getUsers = (req, res) => {
  User.find({}, (err, result) => {
    if (err) { console.log('ha ocurrido un error') }
    else {
      console.log(result)
      res.send(result)
    }
  })
}

// guardar
const createUser = (req, res) => {
  const data = req.body
  
  const user = new User({
    name: data.name,
    age: data.age
  })

  user.save( (err, result) => {
    if (err) {
      console.log('ha ocurrido un error al guardar: ' + err)
    } 
    else {
      console.log('Usuario registrado')
      res.redirect('/users/all')
    }
  })
}

// actualizar get
getUpdateUser = (req, res) => {
  const param = req.params.id

  User.find({_id : param}, (err, result) => {
    if (err) {
      console.log('Error al consultar por el id error: ' + err)
    }
    else {
      console.log(result)
      res.render('update-user', {user: result})
    }
  })
}

// actualizar post
const updateUser = (req, res) => {
  const param = req.params.id
  const data = req.body

  User.findOneAndUpdate({_id:param}, data, (err, result) => {
    if (err) {'error al actualizar, error: ' + err }
    else {
      console.log('usuario actualizado)
      res.redirect('/users/all')
    }
  })
}

// eliminar get
const getDeleteUser = (req, res) => {
  const param = req.params.id
  User.find({_id:param}, (err, result) => {
    if (err) { console.log('error al eliminar, error: ' + err )}
    else {
      console.log(result)
      res.render('delete-user', {user: result})
    }
  })
}

// eliminar post
const deleteUser = (req, res) => {
  const param = req.params.id
  User.deleteOne({_id:param}, (err, result) => {
    if (err) { console.log('error al eliminar, error: ' + err )}
    else {
      console.log(result)
      res.redirect('/user/all')
    }
  })
}
~~~

hasta aquí terminamos con la operaciones básicas del CRUD con NodeJs MongoDB  
   
# JWT Modulo de Autenticación (JSON Web Tokens)
Un token es un conjunto de caracteres codificado, que se compone de 3 partes  
1. header (alg: 'HS256', typ: 'JWT ) algoritmo y tipo
2. payload o data (sub, name, iat) dueño del token, ID nombre y iat (tiempo en el que se creo el token en ms)  
3. union de header y del payload, en base 64 para mayor seguridad 

la idea de utilizar el token es validar el acceso o los permisos en la app  

### Modulos para nuestra aplicacion 
- npm init -y 
- npm i express mongoose bcrypt jsonwebtoken
- npm i nodemon -D 
- src/index.js 

## configuracion del servidor

***index.js*** 

~~~
const express = require('express')
const app = express()

require('./connection')

app.set('port', 3000)

app.use(express.urlencoded({extended: false}))

app.listen(app.get('port'), () => {
  console.log('Application run server on port: '+ app.get('port'))
})
~~~

### coneccion a la base de datos 

***connection.js***

~~~
const mongoose = require('mongoose')

const connection = mongoose.connect('mongodb://localhost:27017/jwtdb')
.then( (db) => {
  console.log('Conexion exitosa')
})
.catch( (err) => {
  console.log('Ha ocurrido un error: ' + err)
})

module.exports = connection
~~~

### Creación de modelio de usuarios

- src/models
- users.js

### Modelo de User en Schema 

~~~
const mongoose = require('mongoose')
const Schema = mongoose.Schema
const userSchema = new Schema({
  name: String,
  email: String,
  password: String
})
const User = mongoose.model('User', userSchema)
module.exports = User

/* con esto ya se puede usar el modelo de archivo */
~~~

### Creación de rutas que vamos a utilizar

- src/routes/users.js
 
~~~
const express = require('express')
const router = express.Router()

router.get('/admin')
router.post('/login')
router.post('/register')

module.exports = router
~~~

- agregar las rutas a nuestro index

~~~
const userRoutes = require('./routes/users')

app.use(userRoutes)
~~~

- funcionalidades de nuestras rutas 

~~~
const jwt = require('jsonwebtoken')
const bcrypt = require('bcrypt')
const user = require('../models/users')

const getAdmin = (req, res) => {
  res.send('muestra mensaje admin')
}

const login = (req, res) => {
  res.send('muestra mensaje login')
}

const register = (req, res) => {
  res.send('muestra mensaje register')
}

module.exports = {
  getAdmin,
  login,
  register,
}
~~~

- accediendo a las funcionalidades de las rutas  

~~~
const express = require('express')
const router = express.Router()
const usersController = require('../controllers/users')

router.get('/admin', usersController.getAdmin)
router.post('/login', usersController.login)
router.post('/register', usersController.register)

module.exports = router
~~~

## Registro de usuario
en la funcionalidad de la ruta register, creamos una constante, la cual instancia el objeto del schema  
y asignamos los valores que se reciben en la body del método post  
en la password debemos encriptar la contraseña con la funcion ***hastSync***, que recibe 2 parametros  
el dato que recibimos en el body del método post y la cantidad de saltos que va a encriptar  

~~~
const register = (req, res) => {
  const user = new User({
    name: req.body.name,
    email: req.body.email,
    password: bcrypt.hashSync(req.body.password, 10)
  })
  user.save((err, result) => {
    if (err) {
      res.send('ha ocurrido un error al salvar la información')
    }
    else {
      res.send('Registro exitoso')
    }
  })
}
~~~

## Iniciar sesión



# Sockets 

# Aplicacion Web en tiempo real


