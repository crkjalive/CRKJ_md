~~~
Davivienda 610 2111 5900008300772111
Davivienda 410 4547 5900006301134547
~~~

# SQL EDteam 2022
Que es una base de datos, un grupo de datos de información organizada, que se almacena en tablas  

# Motores de bases de datos 

## Relacionales  
SQLServer, MariaDB, MySQL, Oracle, Postgres

## NoRelacionales 
MongoDB ***Documentales (JSON)***  
Redis ***Clave - Valor***  
Grafos ***Neo4L, Dgraph*** 

## SGBD
Herramienta que permite administrar todos los  objetos de una base de datos, usuarios, tablas, permisos etc. 

## Postgres 
1. www.postgres.org ->descargar en instalador 
2. password + usurioAdministrador
3. port 5432 por defecto
4. pgadmin

## Archivos de configuración
vim postgressql.conf  
listend_adresses = '*' ***permite que cualquier IP se conecte a este equipo, si no se sabe la ip de la otra maquina a conectar***  
(192.168.20.30, 192.168.20.31)  ***le damos permiso a maquinas especificas***  

## Rutas para editar las configuraciones de postgres
etc/init.d/postgres status ***stado*** online  
etc/init.d/postgres restart ***reinicia***  
psql postgres postgres  

## auth fallo 
para autenticaion del cliente  
pg_hba.conf  ***archivo de configuración para el cliente***  
trust es que confie, no requiere password, se debe reiniciar el servidor  
pg_pgba  


# Docker
Instalación, Aprender Docker 

# Clientes postgres 
1. psql 

# Lenguaje SQL (DDL y DCL)
3 grandes grupos para el manejo de las bases de datos

***DDL (data difination lenguage)*** 
1. como va almacenar, crear y guardar los datos  

***DCL (data control lenguage)***
1. administrar los usuarios de las bases de datos
2. privilegios rwdx

***DML (data manipulation lenguage)***
1. manipulación de crud (Create, Read, Update, Delete)

## Crear usuarios en nuestra bases de datos
Debemos iniciar creando un usuario para que se pueda logear y pueda crear bases de datos  
no se debe usar el usuario por defecto ***postgres***, ya que va a ser el que mas ataquen  

\h CREATE USER / ROLE 
con este comando vemos la documentación para ver como se hace algo  

~~~
CREATE USER chanchito PASSWORD '12345';
~~~

## Crear bases de datos 
crear una base de datos, y asignarle el propietario  

\h CREATE DATABASE  
Para ver como crear una base de datos  
~~~
CREATE DATABASE mydb OWNER chanchito;
~~~

## Listar las bases de datos
> \l 

|name|owner|encoding|collate|ctype|access privileges|
|-|-|-|-|-|-|
|mydb|chanchito|UTF8|en_US.utf8|en_US.utf8||

## Conectar a la base de datos desde la Shell 
> \c mydb chanchito  

~~~
you are now connected to database "mydb" as user "chanchito"
~~~

## Conectar desde la linea de comandos 

~~~
psql mydb chanchito
~~~

## Condicionar a que se pida clave al conectar 

debemos entrar al archivo de configuración de porstgres  
y cambiar de trust a MD5  
> vim /var/lib/posgresql/data/pg_hba.conf  

~~~
IPv4 local connections  
local (trust por MD5)
host  (trust por MD5)

IPv6 local connections  
host  (trust por MD5)
~~~

Así ya nos debe pedir contraseña para conectarnos a la base de datos  

> docker exec -it postgresed psql mydb chanchito 

### 1. Conectar a user postgres
Se debe hacer como usuario postgres nos conectamos con ***\c DB name***  

> \c postgres postgres
> PASSWORD for user postgres:

you are now connected to database 'postgres' as user 'postgres'  

### 2. Cambio de password a un usuario 
~~~
ALTER ROLE chanchito PASSWORD '654321';
~~~

### 3. Crear un nuevo usuario 
~~~
CREATE ROLE google PASSWORD '12345';
~~~

### 4. Asignar usuario a la base de datos
~~~
ALTER DATABASE mydb OWNER TO google
~~~
> \l 

# Tipos de datos 
1. númericos
2. caracter
3. tiempo y funciones de tiempo UnixTime
  1. timestamp ***guarda fecha y hora***
  2. timestamp time zone ***fecha y hora de la zona horaria de la region actual***
  3. date ***solo almacena la fecha***  
  4. time ***solo guardan la hora***
  5. time zone ***hora de la region actual***
  6. inteval ***premiten procesar un campo especifico de la fecha, año, mes, día***
  7. unixtime ***fecha actual númerico desde el 1 jan 1970 1677017898***
4. boolean
  1. en postgres recibe o almacena un 1 o 0 1byte 
  2. recibe true, on, yes, 1 o false, off, no, 0 pero almacena 1byte
5. UUId ***nueva forma de identificar los registros, antihacking***
6. json
7. secuencias

# Crear Tablas
se sugiere crear tablas en plural, ya que podria entrar en conflicto con las palabras reservadas del sistema.  
propiedades de las tablas se deben manejar en minuscula para facilidad a la hora de consultar.

|datos para nuestra tabla|
|-|
| id, name, last_name, age, date_born, available|

## Tabla de personas
~~~
CREATE TABLE persons (
  id UUID, 
  first_name VARCHAR(60),
  last_name VARCHAR(60),
  age SMALLINT,
  birthday DATE,
  available BOOL
);
~~~

### Tabla de trabajos
|||||||
|-|-|-|-|-|-|
|id|id_persons|fecha_inicial|fecha_final|trabajo_actual|

~~~
CREATE TABLE jobs (
  id UUID,
  id_persons UUID,
  begins_at DATE,
  ends_at DATE,
  currently bool
);
~~~

## Modificar estructura de la tabla ALTER
para ***BORRAR*** columnas de una tabla creada

~~~
ALTER TABLE persons DROP COLUMN age;
~~~

para ***AGREGAR*** columnas de una tabla creada
~~~
ALTER TABLE jobs ADD COLUMN job_name VARCHAR(50); 
~~~

## Borrar tablas 
~~~
DROP TABLE other_table;
~~~

# Otorgar privilegios a tablas de lectura 
a usuarios que no son el dueño de la tabla  
de lectura escritura  
la conexión y permisos los otorga el dueño de la tabla en postgres  

~~~
GRAND SELECT ON persons TO alexys;
~~~

así ya se le dan permisos al usuario para hacer consultas con ***SELECT*** de esa tabla a la que le acabamos de dar permisos  

# Revocar privilegios a tablas de lectura
Quitar permisos a las tablas de algun usuario, ya no podra hacer consultas en la tabla  
~~~
REVOKE SELECT ON persons FROM alexis;
~~~

# SQL (DML) 

## Insert
nos permite registrar datos en nuestras tablas  
el orden de campos que vamos a afectar, y en ese orden se ingresaran los valores  

***Universal Unique Identifier (UUID)***  
funcion para generar uuid  

estructura de nuestra tabla
||||||
|-|-|-|-|-|
|id|first_name|last_name|date_born|avaliable|

### Afectando los campos de la tabla  
***Se debe respetar el orden de los campos y de los valores a isertar DEBEN COINCIDIR asi esten en desorden***  

> INSERT INTO name_table (campo1, ..., campoN ) VALUES (valor1, ..., campoN);

~~~
INSERT INTO persons (id, first_name, last_name, date_born, available)
VALUES (gen_random_uuid(), 'Wizard', 'Deejay', '1984-01-08', true);
~~~

### Afectando la tabla sin especificar que campos  
***ya que se va a afectar todos los campos de la tabla en su orden***  

> INSERT INTO name_table VALUES (valor1, ..., campoN);

~~~
INSERT INTO persons
VALUES (gen_random_uuid(), 'Wizard', 'Deejay', '1984-01-08', true);
~~~

### Afectando la tabla con valores por DEFAULT  
***Valores por DEFAULT en nuestras tablas***  

~~~
CREATE TABLE students (
  id UUID DEFAULT gen_random_uuid(),
  first_name VARCHAR(50),
  is_active BOOL DEFAULT true,
  created_at TIMESTAMP DEFAULT now()
);
~~~

> INSERT INTO name_table VALUES (DEFAULT, ..., campoN);

~~~
INSERT INTO students
VALUES (DEFAULT, 'Nataly', DEFAULT, DEFAULT);
~~~
***cuando se insertan datos por default, se insertan null***  
***ya que al crear la tabla no se le dieron valores por default a los campos***  

***solo insertar datos que sabemos que no son por default***  
~~~
INSERT INTO students (first_name) 
VALUES ('Nataly');
~~~

***insertar varios registros a la vez, y demas valores por DEFAUlT***  
~~~
INSERT INTO students (first_name) 
VALUES ('Nataly'), ('Andreina'), ('Linda'), ('Juliana'), ('Jennifer');
~~~

## INSERT desde una consulta SELECT
podemos consultar e insertar datos desde la consulta de otra tabla  

~~~
INSERT INTO students (first_name, is_active)
SELECT f_name, active
FROM tmp_students
~~~

## hacer inserts not null 
debemos crear la tabla con la propiedad ***NOT NULL*** para que no se nos inserten datos a nuestras columnas vacios o null  
~~~
CREATE TABLE students (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY, NOT NULL,
  first_name VARCHAR(50) NOT NULL,
  is_active BOOL DEFAULT true NOT NULL,
  created_at TIMESTAMP DEFAULT now() NOT NULL,
  update_at TIMESTAMP
);
~~~

# SQL (DML) 

## Update
con update actualizamos la informacion de los registros ya insertados en las tablas  

> UPDATE table 
> SET campo1 = valor1, campo2 = valor2, ..., campoN = valorN 
> WHERE , INSERT INTO name_table VALUES (valor1, ..., campoN);

~~~
UPDATE persons
SET first_name = 'Brenda', last_name = 'Jumla'
WHERE id = '45678-4567ae-23442faa-948958'
~~~

En postgres la actualizacion de los registros no es real, ya que postgres elimina el registro e inserta   
un nuevo registro respetando el id, ya que son inmutables, dejando el nuevo registro al final de la tabla,  
sin afectar su id  

Nunca olvidar identificar el registro a ***actualizar o eliminar*** con el ***WHERE*** o se alteraran todos los registros  

vamos a ver una afectación segura de todos los registros a un único valor  
~~~
UPDATE persons
SET available = false;
~~~

# SQL (DML) 

## DELETE 
eliminar registros de nuestra tabla  

> DELETE FROM my_table WHERE campoM = valorM;

~~~
DELETE FROM persons
WHERE id = '45678-4567ae-23442faa-948958'
~~~

***Eliminar datos nulos***  
esta busqueda se debe hacer con ***IS NULL*** ya que null no es un dato comparable  

~~~
DELETE FROM persons 
WHERE id IS NULL;
~~~

## TRUNCATE
truncate elimina todos los datos de la tabla sin marcha atras  

> TRUNCATE TABLE my_table

~~~
TRUNCATE TABLE persons;
~~~

# Llaves primarias, llaves unicas, llaves foraneas
como funcionan estas llaves en la creación de las tablas  

## PRIMARY KEY
vamos a darle nombre a nuestra llave primaria  

> CONSTRAINT persons_id_pk PRIMARY KEY (id)

de esta forma asignamos nombre a nuestra llave primaria sin ***PRIMARY KEY***, directamente en el campo  
esto ayuda a limitar la identificación contra el hackeo de nuestro campo.  
***osea instanciamos la lave primaria nando un nombre que identifique el campo de la tabla***  

~~~
CREATE TABLE students (
  id UUID DEFAULT gen_random_uuid() NOT NULL,
  first_name VARCHAR(50) NOT NULL,
  is_active BOOL DEFAULT true NOT NULL,
  created_at TIMESTAMP DEFAULT now() NOT NULL,
  update_at TIMESTAMP,
  delete_at TIMESTAMP,
  CONSTRAINT persons_id_pk PRIMARY KEY (id) 
);
~~~

## UNIQUE KEY
este hace referencia a que el campo es unico dentro de la tabla, osea que no se puede repetir, ni existir dos iguales  

> CONSTRAINT persons_first_name_last_name_uk UNIQUE (first_name, last_name) 

***nombre a campos afectados, impidiendo que haya dos nombres y apellidos iguales***  

~~~
CREATE TABLE students (
  id UUID DEFAULT gen_random_uuid() NOT NULL,
  first_name VARCHAR(50) NOT NULL,
  is_active BOOL DEFAULT true NOT NULL,
  created_at TIMESTAMP DEFAULT now() NOT NULL,
  update_at TIMESTAMP,
  delete_at TIMESTAMP,
  CONSTRAINT persons_id_pk PRIMARY KEY (id),
  CONSTRAINT persons_first_name_last_name_uk UNIQUE (first_name, last_name)
);
~~~

## FOREIGN kEY 
llaves foraneas nos permiten relacionar dos tablas, por medio de un campo o varios campos  

> CONSTRAINT jobs_persons_id_fk FOREIGN KEY (persons_id) REFERENCES persons (id)

~~~
CREATE TABLE jobs (
  id UUID DEFAULT gen_random_uuid() NOT NULL, 
  persond_id UUID NOT NULL,
  job_name VARCHAR(50) NOT NULL,
  create_at TIMESTAMP DEFAULT now() NOT NULL,
  update_at TIMESTAMP,
  CONSTRAINT jobs_id_pk PRIMARY KEY (id),

  CONSTRAINT jobs_persons_id_fk FOREIGN KEY (persons_id) 
    REFERENCES persons (id) 
    ON UPDATE RESTRICT 
    ON DELETE RESTRICT
);
~~~

si se requiere que en la tabla padre se hacen cambios, y queremos que tambien se cambien en la tabla hijo  
esto si se quiere tambien eliminar en cascada.

> CONSTRAINT jobs_persons_id_fk FOREIGN KEY (persons_id) REFERENCES persons (id)
> ON UPDATE CASCADE 
> ON DELETE CASCADE 

normalmente el campo id no se actualiza, por lo cúal debemos restringir el campo  
además de eliminar
> CONSTRAINT jobs_persons_id_fk FOREIGN KEY (persons_id) REFERENCES persons (id)
> ON UPDATE RESTRICT
> ON DELETE RESTRICT

támbien se puede configurar ***RESTRICT Y CASCADE***  

### insert en jobs
vamos a hacer pruebas de inserts en jobs, para validar que los datos sean correctos y validos  

~~~
// datos que SI existen
INSERT INTO jobs
VALUES (DEFAULT, '6bd5cf9c-44e3-4c2c-8b78-f025e7aca9fcfe', 'DEVELOPER', DEFAULT, DEFAULT)

// datos que NO existen
INSERT INTO jobs
VALUES (DEFAULT, 'abc5cf9c-44e3-4c2c-8b78-f025e7aca9fcfe', 'DEVELOPER', DEFAULT, DEFAULT)
~~~

### delete en persons
como en nuestra tabla creamos restricciones de update y delete, no podremos borrar registros  
ya que ya existen registros en la tabla jobs  

~~~
DELETE FROM persons
WHERE id = '6bd5cf9c-44e3-4c2c-8b78-f025e7aca9fcfe';
~~~

en reumen tendremos limitado si el registro tiene datos en otras tablas impidiendo borrarlos  

# SQL (DML)

## SELECT conversiones
las conversiones permiten hacer operaciones sobre los datos, ejemplo sumarle días a una fecha  
hay convertimos la fecha String a Date, para que la db pueda operar sobre la fecha  

1. puede recibir constantes
~~~
SELECT 'HOLA MUDO';
SELECT 8;
~~~

2. expresiones
~~~
2*2+2/2; // 5 Jerarquia de los signos
~~~

3. catsting 
~~~
SELECT 8/23; // 0 ya que devuelve integer 
SELECT 8::numeric/23::numeric; // 0.34782608695652173913 ya que devuelve float
~~~

### cast no válido
~~~
SELECT 'HOLA'::int; // error ya que es un String y no se deja convertir a Integer
~~~

### cast válido
~~~
SELECT '2018-09-13'::date; // año mes día de String a Date
~~~
***si se requiere convertir de String a Date se hace para válidar si es una fecha, pero si es postgres el que la crea no se requiere hacerle el cast***

1. funciones
~~~
SELECT now() // fecha actual

SELECT upper('Hola Mundo') // convierte a mayusculas

SELECT lower('Hola Mundo') // convierte a minusculas
~~~

5. campos de tablas
~~~
SELECT * FROM tabla; // trae cada uno de los campos de la tabla 

SELECT id, first_name, Last_name, is_active FROM tabla;
~~~

### Haciendo una consulta completa con los ejemplos anteriores
~~~
SELECT id, upper(first_name), is_active, (2+4)::numeric/3::numeric, 'Estudiante' FROM students;
~~~

### ALIAS
~~~
SELECT id, upper(first_name) AS Nombre, is_active, (2+4)::numeric/3::numeric AS Operacion, 'Estudiante' AS Profesion FROM students;
~~~
> Le llamamos proyección a todos los campos que queremos que devuelva una consulta SQL

# WHERE
El ***where*** es un filtro para los registros, limitando el resultado en la consulta SQL  

~~~
SELECT * FROM persons WHERE first_name = 'Wizard';
~~~

***Buscar los resultados en mayusculas, y compararlos con nuestra busqueda mayusculas***  
~~~
SELECT * FROM persons WHERE upper(first_name) = 'WIZARD';
~~~

# Operadores de comparación
| signo | significado |
|-|-|
| = | comparación |
| > |
| < |
| <= |
| >= |
| <> | Fiferente en db equivalente a != |

# opradores condicionales
| signo | significado |
|-|-|
| AND | 1 y 1 |
| OR | 1 o 2 |

# LIKE (sea como)
like nos permite filtrar carácteres, cuando no se conoce todo el valor del carácter  
nos va a traer todos los datos que coincidan sin importar que caracter este donde estaba la i o y  
con el guio bajo es el comodín, donde va a remplazar por lo que tenga el registro  

~~~
SELECT * FROM persons WHERE first_name LIKE 'Alex_s'
~~~

buscar lo que coincida con el porcentaje, dandole el principio o final de la palabra a buscar  
o en el medio de una cadena de texto  
~~~
SELECT * FROM persons WHERE upper(first_name) LIKE 'Ale%' // busca con lo que coincida al final
SELECT * FROM persons WHERE upper(first_name) LIKE '%Ale' // busca con lo que coincida al principio
~~~

# ILIKE (no sea como)
ilike no es case sensitive, busca lo que se parezca y ya.  
no tiene encuenta las mayusculas o minusculas para hacer la busqueda  
~~~
SELECT * FROM persons WHERE first_name ILIKE 'aLE%';
~~~

# BETWEEN
entre un rago de fechas, numeros  
~~~
SELECT * FROM persons WHERE birthday BETWEEN '1990-1-1' AND '2000-1-31';
~~~

# IN
me permite hacer una consulta de una lista de valores dentro de otra consulta  
~~~
SELECT * FROM jobs WHERE persons_id IN ('uuid1', 'uuid2', 'uuid3',);
~~~
los registros que coincidan con esta lista son las que ira a mostrar  

#### Buscar quienes tiene trabajo en la lista de jobs
~~~
SELECT * FROM persons
WHERE id IN (SELECT persons_id FROM jobs);
~~~

# IS NULL
buscar si hay registros null en los campos de las tablas
~~~
SELECT * FROM persons WHERE update_at = null; // No Valido

SELECT * FROM persons WHERE update_at IS NULL; // Válido (trae los null registrados)
~~~

# NOT
niega si el archivo es verdadero 
~~~
SELECT * FROM persons WHERE update_at IS NOT NULL; // trae los registros que no sean nulos en este campo  
~~~

#### Buscar quienes NO tiene trabajo en la lista de jobs
~~~
SELECT * FROM persons
WHERE id NOT IN (SELECT persons_id FROM jobs);
~~~

# SQL Ordenamiento
como ordenar las consultas  

# ORDER BY (asc o desc)
ordenamos alfabeticamente las consultas y con asc o desc, de manera ascendentes o descendente  
~~~
SELECT * FROM persons ORDER BY first_name DESC, create_at ASC;
~~~

# Agrupaciones
Vamos a simular una facturación  

### Productos
~~~
CREATE TABLE products (
  id UUID DEFAULT gen_random_uuid() NOT NULL,
  product_name VARCHAR(30) NOT NULL,
  price NUMERIC (10,2) NOT NULL,
  CONSTRAINT products_id_pk PRIMARY KEY (id),
  CONSTRAINT products_products_name_uk UNIQUE (product_name) 
);
~~~

### Invoices
Encabezado de facturación 
~~~
CREATE TABLE invoices (
  id UUID DEFAULT gen_random_uuid() NOT NULL,
  invoice_date DATE DEFAULT NOW() NOT NULL,
  person_id UUID NOT NULL,
  CONSTRAINT invoices_id_pk PRIMARY KEY (id),
  CONSTRAINT invoices_persons_id_fk FOREIGN KEY (person_id) 
    REFERENCE persons (id) 
    ON UPDATE RESTRICT 
    ON DELETE RESTRICT 
);
~~~

### Details
detalle de la factura  
~~~
CREATE TABLE invoice_items (
  id UUID DEFAULT gen_random_uuid() NOT NULL,
  invoice_id UUID NOT NULL,
  product_id UUID NOT NULL,
  price NUMERIC(10,2) NOT NULL,
  quantity INT DEFAULT 1 NOT NULL,
  amount NUMERIC(10,2) NOT NULL,
  CONSTRAINT invoices_items_id_pk PRIMARY KEY (id),
  CONSTRAINT invoices_items_invoice_id_fk FOREIGN KEY (invoice_id) 
    REFERENCE invoices (id) 
    ON UPDATE RESTRICT 
    ON DELETE RESTRICT,
  CONSTRAINT invoices_items_product_id_fk FOREIGN KEY (product_id) 
    REFERENCE products (id) 
    ON UPDATE RESTRICT 
    ON DELETE RESTRICT
);
~~~

### Insert products
~~~
INSERT INTO products 
VALUES (default, 'arroz', 12.31),
      (default, 'papa', 1.44),
      (default, 'carne', 20);
~~~

### Insert para facturas 

~~~
INSERT INTO invoices (person_id) VALUES ('88') RETURNING id;

INSERT INTO invoices
VALUES (default,'idCliente88', 'idProduct86', '1000', 14.11, 2), 
       (default,'idCliente88', 'idProduct31', '1001', 1.44, 1), 
       (default,'idCliente88', 'idProduct24', '1002', 21, 3);
~~~

~~~
INSERT INTO invoices (person_id) VALUES ('50') RETURNING id;

INSERT INTO invoice_items
VALUES (default,'idCliente50', '31', '1000', 1.44, 3), 
       (default,'idCliente50', '24', '1001', 21, 12); 
~~~

~~~
INSERT INTO invoices (person_id) VALUES ('idCliente39') RETURNING id;

INSERT INTO invoice_items
VALUES (default, '86', '1000', 14.11, 1);
~~~

~~~
INSERT INTO invoices (person_id) VALUES ('idCliente33') RETURNING id;

INSERT INTO invoice_items
VALUES (default,'14', '86', '1000', 14.11, 1);
VALUES (default,'14', '86', '1000', 1.44, 12);
~~~

# consultas de agrupación

### DISTINCT
consulta la información distinguiendo la proyección  
osea me trae el dato unico del campo a consultar, si hay mas de 1 lo agrupara  
podemos investigar los registros unicos de la tabla (emails unicos, nombres unicos)  

~~~
SELECT DISTINCT first_name FROM persons;
~~~

### GROUP BY
debe contener los campos proyectados a excepción de las funciones  
osea si llamamos a buscar los 2 campos de nombre y apellido, debemos agrupar los 2 campos tambien.  
~~~
SELECT first_name Last_name FROM persons GROUP BY first_name, Last_name;
~~~

### Funciones
|||
|-|-|
| count(*) | conteo de registros |
| sum(price * quantity) | va a sumar el total|

#### Ejercicios: 
~~~
SELECT first_name COUNT(*) FROM persons GROUP BY first_name; // trae los registros agrupados, y cuantos hay

SELECT COUNT(*) FROM persons; // me dice cuantos registros tengo en total
~~~

Cuanto es el total de venta de cada factura 
~~~
SELECT idFactura, sum(price * quantity)
FROM invoice_items
GROUP BY idFactura;
~~~

~~~
SELECT product_id, COUNT(*) AS Registros, SUM(price * quantity) valor_venta, SUM(quantity) cantidad
FROM invoice_items
GROUP BY product_id
ORDER BY 4;
~~~

# HAVING 
Es la clausula ***WHERE*** pero por grupos de registros  
ejemplo: cuantas compras ha hecho un cliente  
osea: valido los grupos y comparo los resultados  

#### forma facil
~~~
SELECT persons_id, COUNT(*) AS Cantidad
FROM invoices
GROUP BY person_id
ORDER BY 2 DESC;
~~~

#### forma con having
~~~
SELECT persons_id, COUNT(*) AS Cantidad
FROM invoices
GROUP BY person_id
HAVING COUNT(*) >= 2;
~~~

# LIMIT Y OFFSET
permite limitar la cantidad de registros devueltos  
sirve para paginar las consultas.  

~~~
SELECT * FROM products LIMIT 3 OFFSET 0; // Página 1
SELECT * FROM products LIMIT 3 OFFSET 3; // Página 2
SELECT * FROM products LIMIT 3 OFFSET 6; // Página 3
SELECT * FROM products LIMIT 3 OFFSET 9; // Página 4
~~~

lo que hace es cargar la página con los registros limite por página  
esto se hace en el backend de nuestra aplicación  

|Formula para Paginación | 
|:---|
| offset = página * límite - límite |
| offset = 1 * 5 - 5 = 0 | 
| offset = 2 * 5 - 5 = 5 | 
| offset = 3 * 5 - 5 = 10 | 

