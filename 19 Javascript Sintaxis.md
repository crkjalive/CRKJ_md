# Javascript Languaje
Sintaxis básico de javascript

## Hola Mundo
1. alert('Hola Mundo'); ***ventana de alerta flotante en html***
2. confirm(); ***ventana de confirmacion en html***
~~~
let mi_resultado = confirm("Estas seguro de querer continuar?");
console.log(mi_resultado);
~~~
3. document.write('Hola Mundo'); ***escribir sobre el documento***
4. prompt("Dame tu nombre: "); ***captura de datos STRING por ventana***
~~~
prompt("pregunta: ", default);
let mi_resultado = prompt("Que edad tienes? ",18);
console.log(mi_resultado);
~~~

## Mostrar por consola
1. console.log('Hola Mundo'); ***imprime string***
1. console.log(variables); ***imprime variables*** 
1. console.log(2+2); ***imprime operaciones directamente*** 

## Comentarios
1. /* code... */ ***block code..***
2. // code... ***line code..***

### Back ticks 
comillas invertidas ***`${var}`*** para insertar variables en cadenas de texo  
~~~
const name = 'CRKJ'
console.log(`Hola ${name}`)
~~~

## Modo estricto de Javascript 
impide que yo asigne variables sin haberlas declarado
1. 'use strict'

## Variables
una variable es un contenedor de información  
tener en cuenta su scope global o scope de bloque  

|Variable|declaracion|valor|
|-|-|-|
|contante|const|const nombre = "Jared";|
|variable local|let|let primerNombre = "Kenneth";|
|variable global|var|var apellidos = "Latorre Ramos";| 

***Variable global***  
varia su valor en toda la ejecución del script  
~~~
var pais = 'Colombia'
pais = 'Argentina'
pais = 'Venezuela'
continente = 'America'
document.write(pais+' '+continente)
~~~

***Variable con alcance a nivel scope de bloque***  
variable que su valor no puede cambiar fuera de su scope de ejecución  
~~~
let lenguaje = "javascript";
console.log(lenguaje)
if(true){
	let lenguaje = "python";
	console.log(lenguaje);
}
console.log(lenguaje)
~~~
> javascript  
> python  
> javascript  

***Constante, su valor siempre es el mismo inalterable***  
para declarar valores constantes que no varian  
~~~
const web = "http://www.google.com"
const PI = 3.14159265
~~~

## Operadores y tipos de datos 
|no.| operadores | tipo de operador |
|-|-|-|
|1.| ```+ - * / %``` | operadores matematicos |
|2.| ```<> <= >= == != === = !``` | comparacion | 
|3.| ```and && y or ll``` | operador condicional |
|4.| ```true false``` | validadores |
|5.| ```string, int, bool, float``` | tipos de datos en Js |
|6.| ```++ -- += -= **``` | incrementos y decrementos |

## Funciones del lenguaje
se deben almacenar en una variable para ver el resultado  

1. Number() ***combierte un string númerico a número***
2. parseInt(var) ***transforma a entero***
3. parseFloat(var) ***transforma a flotante***
4. typeof(var) ***saber que tipo de dato es***
5. numero.toString() ***cambiar a string***
6. texto.toUpperCase() ***a mayusculas***
7. texto.toLowerCase() ***a minusculas***
8. .length ***longitud***
9. texto1.concat(texto2) ***concatena variables***
10. textoContenedor.indexOf('BuscarCadena') ***busca posicion***
11. textoContenedor.search('BuscarPalabra') ***busca palabra***
12. textoContenedor.match('BuscarPalabra') ***devuelve un array con el resultado***
13. texto.substr(14, 8) ***cadena desde el caracter 14, 8 letras***
14. texto.charAt(24) ***sacar 1 caracter***
15. texto.startsWith('Bienveni') ***verifica sí empieza con***
16. texto.endsWith('cript') ***verifica sí termina con***
17. texto.includes('al curso') ***si contiene retorna true o false***

# Funciones de busqueda en strings
1. texto.slice(15) ***corta en cadena desde el caracter 15***
2. texto.slice(15,30) ***corta en cadena desde el caracter 15 al 30***
3. texto.split(" ") ***divide cadena de texto, en array por palabras***
4. texto.trim() ***quita espacios de inicio y final***

# Estructuras de control
1. debugger ***detiene el ciclo para saber que esta pasando***
2. break ***cortamos la ejecucion del bucle y salimos***  

## if 
Condicional if: evaluar si es verdadero o falso el dato  
validar si existe errores  
~~~
if (true) { // code... } 
else if (true) { // code... }
else { // Code... }
~~~
***ejemplo***  
~~~
let edad = 18;
if (edad >= 18) { document.write("eres mayor de edad")
} else if (edad <= 10 ) { document.write("eres un niño")
} else { document.write("eres menor de edad") }
~~~

## switch case
valida si existe un posible caso
~~~
let edad = 21;
let imprime = '';

switch (edad) {
	case 21:
		imprime = 'eres mayor de edad';
	break;
	case 18:
		imprime = 'eres menor de edad en EU';
	break;
	case 30:
		imprime = 'crisis de los 30';
	break;
	default:
		imprime = 'edad por default';
	break;
}
console.log(imprime);
~~~

## for
ciclo for: itera varias veces una estructuta de datos, mientras la condicion  
sea true, al ser false detendra su ejecución
~~~
let numeroCien = 100;
for (let i = 0; i < numeroCien; i++) {
	console.log("print the number: ", (i+1));
}
~~~

## while (mientras)
ciclo mientras, valida si la condicion es true ejecutandose cada vez, al ser false  
detendra su ejecución.
~~~
let year = 2020;
while (year <= 2051) {
	console.log('what year is it: ', year);
	year++;
}
~~~

## do while (mientras hacer)
se ejecuta al menos 1 ves antes de validar
~~~
let years = 15; 

do {
	document.write('se va a ejecutar asi no se haya validado la condicion <br/>')
	years++;
} while (years != 20)
~~~