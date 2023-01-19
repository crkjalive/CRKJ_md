# SQL Consultas Avanzadas

## Sentencias en la estructura de la base de datos
1. CREATE DATABASE MyDataBase; ***crea base de dadtos***
2. SHOW DATABASES; ***muestra las bases de datos creadas***
3. SHOW TABLES; ***muestra las tablas creadas***
4. USE MyDataBase; ***seleccionar database***
5. DROP DATABASE MyDataBase; ***borrar base de datos***
6. DESC MyDataBase; ***abreviado, estructura de la base de datos***
7. DESCRIBE MyTable; ***estructura de la tabla***

## Sentencias en consultas de registros de la base de datos
### SELECT
1. SELECT * FROM ***MyTable***; ***busca todo lo que contenga la tabla***
2. SELECT name, email, phone FROM ***MyTable***; ***busca datos en los campos especificos***
3. SELECT email, (7+7) AS 'OPERACIONES' FROM ***MyTable***; ***Operacion con alias AS***
4. SELECT id, nombre, email, (id+27) AS suma FROM ***MyTable*** ORDER BY suma DESC; ***Ordenado ASC y DESC***
5. SELECT * FROM ***MyTable*** WHERE email = 'jared@gmail.com'; ***condiciona la busqueda a 1***
6. SELECT email FROM ***MyTable*** WHERE apellido LIKE '%a%' AND password = '1234'; ***busca con like que contenga la a y la clave sea 1234***
7. SELECT * FROM ***MyTable*** WHERE (YEAR(fecha) % 2 = 0); ***busca Pares***
7. SELECT * FROM ***MyTable*** WHERE (YEAR(fecha) % 2 != 0); ***busca Impares***
8. SELECT UPPER(nombre), apellido FROM ***MyTable*** WHERE (LENGTH(nombre) > 5) AND YEAR(fecha) < 2022; ***name > 5, fecha < 2022***
9. SELECT id, nombre FROM ***MyTable*** ORDER BY nombre desc LIMIT 4, 3; ***3 registros y en orden descendente, desde el 5 registro***
10. SELECT COUNT(titulo) FROM posts GROUP BY categoria_id; ***cuenta los titulos y agrupa por id***
11. SELECT COUNT(titulo) AS 'Numero de posts', categoria_id FROM posts GROUP BY categoria_id HAVING COUNT(titulo) >= 3; ***having es lo mismo que el WHERE pero para grupos***
12. SELECT AVG(id) 'promedio de posts' FROM posts; ***promedio de post***
13. SELECT SUM(id) AS 'suma de id' FROM posts; ***sumatoria de id***

### INSERT
1. INSERT INTO ***MyTable*** VALUES (null, 'name', 'lastName', 'email', '3122405060', '2019-05-01'); ***insertar datos***

### UPDETE 
1. UPDATE ***MyTable*** SET fecha=CURDATE(), apellido='cero' WHERE id=1; ***actualiza a la fecha actual el id 1***

### DELETE
1. DELETE FROM ***MyTable*** WHERE id = 8; ***elimina el registro con id 8***
2. DELETE FROM ***MyTable*** WHERE email = 'admin@admin.com'; ***elimina el registro con ese email***

# Subconsultas
consiste en hacer consultas dentro de otras consultas  
utiliza los resultados de la subconsulta para operar en la consulta principal  
se optiene jugando con las claves ajenas / foraneas  

## Operador IN
1. SELECT * FROM ***usuarios*** WHERE id IN (SELECT usuario_id FROM ***posts***); ***busca id de usuario que coincidan con los de post***

## Operador NOT IN
1. SELECT * FROM usuarios WHERE id NOT IN (SELECT usuario_id FROM posts); ***busca lo que NO coincida en la consulta***

## SELECT IN
1. SELECT nombre, apellido FROM usuarios WHERE id IN (SELECT usuario_id FROM posts WHERE titulo LIKE '%man'); ***obtener los usuarios que en algun post en su titulo contenga man***
2. SELECT titulo FROM posts WHERE categoria_id IN (SELECT id FROM categorias WHERE nombre='accion') ***obtener todos los post de accion, usando su nombre***
3. SELECT * FROM categorias WHERE id IN (SELECT categoria_id FROM posts GROUP BY categoria_id HAVING COUNT(categoria_id) >=5); ***mostrar las categorias con mas de 5 entradas***
4. SELECT * FROM usuarios WHERE id IN (SELECT usuario_id FROM posts WHERE dayofweek(fecha)=3); ***usuarios que crearon un posts un martes***
5. SELECT usuario_id, COUNT(id) FROM posts GROUP BY usuario_id ORDER BY COUNT(id) DESC; ***busca usuario con mas post***
6. SELECT nombre FROM usuarios WHERE id IN (SELECT usuario_id, COUNT(id) FROM posts GROUP BY usuario_id ORDER BY COUNT(id) DESC LIMIT 1 ); ***subconsulta completa***
7. SELECT * FROM categorias WHERE id IN (SELECT categoria_id FROM posts); ***busca categorias con post***
8. SELECT * FROM categorias WHERE id NOT IN (SELECT categoria_id FROM posts); ***busca categorias SIN post***  

# Consultas multitablas y joins
consiste en hacer una consulta de varias tablas  
Debemos hacer la condicion comparando los id de las llaves foraneas  
con el fin de que coincidan los datos almacenados en las tablas  

~~~
SELECT campo1,campo2,campo3 
FROM tabla1, tabla2, tabla3
WHERE e.usuario_id = u.id AND e.categoria_id = c.id
~~~

### Tabla de ejemplo
Esta tabla hace las consultas y subconsultas ***NO PRESENTABLE***  

> id, usuario_id, categoria_id, titulo, descripcion, fecha  

|id|id|id|name|name|date|
|-|-|-|-|-|-|
|1|1|1|ironman|tony stark|2021-05-31|
|2|1|1|spiderman|piter parker|2021-05-31
|3|1|1|american captain|steven grant rogers|2021-05-31|
|4|1|2|wonder woman|lilli aspell|2021-05-31|
|5|2|2|batman|bruce wein|2021-05-31|
|6|2|2|flashjay|garrick|2021-05-31|
|7|2|2|superman|clar ken|2021-05-31|
|8|2|2|joker|jack naiper|2021-05-31|
|9|3|3|wolverin|logan|2021-05-31|
|10|3|3|magneto|poder de manejar el hierro a voluntad|2021-05-31|
|11|3|3|profesor x|charlis francis xavier|2021-05-31|
|12|3|3|mystique|jenifer lawrens|2021-05-31|
|13|1|3|fenix|jean grey|2021-05-31|
|14|1|3|storm|Ororo Iqadi Munroe|2021-05-31|
|15|1|3|scarlet witch|wanda maximoff|2021-05-31|
|16|5|3|chanchi feliz|Hola mundo desde SQL subconsulta|2021-06-01|

### Consulta haciendo referencia a los campos de las tablas
~~~
SELECT usuarios.id , usuarios.nombre as 'usuario', posts.titulo as 'super heroe', posts.descripcion as 'nombre real',  categorias.nombre as 'compañia', posts.fecha
FROM posts, usuarios, categorias
WHERE posts.usuario_id = usuarios.id AND posts.categoria_id = categorias.id ORDER BY usuarios.id;
~~~

### La misma tabla con ALIAS
~~~
SELECT u.id , u.nombre as 'User', p.titulo as 'Hero', p.descripcion as 'Secret person',  c.nombre as 'Company', p.fecha as 'Date'
FROM posts p, usuarios u, categorias c
WHERE p.usuario_id = u.id AND p.categoria_id = c.id ORDER BY u.id;
~~~

### SELECT con ALIAS
mostrar el nombre de las categorias y al lado cuantos posts tienen  
1. SELECT c.nombre, COUNT(p.id) FROM categorias c, posts p WHERE p.categoria_id = c.id GROUP BY p.categoria_id;
2. SELECT u.email, count(titulo) FROM usuarios u, posts p WHERE p.usuario_id = u.id group by p.usuario_id;

# INNER JOIN
el inner join los que hace es una combinacion interna entre dos tablas  
Con inner join trae la información más rápido para muchos registros  
***inner join*** cruza las tablas y muestra los registros que contengan datos y coincidan con ***ON*** y la condicion

1. SELECT p.id, p.titulo, u.nombre AS 'User', c.nombre AS 'categoria' FROM posts p INNER JOIN usuarios u ON p.usuario_id = u.id INNER JOIN categorias c ON p.categoria_id = c.id;
2. SELECT p.id, p.titulo, u.nombre AS 'User' FROM posts p INNER JOIN usuarios u ON p.usuario_id = u.id;

# LEFT JOIN
Left join me trae lo que este en la tabla de la izquierda, asi no tenga registros.  
manteniendo las filas de la izquierda, asi tenga registros en 0 o null  

1. SELECT categorias.nombre, COUNT(posts.id) FROM categorias LEFT JOIN posts ON posts.categoria_id = categorias.id GROUP BY posts.categoria_id;

# RIGTH JOIN
Mantiene todas las filas de la tabla de la derecha, tengan registros en 0 o null  

1. SELECT c.nombre, COUNT(p.id) FROM posts p RIGTH JOIN categorias c ON p.categoria_id = c.id GROUP BY p.categoria_id;

# VISTAS EN MYSQL
- Es almacenar una consulta en un nombre, simplificando volver hacer toda la sentencia
- una consulta almacenada en la base de datos que se utiliza como tabla virtual
- No almacena datos si no que utiliza asociaciones y los datos originales de las tablas, de forma que siempre se mantiene actualizada
- las consultas virtuales se visualizan mostrando las tablas, ya que no existe comando para ver las vistas almacenadas

### Creacion de una vista 
~~~
CREATE VIEW posts_por_categorias AS
SELECT c.nombre, COUNT(p.id)
FROM posts p
RIGHT JOIN categorias c ON p.categoria_id = c.id
GROUP BY p.categoria_id;
~~~

1. SHOW tables; ***consultar las vistas creadas y las tablas***
2. SELECT * FROM posts_por_categorias; ***consultar la vista***
3. SELECT * FROM posts_por_categorias WHERE nombre='marvel'; ***consulta vista y llama un dato específico***
4. DROP VIEW posts_por_categorias; ***borrar vista***



