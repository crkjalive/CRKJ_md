# Flexbox
1. Diseñado y pensado en 2 dimensiones X y Y 
2. se basa en un contenedor con items

~~~
.flex {
	display:flex;
	flex-direction: column;
}
~~~

### Flex direction

1. flex-direction: row;
2. flex-direction: row-reverse;
3. flex-direction: column;
4. flex-direction: column-reverse;
5. flex-wrap: nowrap;
6. flex-wrap: wrap;
7. flex-flow: row wrap;
8. flex-flow: row nowrap;

### Justificar contenido horizontal
1. justify-content: flex-start;
2. justify-content: flex-end;
3. justify-content: center;
4. justify-content: space-around;
5. justify-content: space-between;
6. justify-content: space-evenly;

### Alinear contenido vertical
1. align-items: flex-start;
2. align-items: flex-end;
3. align-items: center;
3. align-items: stretch;
4. align-items: space-around;
5. align-items: space-between;
6. align-items: space-evenly;

### Alinear en el contenedor 
1. align-content: flex-start;
2. align-content: flex-end;
3. align-content: center;
4. align-content: space-around;
5. align-content: space-between;
6. align-content: space-evenly;

### Manipular orden de los elementos
order: se ordena cada item dentro de su contenedor, en la posicion que se desee.
1. order: 1;

### Como hacer que los elementos usen mas espacio
default es 0, asi que creceran los elementos de manera proporcional
1. flex-grow: 0; 
2. flex-grow: 2; 
3. flex-grow: 1; 
 
### Distribuir a lo largo el contenedor
1. flex-grow:2
2. flex basis: 120px
3. flex: 1 120px ***forma simplificada***

### align-self
permite alinear respecto al eje que estamos utilizando
1. align-self: auto;
2. align-self: flex-start;
3. align-self: flex-end;
4. align-self: center;
5. align-self: baseline;
6. align-self: stretch;

### Elemento sin efecto dentro de flex 
float, clear, vertical-align 

### Juego de flexbox
https://flexboxfroggy.com/