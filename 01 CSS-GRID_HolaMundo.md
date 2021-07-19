# CSS Grid by Hola Mundo 
1. La grilla es un sistema que se implementa en CSS3 para distribucion homogenea de los elementos, dentro de un area o en la página completa
2. esta grilla es formada por seldas, que permiten distribuir el contenido, entre columnas y filas con instrucciones de ancho y alto definidos por el desarrollador

***CSS que se aplica***

|elemento |propiedad |valor |
|-|-|-|
|.contenedor | display: grid; | vuelve el contendor en una grilla |
|.elemento | | se le aplican los estilos|	

### Ejemplo básico

***html***
~~~
<div class="contenedor">
	<div class="elemento">A</div>
	<div class="elemento">B</div>
	<div class="elemento">C</div>
</div>
~~~

***CSS***
~~~
.contenedor{
	display: grid;
}
.element {
	background-color: red;
}
~~~

### Columnas y Filas

|elemento |propiedad |valor |
|-|-|-|
|.contenedor | grid-template-rows: | se le da el ancho a las filas |
|.contenedor | grid-template-columns: | se le da el ancho a las columnas |

~~~
.grid{
	grid-template-rows: 50px 100px;
	grid-template-columns: 50px 100px;
}
~~~
1. el primer valor, hace referencia a la primera fila o columna.
2. el segundo valor, hace referencia a la segunda fila o columna.
3. estos valores son fijos

### Metodo en fracciones
1. toma y divide el total del contenedor en fracciones 
~~~
.grid{
	grid-template-columns: 1fr 2fr 3fr; // 6 fracciones en total
}
~~~

| medidas | propiedad |
|-|-|-|
| % | porcentaje|
| rem em | relacion a la fuente |
| px | pixeles |
| fr | fracciones |

~~~
.grid{
	grid-template-columns: 2rem 20% 2fr 1fr;
}
~~~

### Tamaños minimos y maximos de la columna o fila con la funcion minmax()
con la funcion minmax podemos setiar el valor minimo, y un valor maximo 
~~~
.grid{
	grid-template-rows: minmax(100px, auto);
	grid-template-columns: minmax(auto, 50%);
}
~~~

### Repetir dimensiones 
~~~
.grid{
	grid-template-rows: repeat(4, 50px);
	grid-template-columns: 50px repeat(3, 1fr) 20%;
}
~~~

### Brechas entre elementos
espacio entre los elementos
~~~
grid-row-gap: 20px;
grid-column-gap: 10px;
~~~

alternativa simplificada
~~~
grid-gap: 20px 10px;
~~~

### Expandir elementos en la grilla
se le aplica a el elemento y no al contenedor

1. grid-column-start
2. grid-column-end
3. grid-row-start
4. grid-row-end

tomara desde la columna 1 hasta la ultima columna,  
expandiendo el elemento en todo el ancho de su contenedor o la pantalla.
~~~
.header {
	grid-column-start: 1;
	grid-column-end: 1;
}
~~~

***alternativa simplificada***  
tomara la cantidad de lineas que se le pasen
~~~
.element {
	grid-column: 1 / 6;
	grid-row: 1 / 3;
}
~~~

# Asignando nombres a las lineas de la grilla
De esta manera podemos definir el ancho y el alto de nuestra filas y columnas
~~~
.grid {
	grid-template-rows: [row-1-inicio] 50px [row-2-inicio] 50px [row-3-fin];
	grid-template-columns: [col-1-inicio] 1fr [col-2-inicio] 1fr [col-3-inicio] 1fr [col-4-fin];
}

.header {
	grid-column: col-1-inicio / col-4-end;
	grid-row: row-1-inicio / row-4-end;
}
~~~

### Usando repeat para lineas predecibles 
Excelente forma de posicionar elementos dentro de la grilla, nombrando cada linea de la grilla.
~~~
.grid {
	grid-template-rows: repeat(2, [row-inicio] 50px [row-fin]);
	grid-template-columns: repeat(3, [col-1-inicio] 1fr [col-2-end]);
}

.header {
	grid-column: col-inicio / col-end 3;
	grid-row: row-inicio / row-end 3;
}
~~~
___
revisar el tema de grillas
___

# Areas de grillas 
De esta forma lo que hace es dividir por areas el contenedor de la página
~~~
grid-template-areas:"header header"
					"content sidebar"
					"footer footer";

grid-template-rows: 150px 1fr 100px;
grid-template-columns: 1fr 200px;
~~~
Así se declarar grillas de forma explicita,  
donde definimos que queremos que tenga un comportamiento determinado

### Grillas
implicitas: es el comportamiento que no se allan definido, lo que seguira apareciendo despues de lo definido.
~~~
grid-auto-rows:
grid-auto-flow: row | column
~~~
de esta manera seguira el flujo de los elementos en filas o columnas
___
propiedades de alineacion
___


### Alinear y distribuir contenido 
justify-content
1. justify-items:center;
2. justify-items:start;
3. justify-items:end;
4. justify-items:stretch;

align-items
1. align-items: start;
2. align-items: center;
3. align-items: stretch;
4. align-items: end;

alineacion horizontal con justify-self, en el elemento
1. justify-self: start;
2. justify-self: center;
3. justify-self: end;
4. justify-self: stretch;

alineacion vertical con justify-self, en el elemento
1. align-self: center;
2. align-self: start;
3. align-self: end;
4. align-self: end;

alineacion en el centro
1. align-self: center;
2. justify-self: center;

### Alineando grilla completa
En la grilla
1. justify-content: start;
2. justify-content: end;
3. justify-content: center;
4. justify-content: space-around;
5. justify-content: space-between;
6. justify-content: space-evenly;

verticalmente
1. align-content: start;
2. align-content: end;
3. align-content: center;
4. align-content: space-around;
5. align-content: space-between;
6. align-content: space-evenly;







