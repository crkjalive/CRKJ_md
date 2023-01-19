# SQL Comandos
### Eliminar la base de datos
~~~
DROP DATABASE MyDataBase;
~~~

### Crea una base de datos nueva
~~~
CREATE DATABASE MyDataBase;
~~~

### Use DATABASE como base de datos
~~~
USE MyDataBase;
~~~

### Elimina tabla
~~~
DROP TABLE my_table;
~~~

### Limpia los datos de la tabla a cero
~~~
TRUNCATE my_table;
~~~

### Crear tablas
~~~
CREATE TABLE my_table(id int, email varchar(255), username varchar (50));
~~~

### Eliminar la columna
~~~
ALTER TABLE my_table DROP COLUMN edad;
~~~

### Agregar columna
~~~
ALTER TABLE my_table ADD edad INT;
~~~

### Modificar el tipo de dato
~~~
ALTER TABLE my_table MODIFY COLUMN email varchar(50);
~~~

### Agregar llave primaria
~~~
ALTER TABLE my_table ADD primary key (id);
~~~

### Agrega autoincremental al id
~~~
ALTER TABLE my_table MODIFY COLUMN id INT auto_increment;
~~~

# Consultas SQL

### INSERTAR registro
~~~
INSERT INTO my_table(email, username, edad)
VALUES ('jared@correo.com', 'Jared', 1);
~~~

### ELIMINAR registro (limita a 1 solo)
~~~
DELETE FROM my_table WHERE email = 'chanchito@correo.com' limit 1; 
~~~

### LEER registros (buscar todos los registros y buscar por email especifico)
~~~
SELECT * FROM my_table;
SELECT * FROM my_table WHERE email='chanchito@correo.com'; 
~~~

### BUSCAR condicionando la consulta
~~~
SELECT * FROM my_table WHERE edad > 21;
~~~

### ACTUALIZAR registro (WHERE previene actualizar todos los registros de la tabla)
~~~
UPDATE my_table SET email = 'felix@correo.com' WHERE id = '18'; 
~~~

### ELIMINAR (pendiente de WHERE)
~~~
DELETE FROM my_table WHERE id ='2';
~~~

