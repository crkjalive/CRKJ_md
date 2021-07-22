# CSS GRID 
1. grilla de css
~~~
.contenedor 
	.div	
	.div
~~~
2. display: grid; ***crea grilla***
3. grid-template-columns: 50% 50%; ***ancho de columnas***
4. grid-template-rows: 200px 400px; ***alto de la fila***
5. grid-auto-rows: 200px; ***aplica alto a todas las filas***
6. grid-auto-columns: 200px; ***aplica ancho a todas las filas***

### valores que recibe
1. px
2. %
3. auto
4. em
5. fr

### fracciones
1. 1fr 1fr 1fr 1fr ***divide pantalla entre 4***
2. repeat(4, 1fr); ***simplifica***

### espaciados entre
1. gap: 1em; ***espaciado entre filas y columnas***
2. column-gap: 1em; ***espaciado entre columas***
3. row-gap: 1em; ***espaciado entre filas***

### valores minimos y maximos de las filas o columnas
1. grid-template-rows: minmax(100px, auto);
___

### aliniaciones horizontales de todos los elementos
1. justify-content: start;
2. justify-content: center;
3. justify-content: end;

### aliniaciones verticales de todos los elementos
1. align-items: start;
2. align-items: center;
3. align-items: end;

### aliniaciones horizontales del elemento
1. justify-self: start;
2. justify-self: center;
3. justify-self: end;

### aliniaciones verticales del elemento
1. align-self: start;
2. align-self: center;
3. align-self: end;
___

# anchar elemento mas espacios
Se le debe aplicar a la clase del elemento
1. grid-column: 1/4 ***ancho de la linea 1 hasta la 4***
2. grid-row: 1/3 ***alto del elemento desde la linea 1 hasta la 3***

