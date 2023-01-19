# SQL
1. CREATE DATABASE MyDataBase; ***Crea una base de datos nueva***
2. DROP DATABASE MyDataBase; ***Eliminar la base de datos***
3. USE MyDataBase; ***Use DATABASE como base de datos***
4. TRUNCATE MyTable; ***Limpia los datos de la tabla a cero***
5. DROP TABLE MyTable; ***Elimina tabla***
6. CREATE TABLE MyTable(id(int) PRIMARY KEY AUTO_INCREMENT, username varchar(50), email varchar(100)); ***Crear tablas***
7. ALTER TABLE MyTable DROP COLUMN edad; ***Eliminar la columna***
8. ALTER TABLE MyTable ADD edad INT; ***Agregar columna***
9. ALTER TABLE MyTable MODIFY COLUMN email varchar(50); ***Modificar el tipo de dato***
10. ALTER TABLE MyTable ADD primary key (id); ***Agregar llave primaria***
11. ALTER TABLE MyTable MODIFY COLUMN id INT auto_increment; ***Agrega autoincremental al id***

# Consultas
***LEER registros (WHERE) condiciona***  
SELECT * FROM MyTable;  
SELECT * FROM MyTable WHERE email='chanchito@correo.com';  
SELECT * FROM MyTable WHERE edad > 21;

***INSERTAR registro***  
INSERT INTO MyTable(email, username, edad) VALUES ('jared@correo.com', 'Jared', 1);

***ACTUALIZAR registro (WHERE) solo el registro***  
UPDATE MyTable SET email = 'felix@correo.com' WHERE id='18'; 

***ELIMINAR registro (limita a 1 solo)***  
DELETE FROM MyTable WHERE email = 'chanchito@correo.com' limit 1;  
DELETE FROM MyTable WHERE id='2';