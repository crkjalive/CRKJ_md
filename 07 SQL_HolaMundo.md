### eliminar la base de datos
- drop database prueba;

### crea una base de datos nueva
- create database prueba;

### usar prueba como base de datos
- use prueba;

### elimina tabla
- drop table usuario;

### limpia los datos de la tabla a cero
- truncate usuario;

### crear tablas
- create table usuario(id int, email varchar(255), username varchar (50));

### eliminar la columna
- alter table usuario drop column edad;

### agregar columna
- alter table usuario add edad int;

### modificar el tipo de dato
- alter table usuario modify column email varchar(50);

### agregar llave primaria
- alter table usuario add primary key (id);

### agrega autoincremental al id
- alter table usuario modify column id int auto_increment;

### Consultas SQL

### INSERTAR registro
~~~
insert into usuario(email, username, edad)
values ('jared@correo.com', 'Jared', 1);
~~~

### ELIMINAR registro (limita a 1 solo)
~~~
delete from usuario where email = 'chanchito@correo.com' limit 1; 
~~~

### LEER registros (buscar todos los registros y buscar por email especifico)
~~~
select * from usuario;
select * from usuario where email='chanchito@correo.com'; 
~~~

### Buscar condicionando la consulta
~~~
select * from usuario where edad > 21;
~~~

### ACTUALIZAR registro (where previene actualizar todos los registros de la tabla)
~~~
update usuario set email = 'felix@correo.com' where id = '18'; 
~~~

### ELIMINAR (pendiente de WHERE)
~~~
delete from usuario where id ='2';
~~~

