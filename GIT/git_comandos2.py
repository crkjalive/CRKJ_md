""" solo comandos """

git init # inicia proyecto

git add file.txt # añadir repo local
git add . # agrega todos los cambios

git commit -m 'version 1'# mesaje para agregar al repo local
git status # estado de repo si hay cambios

git push # (origin master) envia repo a server
git pull # (origin footer) trae repo del server

git log stat # ver los cambios especificos
git log file.txt # todos los cambios historicos 
git show # muestra los cambios 

git rm file.txt # traked agrega los cambios
git rm --cached file.txt # untraked quita los cambios

git config # configuracion 
git config --list # configuracion default 
git config --global user.name # usuario
git config --global user.email # email 

git diff commitA commitB # miro y comparo los cambios
git rebase master # (experimento) reescribe la rama 

git reset "indicador commit A" --SOFT #reset suave
git reset "indicador commit B" --HARD # reset fuerte 
git reset --HARD "id" # borra hasta la rama  

git checkout 'rama' # me muevo entre ramas
git checkout "indicador Commit" file.txt # volver a version

git clone url # trae los datos de repo 

git fetch # trae cambios nuevos a repo local
git merge # (master) trae a directorio de trabajo 
(master) git merge header # fusion master y header 

git branch cabecera # envia repo local

git remote add origin 'url' # añadimos el repo de github 

# primera vez que se fusionan los repo 
git pull origin master --alow-unrelated-histories

# graficamos en consola las ramas 
git log --all --graph --decorate --oneline

# tags versionando los commit
git tag -a 'mensaje' codeIndicador v1.0

git stash list 
git stash pop 
git stash brand english-version 
# envia los cambios nuevos a una rama nueva 
git stash drop

git clean --dry-run # simula lo que va a limpiar 
git log --oneline # muestra lista de commit
git cherry-pick 'indicador commit' # trae commit anteriores
git commit amend # editamos el commit 
git branch -D cabecera # eliminamos rama

# buscar palabras
git grep -n platzi
# buscar cantidad de palabras 
git grep -c palabraBuscar
# quien modifico
git blame index.html # quien modifico que 
git blame css/estilos.css L35,53 # de la linea 35 a la 53,  
git blame css/estilos.css L35,53 -c # mas formato  


""" llaves SSH """ 
ssh-keygen -t rsa -b 4096 -C "micorreo"
passphrase (clave con espacios si queremos)

.ssh # directorio de llaves cifradas 

d_rsa # private key 
d_rsa.pub # public key

# servicio ssh-agent 
eval $(ssh-agent -s)
> Agent pid 198

ssh-add ~/.ssh/id_rsa # agregamos al sistema










