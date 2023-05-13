Video 1
# Consultas entre tablas
Relacionar la tablas en la consultas  

funciona con la teoría de los conjuntos  

~~~
SELECT COUNT(*) FROM tabla_a; // 5 registros
SELECT COUNT(*) FROM tabla_b; // 10 registros
~~~
Estas consultas me traerian 50 registros  

***Esta consulta es natural para SQL en el plano cartesiano***  

~~~
SELECT * FROM tabla_a, tabla_b;
~~~

# CROSS JOIN
como podemos filtrar la información en la tabla para que no me traiga todas  
las consultas cruzadas por cada registro de cada tabla  

~~~
SELECT * FROM tabla_a CROSS JOIN tabla_b;
~~~

# Proyecto de pruebas
~~~
CREATE TABLE tabla_a (
	id INT NOT NULL,
    description VARCHAR(50) NOT NULL,
    CONSTRAINT tabla_b_id_pk PRIMARY KEY (id)
);
~~~

~~~
CREATE TABLE tabla_b (
	id INT NOT NULL,
    title VARCHAR(50) NOT NULL,
    CONSTRAINT tabla_b_id_pk FOREIGN KEY (id) REFERENCES tabla_a (id)
    ON UPDATE RESTRICT
    ON DELETE RESTRICT
);
~~~

### poblado de tablas 
~~~
INSERT INTO tabla_a VALUES (5,'FIVE');
INSERT INTO tabla_b VALUES (1,'ONE'), (2,'TWO'), (3,'THREE');
~~~

# CROSS JOIN
genera que por cada elemento de la tabla a,  va a cruzarlo con cada uno  
de los elementos de la tabla b  

Debemos especificar como vamos a filtrar esa información, 
~~~
SELECT * FROM `tabla_a` CROSS JOIN `tabla_b`;
~~~

|id|description|id|title|	
|-|-|-|-|
|1|UNO|1|ONE|
|1|UNO|2|TWO|
|1|UNO|3|THREE|
|1|UNO|4|FOR|
|2|DOS|1|ONE|
|2|DOS|2|TWO|
|2|DOS|3|THREE|
|2|DOS|4|FOR|
|3|TRES|1|ONE|
|3|TRES|2|TWO|
|3|TRES|3|THREE|
|3|TRES|4|FOR|
|4|CUATRO|1|ONE|
|4|CUATRO|2|TWO
|4|CUATRO|3|THREE
|4|CUATRO|4|FOR|
|5|FIVE|1|ONE|
|5|FIVE|2|TWO|
|5|FIVE|3|THREE|
|5|FIVE|4|FOR|

# Natural JOIN
Así asocia los id entre tablas  
busca los elementos de la tabla_a, que coincidan con la tabla_b  
en el nombre ***igual*** entre tablas a y b  

~~~
SELECT * FROM `tabla_a` NATURAL JOIN `tabla_b`;
~~~

|id|description|title|
|-|-|-|
|1|UNO|ONE|
|2|DOS|TWO|
|3|TRES|THREE|
|4|CUATRO|FOR|

Lo que hace el natural join es relacionar las dos tablas por el nombre del campo igual  
a el de las dos tablas (id).  
que son son campos que coinciden  

Natural Join no busca por llave foranea, si no por campo con el mismo nombre  

Video 2
# INNER JOIN 
Muestra los registros que coincidan en ambos conjuntos  
son todos los elementos que conincidan tanto en la tabla a como en la tabla b  
especificamente le damos la instrucción a los campos que deben coincidir  
![INNER JOIN](img/inner%20join.png)

# LEFT JOIN 
Muestra todos los registros de la tabla de la ***IZQUIERDA*** y aquellos que coincidan  
con la tabla de la ***DERECHA***  
![LEFT JOIN](img/left%20join.png)

# RIGHT JOIN
Muestra todos los registros de la tabla de la ***DERECHA*** y aquellos que coincidan  
con la tabla de la ***IZQUIERDA***  
![RIGHT JOIN](img/right%20join.png)

# FULL JOIN 
Muestra todos los registros de ambas tablas y muestra los que tienen relación entre ellas.  
![FULL JOIN](img/full%20join.png)

Debemos decirle a los join explicitamente cuales son los campos que vamos a relacionar  
entre la tabla a y la tabla b.  

Especificando cuales son los campos con los que se deben relacionarse

~~~
SELECT * FROM persons;
SELECT * FROM invoices;

SELECT * 
FROM persons INNER JOIN invoices 
ON persons.id = invoices.persons_id;
~~~

la consulta se debe relacionar con ***ON*** por el campo que relaciona la tabla a y la tabla b.  

### Filtrar consulta

~~~
SELECT persons.id, persons.first_name, persons.last_name, persons.birthday, invoices.invoice_date
FROM persons 
INNER JOIN invoices ON persons.id = invoices.persons_id; 
~~~

Inner join: es decir todos aquellos registros de la tabla a, que coincidad con  
la tabla b en sus campos id y persosn_id

### Más consultas a la consulta 
podemos hacer más subconsultas, con ***INNER JOIN***  

~~~
SELECT persons.id, persons.first_name, persons.last_name, 
persons.birthday, invoices.invoice_date
products.product_name, invoice_items.price, invoice_items.quantity
(invoice_items.quantity * invoice_items.price)

FROM persons 

INNER JOIN invoices ON persons.id = invoices.persons_id
INNER JOIN invoice_items ON invoices.id = invoice_items.invoice_id;
INNER JOIN products 
~~~

con INNER JOIN no importa cual es la tabla A o B, ya que va a relacionar todo  
los que coincida entre la dos tablas

Video 3

## Left Join 
Nos va a traer lodos aquellos registros de la tabla A  
y todos los registros que coincidan entre la tabla A y la tabla B  

Ejemplo: Mostrar todos nuestros clientes (Usuarios), así no hayán comprado  

~~~
SELECT first_name, last_name, invoice_date
FROM persons LEFT JOIN invoices
ON persons.id = invoices.person_id; 
~~~

Con ***LEFT JOIN***, Me va a traer todos los registros de la tabla persons  
así no tenga registros en la tabla invoices  
y sí hay coincidencias en la tabla invoices me los mostrará támbien  

## RIGHT JOIN 
siendo la misma consulta me va a traer todos los registros de la tabla de la ***DERECHA***  
y tambien los registros que coincidan con la tabla de la ***IZQUIERDA***  

Hay que tener claro que dependiendo de la posicion antes del join será la tabla de la ***DERECHA***,  
y despues del JOIN será la tabla de la ***IZQUIERDA***

~~~
SELECT first_name, last_name, invoice_date
FROM  invoices RIGHT JOIN persons
ON persons.id = invoices.person_id; 
~~~

Video 3 7:43 full join

## Full Join 
Me trae todo los que tiene la tabla A, los registros que coincida con la tabla B,  
y los registros de la tabla B  

~~~
SELECT * FROM alpha FULL JOIN gama
    ON alpha.id = gama.id;
~~~
me va a traer todo los registros de la tabla alpha, de la tabla gama,  
y los que coincidan entre alpha y gama  

para que utilizamos FULL JOIN  
nos facilita la busqueda de informacion escondida, registros de algunas tablas que no  
tienen una relación directa, facilitando el analisis de datos  
