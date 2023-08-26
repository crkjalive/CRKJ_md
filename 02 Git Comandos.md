# Git Comandos
1. git init ***inicia proyecto***  

2. git add file.txt  ***añadir archivo especifico al repo local***  
3. git add . ***agrega todos los cambios al repo***  

4. git commit -m 'version 1' ***mesaje para agregar al repo local***  
5. git status ***muestra y valida si hay cambios sin agregar al repo***  

6. git push ***(origin master) envia repo a server***  
7. git pull ***(origin footer) trae repo del server***  

8. git log --stat ***ver los cambios especificos***  
9. git log file.txt ***todos los cambios historicos***   
10. git show ***muestra los ultimos cambios y propiedad del repo***   

11. git rm file.txt ***traked agrega los cambios***  
12. git rm --cached file.txt ***untraked quita los cambios***  

### configuracion git
1. git config ***configuracion***  
2. git config --list ***configuracion default***   
3. git config --global user.name ***usuario***  
4. git config --global user.email ***email***   

5. git diff commitA commitB ***miro y comparo los cambios***  
6. git rebase master ***(experimento) reescribe la rama***   

7. git reset "indicador commit A" --SOFT ***reset suave***  
8. git reset "indicador commit B" --HARD ***reset fuerte***   
9. git reset --HARD "id" ***borra hasta la rama***  

10. git checkout 'rama' ***me muevo entre ramas***  
11. git checkout "indicador Commit" file.txt ***volver a version***  

12. git clone url ***trae los datos de repo***  

13. git fetch ***trae cambios nuevos a repo local***  
14. git merge ***(master) trae a directorio de trabajo***   
15. (master) git merge header ***fusion master y header***  

16. git branch cabecera ***envia repo local***  

17. git remote add origin 'url' ***añadimos el repo de github***  

### primera vez que se fusionan los repos
1. git pull origin master --alow-unrelated-histories

### graficamos en consola las ramas 
1. git log --all --graph --decorate --oneline

### tags versionando los commit
1. git tag -a 'mensaje' codeIndicador v1.0  

1. git stash list  
2. git stash pop  
3. git stash brand english-version  

### Eenvia los cambios nuevos a una rama nueva 
1. git stash drop

1. git clean --dry-run ***simula lo que va a limpiar*** 
2. git log --oneline ***muestra lista de commit***  
3. git cherry-pick 'indicador commit' ***trae commit anteriores***  
4. git commit amend ***editamos el commit***  
5. git branch -D cabecera ***eliminamos rama***  

# buscar palabras
1. git grep -n platzi

# buscar cantidad de palabras 
1. git grep -c palabraBuscar

# quien modifico
1. git blame index.html ***quien modifico que***  
2. git blame css/estilos.css L35,53 ***de la linea 35 a la 53***  
3. git blame css/estilos.css L35,53 -c ***mas formato***  


# llaves SSH
- ssh-keygen -t rsa -b 4096 -C "micorreo"  
- passphrase (creamos clave, acepta espacios)  

- .ssh ***directorio de llaves cifradas***  

- d_rsa ***private key***  
- d_rsa.pub ***public key***  

## servicio ssh-agent 
eval $(ssh-agent -s)  
> Agent pid 198  

ssh-add ~/.ssh/id_rsa ***agregamos al sistema***  