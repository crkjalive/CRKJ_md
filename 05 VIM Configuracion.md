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
|set clipboard+=unnamedplus|habilita copiar y pegar entre programas|
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
|set title| titulo en la ventana de la terminal|
|set linebreak|no corta palabras|
|set noswapfile| parece que no crea los archivos wap|

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
" Seteo basico "
set number
set mouse=a
set numberwidth=1
set clipboard+=unnamedplus
syntax enable
set showcmd
set ruler
set encoding=utf-8
set showmatch
set sw=2
set relativenumber
set laststatus=2
set linebreak
set title
set noswapfile


" bloque de plugins a instalar "
call plug#begin('~/.vim/plugged')


" para moverce mas rapido en el código "
Plug 'easymotion/vim-easymotion' 

" Menu para crear mover eliminar archivos "
Plug 'scrooloose/nerdtree'

" Navegación entre ventanas abiertas CTRL h/l "
Plug 'christoomey/vim-tmux-navigator'

" emmet "
Plug 'mattn/emmet-vim'

" autocompletado de palabras "
Plug 'neoclide/coc.nvim'

" Multiple seleccion ctrl n"
Plug 'mg979/vim-visual-multi', {'branch': 'master'}

" Theme "
Plug 'morhetz/gruvbox'


call plug#end()


" aplicar el theme
colorscheme gruvbox
let g:gruvbox_contrast_dark = "hard"

" tecla lider 
let mapleader=" " 

" automaticamente cierra NerdTree
let NERDTreeQuitOnOpen=1

" s para easymotion buscador
nmap <leader>s <Plug>(easymotion-s2) 
" nt para nerdTree con m abre el menu
nmap <leader>nt :NERDTreeFind<CR>
nmap <leader>w :w<CR>
nmap <leader>q :q<CR>

" Invertir las teclas de subir y bajar"
noremap k j
noremap j k



" Comandos Nvim "
inoremap ( ()<Esc>i
inoremap { {<CR><CR>}<Esc>ki  
inoremap [ []<Esc>i
inoremap < <><Esc>i
inoremap ' ''<Esc>i
inoremap " ""<Esc>i
inoremap $<CR> `${}`<Esc>2ha
inoremap ppp<CR> print()<Esc>i
inoremap ppl<CR> console.log();<Esc>hi
inoremap cl<CR> class="" <Esc>2ha
inoremap id<CR> id="" <Esc>2ha
inoremap href href=""<Esc>i
inoremap type<CR> type=""<Esc>i
inoremap name<CR> name=""<Esc>i



" Comandos para Javascript "
inoremap use<CR> 'use strict'<CR><CR>window.addEventListener('load', () => {<CR><CR>});<CR><CR><CR><CR><CR><CR><CR><CR><Esc>9ki
inoremap ~<CR> const  = () => {<CR><CR>}<Esc>0kk6li
inoremap => () => {<CR><CR>}<Esc>ka  

" for while if "
inoremap for<CR> for(let=i;i< .length;i++){}<Esc>012la
inoremap wl<CR> while(){}<Esc>3ha
inoremap if<CR> if(){}<Esc>3ha
inoremap else<CR> else{}<Esc>i

" addEventListener "
inoremap ad<CR> addEventListener('click', () => {<CR><CR>});<Esc>ka  
inoremap do<CR> document.querySelector('');<Esc>3ha
inoremap di<CR> document.getElementById('');<Esc>3ha

inoremap js<CR> let js="textContent createElement value appendChild append innerHTML style className getElementsByClassName getElementsByTagName querySelectorAll querySelector document.write backgroundColor padding textAlign border color fontSize textTransform createTextNode window location open url href innerHeight innerWidth screen height width click blur change focus mouseover mouseout onclick keydown keypress keyup String.fromCharCode(event.keyCode) setInterval setTimeout clearInterval"<CR><Esc>




" Comandos para CSS "
inoremap med<CR> @media screen and (min-width 768px){<CR><CR>}<Esc>ki

inoremap css<CR> *,*::before,*::after{box-sizing:border-box;margin:0;padding:0;font-family:'arial';}<CR>a{text-decoration:none;}<CR>li{list-style:none;}<CR>ul{display:flex;}<CR><Esc>

inoremap .css<CR> .css[type="submit"]{background:dodgerblue;color:gold;width:100vh;height:100vw;text-align:right left;font-size:16px;display:block flex grid;position:relative absolute fixed;margin:auto;cursor:pointer;vertical-align: top super bottom sub middle baseline;border-radius:50%;grid-template-columns:repeat(1, 1fr);grid-template-rows: minmax(2em, auto);grid-gap:.5em 1em;grid-column-start:1;grid-column-end:1;grid-row-start:1;grid-row-end:1;align-content:space-evenly;align-self:end;align-items:center;justify-content: space-around space-between;justify-self: stretch;justify-items: start;justify-content:end;justify-self:start;order:1;flex-direction:row-reverse;flex-wrap:wrap row nowrap;align-items:flex-start flex-end;}<CR><Esc>



" Comandos para HTML"
inoremap html<CR> <html></html><Esc>6hi
inoremap head<CR> <head></head><Esc>6hi
inoremap body<CR> <body></body><Esc>6hi

inoremap st<CR> <style></style><Esc>7hi
inoremap lk<CR> <link rel="stylesheet" href=""><Esc>hi
inoremap sc<CR> <script type="module"  src=".js"></script><Esc>13hi

inoremap header<CR> <header id="" class="header" ></header><Esc>2ba
inoremap nav<CR> <nav id="nav" class="nav"><CR><ul id="ul" class="ul" ></ul><CR></nav><Esc>5ba
inoremap ul<CR> <ul id="ul" class="ul" ></ul><Esc>4hi
inoremap a<CR> <a class="a" href=""></a><Esc>3hi
inoremap li<CR> <li class="li" ></li><Esc>4hi

inoremap div<CR> <div id="" class="" ></div><Esc>5hi
inoremap img<CR> <img id="" class="" src="" alt=""/><Esc>3b2li
inoremap art<CR> <article id="" class="article"></article><Esc>bblli
inoremap sec<CR> <section id="" class="article"></section><Esc>bblli
inoremap foo<CR> <footer id="footer" class="footer"></footer><Esc>8hi

inoremap p<CR> <p class="" ></p><Esc>3hi
inoremap h1<CR> <h1 class="h1" ></h1><Esc>4hi
inoremap h2<CR> <h2 class="h2" ></h2><Esc>4hi
inoremap h3<CR> <h3 class="h3" ></h3><Esc>4hi
inoremap h4<CR> <h4 class="h4" ></h4><Esc>4hi
inoremap h5<CR> <h5 class="h5" ></h5><Esc>4hi
inoremap h6<CR> <h6 class="h6" ></h6><Esc>4hi

inoremap fm<CR> <form id="" class="" action="" method=""><CR><CR></form><Esc>ki
inoremap lbl<CR> <label for=""><label><Esc>8hi
inoremap btn<CR> <button></button><Esc>2bli
inoremap pp<CR> <input  <CR>id=""<CR>class=""<CR>type="text"<CR>name=""<CR>placeholder=""<CR>>
inoremap pps<CR> <input type="submit" value="enviar"/><Esc>

inoremap ñññ<CR> <!DOCTYPE html><CR><html lang="es"><CR><head><CR><meta charset="UTF-8"/><CR><meta http-equiv="X-UA-Compatible" content="IE=edge"/><CR><meta name="viewport" content="width=device-width, initial-scale=1.0"/><CR><title>pagina en construccion</title><CR></head><CR><body><CR><header id="" class="header" ></header><CR><section id="" class="section"></section><CR><footer id="footer" class="footer"></footer><CR></body><CR></html><CR><Esc>

~~~
