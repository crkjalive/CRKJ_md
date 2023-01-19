# VIM
Comandos de navegacion

| comando | Ayuda |
|-|-|
| :help | ayuda |
| :Tutor | tutorial vim |
| :help | init |

### Ruta para configurar nvim
>home/khriz/.config/nvim/init.vim

### Ayuda para cualquier comando
>:help w

### Crear un archivo
>nvim FILENAME ***crea un nuevo archivo***

### Salir y Guardar
| comando | accion |
|-|-|
| Esc Esc | salir del modo |
| :q | salir |
| :q!| salir sin guardar cambios |
| :w | guardar |
| :wq | guardar y salir |

### Modos en VIM
| Tecla | Modo | Permite |
|-|-|-|
| v | modo visual | cortar, pegar, insertar, avanzar |
| i | modo insertar | editar, escribir |
| b | modo bloque | seleccionar bloques de codigo |
| x | elimina hacia la derecha | el Suprimir de NVIM |

### Mover por teclado
| Tecla | Accion |
|-|-|
| h | left |
| j | down |
| k | up |
| l | right |

### Avanzar por palabras
| Tecla | Accion |
|-|-|
| w | avanzar al inicio de la siguiente palabra |  
| e | avanzar al final  de la siguiente palabra |
| b | atras al inicio de la palabra anterior |

### Editar texto
| comando | accion |
|-|-|
| u | undo deshacer == ctrl z |
| ctrl r | rehacer == ctrl y |
| dw | elimina desde el cursor hacia adelante |
| db | elimina desde el cursor hacia atras |
| de | elimina la palabra siguiente |
| dd | corta o elimina linea completa |
| d$ | elimina desde el cursor hasta el final |
| d | d + movimiento arriba o abajo, elimina |
| d5 movUp | elimina por arriba |
| d5 movDown | elimina por abajo |

### Eliminando mas rapido
| comando | accion |
|-|-|
| d2b | elimina 2 palabras hacia atras por el inicio de la palabra |
| d5e | elimina 5 palabras hacia adelante por el final de la palabra |
| d6w | elimina 6 palabras hacia adelante por el inicio de la palabra |

### Moviendonos rapidamente
| comando | accion |
|-|-|
| 40 + + | mover a la linea 40 o a la que uno quiera |
| 40 + - | mover a la linea 40 o a la que uno quiera |
| gg | inicio del documento |
| shift + g | al final del documento |
| 0 | muevo al inicio de la linea |
| $ | muevo al final de la linea |
| 1-9 | salta cantidad en palabras |
| 2w o 2b | numero + w se mueve n cantidad de palabras |

### Eliminando varias lineas de código
| comando | accion |
|-|-|
| 5dd | elimina cantidad de lineas por debajo del cursor |

### Comando undo o deshacer
| comando | accion |
|-|-|
| u | devuelve los cambios |
| U | devuelve todos los cambios de la linea |

### Pegar, remplazar, eliminar
| comando | accion | importante |
|-|-|
| O | insertar por encima del cursor | shift + o |
| o | insertar por debajo del cursor |
| p | pegar por debajo del cursor en la linea |
| P | pegar por encima del cursor en la linea | shift + p |
| r | remplazar la letra |
| R | empieza a remplazar |
| ce | reemplazar desde el cursor hasta el final de la palabra |
| c2 mov | elimina linea por arriba o abajo |
| ctrl g | muestra total de linea, y nombre del archivo |

### Insertar
| comando|accion|
|-|-|
| a | insertar texto despues del cursor |
| A | insertar al final de la linea |
| i | insertar detras del caracter |
| R | reemplaza mientras escribes |

### Copiar y pegar
|comando | accion |
|-|-|
| y | copia linea |
| yw | copia letra |
| p | pega linea copiada |
| shift + p | pegar por arriba de la linea |
| cw | quita palabra desde el cursor |
| ciw | elimina toda la palabra|muy util |

### Seleccionar todas la misma palabra
| comando | accion |
|-|-|
| gd | selecciona todas las palabras iguales |
| gf | lleva al archivo |

### Comandos buscar y remplazar
| comando | accion | importante |
|-|-|
| : | comando |
| / | buscar palabra + enter | hacia adelante |
| ? | buscar por debajo + enter | hacia atras |
| n | avanza en la busqueda |
| N | retrocede en la busqueda |
| shift + % | () [] {} me mueve al inicio/final del cierre |

### Buscar y Remplazar
| Comando | Accion ||
|-|-|-|
| :s/palabra | quita en la linea la palabra que se busca |
| :%s/old/new | :%s/palabraVieja/palabraNueva/global | reemplazar palabras % |
| :%s/old/new/g | reemplazar todas palabras |
| :%s/mail/email/gc| preguntando los reemplazos |












