# TERMINAL 

### actualizar sistema linux
sudo apt update && upgrade

### pip
sudo apt install python3-pip

### nodejs
sudo apt install nodejs

### nodejs nvm 
instala nvm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash

activa nvm
```source ~/.bashrc```

version a instalar de nodejs
nvm install v14.x

### npm
sudo apt install npm

### git
sudo apt install git

### zsh
sudo apt install zsh

### repo oh my zsh
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

### default
chsh -s /usr/bin/zsh

### ~ /.bashrc
al inicio
~~~
if test -t 1; then
exec zsh
fi
~~~

### neovim
sudo apt install neovim

### comprobacion
nvim +checkhealth

### curl
sudo apt install curl
~~~
curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
~~~

### plug neovim 
sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'

### Comandos terminal
|accion|comando|
|-|-|
|copiar | cp file.txt ~destino |
|mover | mv file.txt ~destino |
|elimina | rm + file |
|eliminar directorio | rm -rf carpeta |


