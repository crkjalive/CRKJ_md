# VIM configuración
***neovim o vim*** 

### VIM
~~~
curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
~~~

### NVIM
~~~
khriz@DESKTOP-PTH1GTA:~/.local/share/nvim/site/autoload$  plug.vim
~~~

### Linux
> sudo apt install neovim

### Mac
> brew install --HEAD neovim

# Configurando vim y nvim (Video 17)

### nvim
Estas lineas lo que hacen es usar el mismo archivo de configuración de vim en nvim

ruta /.config/nvim/init.vim

```
set runtimepath^=~/.vim runtimepath+=~/.vim/after
let &packpath=&runtimepath
source ~/.vimrc
```
esté código debería de configurarse así (holaMundo)

luego de esas lineas editamos el archivo de .vimrc
___

|init.vim|
|-|
|set number|numeros a la izquierda|
|set mouse=a|habilita el mouse dentro de nvim|
|set numberwidth=1|ancho de los numeros|
|set clipboard=unnamed|no queda en el clipboard si copio|
|syntax enable|habilita la sintaxis, resaltado de color|
|set showcmd|muestra los comandos que se estan ejecutando|
|set ruler|posicion dentro de nvim|
|set encoding=utf-8|caracteres|
|set showmatch|resalta los parentesis de cierre|
|set sw=2|cantidad de espacios a 2|
|set relativenumber|me apunta en cero|
|set laststatus=2|barra siempre visible|
|set noshowmode|oculta los modos de trabajo|
|set cursorline|linea en el cursor|

# Instalando gestor de extensiones
se busca por plug vim
[manager de plugins](https://github.com/junegunn/vim-plug)

junegunn/vim-plug: Minimalist Vim Plugin Manager - GitHub

# para linux
crea una carpeta de autoload / plug.vim
```
sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
```
# configuramos la ruta de los plugins 
1. sudo apt install git 
2. para que instale los plugs :PlugInstall

```
call plug#begin('~/.vim/autoload/plugged')
```
___

|Instalamos los plug|
|-|-|-|
| call plug#begin('ruta del autoload/plugged')| carga ruta de plugins|
| Plug 'morhetz/gruvbox'| tema grubvox |
| colorscheme gruvbox | aplica el tema |
| let g:gruvbox_contrast_dark = "hard" | configura el color del tema |
| Plug 'easymotion/vim-easymotion'| nos permite navegar desde cualquier parte de nuestro codigo, y buscar segun la tecla a oprimir|
| nmap<leader>s <Plug>(easymotion-s2) | leader + s para buscar la posicion y saltar | 
| Plug 'scrooloose/nerdtree' | plug arbol de directorios o menu | 
| nmap<leader>nt :NERDTreeFind<CR> | space + nt | directorios |
| m | para abrir el menu | 
| let NERDTreeQuitOnOpen=1 | cierra automaticamente el arbol de directorios|
| let mapleader=" " | space como tecla lider |
| Plug 'christoomey/vim-tmux-navigator' | navegar entre ventanas | CTRL h/l |


|creando atajos personalizados|
|-|-|
| nmap ```<leader>```w :w```<CR>``` | space + w | gardar |
| nmap ```<leader>```q :q```<CR>``` | space + q | salir |

// asi quedo el directorio y el fichero final

neovim
.config/nvim/init.vim
.vim/autoload/plug.vim
.vim/plugged

___

### init.vim
~~~
" Configuracion nvim y sus plug
set number
set mouse=a
set numberwidth=1
set clipboard=unnamed
syntax enable
set showcmd
set ruler
set encoding=utf-8
set showmatch
set sw=2
set relativenumber
set laststatus=2
"set noshowmode 

call plug#begin()

" Thems o temas 
Plug 'morhetz/gruvbox'

" IDE
Plug 'easymotion/vim-easymotion' "buscar y saltar
Plug 'scrooloose/nerdtree' "directorios
Plug 'christoomey/vim-tmux-navigator' "saltar ventanas control l o h
Plug 'mattn/emmet-vim' "plug de emmet

call plug#end()

colorscheme gruvbox

let g:gruvbox_contrast_dark = "hard"
let mapleader=" "
let NERDTreeQuitOnOpen=1

"easymotion space + s buscar posicion saltar
nmap<leader>s <Plug>(easymotion-s2)

"arbol de directorios space + nt
nmap<leader>nt :NERDTreeFind<CR>

nmap<leader>w :w<CR> "space w write 
nmap<leader>q :q<CR> "space q salir

inoremap ( ()<Esc>i
inoremap { {}<Esc>i
inoremap [ []<Esc>i
inoremap < <><Esc>i
inoremap ' ''<Esc>i
inoremap " ""<Esc>i
inoremap < <><Esc>i
inoremap ' ''<Esc>i
inoremap ppp print("")<Esc>hi
inoremap ppl console.log("")<Esc>hi
~~~