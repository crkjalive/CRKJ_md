# Applicacion Web con Node y SQL CRUD 

1. npm init --yes ***inicializar proyecto***
2. npm install express ***servidor***
3. npm install mysql ***SQL***
4. npm install express-myconnection ***rutas***
5. npm install morgan ***para saber las peticiones***
6. npm install ejs ***motor de plantillas***
7. npm install nodemon -D ***detecta cambios, reiniciando el servidor***

npm install express mysql express-myconnection morgan ejs

### Server de express
~~~
const express = require('express');
const app = express();

app.listen(3000, () => {
  console.log('server on port 3000')
});
~~~

### configuracion script para correr nodemon
esta configuracion es la que permite que se mantenga el servidor atento a los cambios que vamos haciendo  

package.json
~~~
  "scripts": {
    "dev": "nodemon src/app.js"
  },
~~~
#### Ejecuta:   
~~~
npm run dev
~~~

# Configuracion del motor de plantillas
esta carpeta será la encargada de manejar el motor de plantillas, y almacenar las vistas  
~~~
app.set('view engine', 'ejs'); // motor de plantillas
~~~
# modulo path para configurar las vistas (views)
encargado de unir rutas  
~~~
const path = require('path');
~~~

configuracion del path para que sepa donde se almacenan las vistas 
~~~
app.set('views', path.join(__dirname, 'views))
~~~

### configuracion de la conexion con la base de datos en MySQL
~~~
app.use(myConnection(mysql, { 
  host: "localhost",
  user: "crkj",
  password: "crkjalive",
  database: "sale",
  port: 3306,
}, 'single'));
~~~

### /routes /customer.js
aqui vamos a guardar las rutas de nuestra aplicacion
~~~
const express = require('express');
const router = express.Router() // objeto que va a ir almacenando mis rutas

// urls de nuestra aplicación

module.exports = router;
~~~

### /controllers /customerController.js
aqui vamos a guardar las funciones que controlan las rutas
~~~

~~~

# Archivo Inicial de la configuracion de la APP
archivo que contiene toda la configuracion inicial del servidor de nuestra aplicación  
- importamos los modulos, e instanciamos express
- importamos el modulo de las rutas
- parametros para la conexion con la base de datos
- express.static, tendremos los archivos css, e imagenes
- levantamiento del servidor con express

~~~
// Archivo de configuración inicial de nuestro app 😎👍
const express = require('express'); // server
const path = require('path'); // routers
const morgan = require('morgan'); // funciones middlewares
const mysql = require('mysql') // SQL module
const myConnection = require('express-myconnection') // conection con SQL

// instancia de express
const app = express();

// Settings, configuraciones para la aplicación
app.set('port', process.env.PORT || 3000); // configuracion del puerto 3000
app.set('view engine', 'ejs'); // motor de plantillas
app.set('views', path.join(__dirname, 'views')); // configura directorio views

// aqui vamos a almacenar las rutas cada vez que un usuario ingrese a la ruta principal /
const customerRoutes = require('../routes/customer');

// Middlewares, son funciones que se ejecutan antes de que existan las peticiones de los usuarios - muestra mensajes en consola sobre las peticiones de los usuarios
app.use(morgan('dev')); // mostrara mensajes de respuesta en consola

// datos para conexion con MySQL
// configuracion de conexión, funciona 🙌🙌🙌
app.use(myConnection(mysql, { 
  host: "localhost",
  user: "crkj",
  password: "crkjalive",
  database: "sale",
  port: 3306,
}, 'single'));

// Routers (rutas o peticiones del servidor), almacenadas en esta variable
app.use('/', customerRoutes);

// archivos estaticos (css, imagenes)
app.use(express.static(path.join(__dirname, 'public')))

// server on
app.listen(app.get('port'), () => {
  console.log('server on port 3000')
});
~~~
___

# CRUD de la applicación
Modulo para manejar el CRUD, atraves de metodos, almacenados en un objeto  

~~~
// Objeto que va almacenando los metodos que vamos a ir utilizando
const controller = {};

// metodos list, save, delete
controller.list = (req, res) => {
  // res.send('hello world, desde el metodo list'); // mensaje de prueba
}

module.exports = controller;
~~~

### metodo de conexion y consulta de la tabla
funcion que nos trae express para conectar los metodos de las consultas  
~~~
// Objeto que va almacenando los metodos que vamos a ir utilizando
const controller = {};

// metodos list, save, delete, update
controller.list = (req, res) => {
  req.getConnection((err, conn) => { // recibe la conexion de expressConnection para hacer la consulta
    conn.query("SELECT * FROM contactos", (err, customers_data) => {
      // valida si hay un error, que se puede manejar con next(err), o de dumi con res.json(err)
      if (err) {
        // next(err)
        res.json(err);
      }
      // miramos por consola los datos que nos trae la consulta
      console.log(customers_data); 
      // renderizar una vista customers.ejs
      res.render("customers_view", {
        data: customers_data,
      });
    });
  });
  // res.send('hello world, desde el metodo list'); // mensaje de prueba
};

module.exports = controller;
~~~

### Vistas en ejs
aqui escribimos html normal y agregamos javascript entre mayores y menores que ***<%%>*** y los porcentages + un = interpretara código, sin el = ejecutamos ciclos y funciones del lenguaje

### CRUD funciones
- customerController controla las  funciones del crud (list, delete, update, add)
- customer en este archivo declaramos las rutas que es usuario ira a ejecutar

# Modulo completo del CRUD
contiene los comentarios  
~~~
// Objeto que va almacenando los metodos que vamos a ir utilizando
const controller = {}

// metodos list, save, delete, update
controller.list = (req, res) => {
  req.getConnection((err, conn) => {
    // recibe la conexion de expressConnection para hacer la consulta
    conn.query("SELECT * FROM crud_fazt", (err, customers_data) => {
      // valida si hay un error, que se puede manejar con next(err), o de dumi con res.json(err)
      if (err) {
        // next(err)
        res.json(err)
      }
      // miramos por consola los datos que nos trae la consulta
      // console.log(customers_data)
      // renderizar una vista customers.ejs
      res.render("customersView", {
        data: customers_data,
      })
    })
  })
  // res.send('hello world, desde el metodo list') // mensaje de prueba
}

// funcion insertar datos en la tabla del formulario
controller.save = (req, res) => {
  const data = req.body
  req.getConnection((err, conn) => {
    conn.query("INSERT INTO crud_fazt set ?", [data], (err, rows) => {
      res.redirect("/") // redirecciona luego de insertar
      // console.log(rows) // muestra todos los objetos de la tabla
      // console.log(req.body) // muestra el objeto de datos
      // res.send(`<a href="/">works</a>`) // me manda a /add e imprime link a directorio
    })
  })
}

// funcion para editar el dato de la tabla
controller.edit = (req, res) => {
  const { id_customer } = req.params
  req.getConnection((err, conn) => {
    conn.query(`SELECT * FROM crud_fazt WHERE id_customer = ${id_customer}`, (err, customer) => {
      res.render('customer_edit', {
        data: customer[0]
      })
    })
  })
}

controller.update = (req, res) => {
  const {id_customer} = req.params
  const newCustomer = req.body 
  req.getConnection((err, conn) => {
    conn.query('UPDATE crud_fazt SET ? WHERE id_customer = ?', [newCustomer, id_customer], (err, rows) => {
    res.redirect('/')
    })
  })
}

// funcion eliminar dato de la tabla
controller.delete = (req, res) => {
  const { id_customer } = req.params
  req.getConnection((err, conn) => {
    if (err) {res.json(err)}
    conn.query(`DELETE FROM crud_fazt WHERE id_customer = ${id_customer}`, (err, rows) => {
      if (err) {res.json(err)}
      res.redirect("/")
    })
  })
}

module.exports = controller
~~~

### rutas del Customer
~~~
// archivo de configuracion de las url que vamos a manejar
const express = require('express');
const router = express.Router() // objeto que va a ir almacenando mis rutas

const customerController = require('../controllers/customerController'); // modulo que contiene un objeto que almacena los metodos del crud

// llama al metodo list del objeto
router.get('/', customerController.list)
router.post('/add', customerController.save)
router.get('/delete/:id_customer', customerController.delete)

router.get('/update/:id_customer', customerController.edit )
router.post('/update/:id_customer', customerController.update)

module.exports = router;
~~~ 