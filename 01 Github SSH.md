# SSH
- ssh-keygen -t rsa -b 4096 -C "0soundlive@gmail.com"

### que significa cada campo
1. ssh-keygen -t rsa - ***especifica el algoritmo***
2. -b 4096 # - ***bits de encriptacion***
3. -C # - ***correo de la llave***

### passphrase: # 
agregamos passphrase, este permite crear contraseña con espacios 

### comprobar el proceso y agregarlo a windows
evalua que quede funcionando esta configuración  
1. eval $(ssh-agent -s)

### agregamos la llave al entorno de windows
1. ssh-add ~/.ssh/id_rsa

# configuración en MAC 
1. eval "$(ssh-agent -s)"

~~~
config
	Host *
		AddKeysToAgent yes
		UseKeychain yes
		IdentityFile ~/.ssh/id_rsa 
~~~

siempre debe haber llaves por equipo que se usa 

~~~
git config -l // todos los comandos 
git config --global user.email "EmailUser"
git config --global user.name "NameUser"
~~~

# agregar llaves a Github 
paso a paso, para dejar el repo sin que toque poner las llaves de autenticación  
en github configuramos  

1. settings
2. SSH and GPG keys
3. name
4. id_rsa.pub ***codigo a pegar***
5. agregar y listo

# prueba de fuego
ponemos a prueba la configuración anterior  

1. git clone urlRepo 
2. entramos al repo - cd repo 
3. creamos un archivo README.md para enviar - touch README.md
4. git add . - agregamos todos los cambios
5. git commit -am "agregamos detalles" - 
6. git push - mandamos los cambios a Github
7. ya no pide contraseña ni nada para enviar - pide contraseña si no hemos agregado las keys















