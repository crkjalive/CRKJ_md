# SSH
ssh-keygen -t rsa -b 4096 -C "0soundlive@gmail.com"

ssh-keygen -t rsa //especifica el algoritmo
-b 4096 # bits de encriptacion
-C # correo de la llave

passphrase: # contraseña con espacios 

# comprobar el proceso y agregarlo a windows
```eval $(ssh-agent -s)```

# agregamos la llave al entorno de windows
```ssh-add ~/.ssh/id_rsa```

#en mac 
```
eval "$(ssh-agent -s)"

config
	Host *
		AddKeysToAgent yes
		UseKeychain yes
		IdentityFile ~/.ssh/id_rsa 
```

siempre debe haber llaves por equipo que se usa 

```
git config -l 
git config --global user.email "0soundlive@gmail.com"
```

# agregar llaves a Github 
1. settings
2. SSH and GPG keys
3. name
4. id_rsa.pub ***codigo a pegar***
5. agregar y listo