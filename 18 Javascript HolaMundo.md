# FILTER
lo que hace este metodo es buscar dentro de un array de elementos u objetos algun dato en especifico  
~~~
const numeros = [1,2,3,4,5,6,7,8,9]
const mascotas = [
	{nombre: 'Puchini', edad: 12, tipo: 'perro'},
	{nombre: 'Chanchito', edad: 3, tipo: 'perro'},
	{nombre: 'Pulga', edad: 10, tipo: 'perro'},
	{nombre: 'Pelusa', edad: 16, tipo: 'gato'}
];
console.log(numeros)
console.log(mascotas)

const suma = (ns) => {
	let acumulado = 0;
	for(i = 0; i < ns.length; i++){
		acumulado += ns[i];
	}
	return acumulado
}
~~~
Esto nos devuelve un ***nuevo array*** con los elementos encontrados, si la condicion es true
~~~
const numerosFilter = numeros.filter(x => x < 5)
console.log(numerosFilter)
~~~
nos devuelve un ***nuevo array*** con los objetos encontrados que queriamos buscar
~~~
const perros = mascotas.filter(x => x.tipo == 'perro')
const gatos = mascotas.filter(x => x.tipo == 'gato' )
const mayores = mascotas.filter(x => x.edad >= 11)
console.log(perros)
console.log(gatos)
console.log(mayores)
~~~

# MAP
.map recibe un arrow function devolviendonos un nuevo array de objetos de igual   longitud, almacenando los resultados en una nueva variable  
~~~
const multiplicados = numeros.map(x => x * 2)
console.log(multiplicados)
~~~
Crear array de parejas de numeros  
~~~
const parejas = numeros.map(x => [x, x])
console.log(parejas)
~~~
Obtener la edad promedio de todas las mascotas
~~~
const edades =  mascotas.map(x => x.edad)
const resultado = suma(edades)
console.log(edades)
console.log(resultado / edades.length)
~~~

# REDUCE
.reduce recibe un arrow function con 2 parametros que son: el ***acumulado inicial***
y el ***primer elemento del array***, seguido el accumulado inicial se lo pasamos 
despues de la operacion a realizar  
~~~
const numeros = [5,2,4,8,5]
const resultado = numeros.reduce((acc, el) => acc * el, 7)
console.log(resultado)

const reducido = [12].reduce((acc, el) => acc + el, 9)
console.log(reducido)
~~~
***Buscar algo en un array***  
~~~
const mascotas = [
	{nombre: 'Puchini', edad: 12, tipo: 'perro'},
	{nombre: 'Chanchito', edad: 3, tipo: 'perro'},
	{nombre: 'Pulga', edad: 10, tipo: 'perro'},
	{nombre: 'Pelusa', edad: 16, tipo: 'gato'}
];

const indexed = mascotas.reduce((acc, el) => ({
	...acc, [el.nombre]: el,
}), {})

console.log(indexed['Pelusa']);
~~~

> {nombre: 'Pelusa', edad: 16, tipo: 'gato'}  

***Array Plano***  
~~~
const anidado = [1, [2,3], 4,[5]]
const plano = anidado.reduce((acc, el) => acc.concat(el), [] );
console.log(plano)
~~~

>	[1, 2, 3, 4, 5]

# ARROW FUNCTIONS
fat arrow functions, son funciones que se pueden almacenar como valores   
en una variable, con return implicito en una sola línea.  
con uso de corchetes si se van a ejecutar mas operaciones en su interior.   

***function***  
~~~
function suma(a,b) {
	return a + b
}
const resultado = suma(1,5)
console.log(resultado) // 6
~~~

***fat arrow function***  
~~~
const sumar = (a, b) => a + b
const resultados = sumar(1 , 5)
console.log(resultados)
~~~

# Closures
programacion funcional  
son la combinacion de una funcion, y el alcance lexico que tiene un closures  
se crea por fuera de la funcion.

~~~
const x = 'Fluffy'

const f = () => {
	const y = 'Kins'
	console.log(x , y)
}
f()
~~~
> Fluffy kins

Una funcion puede acceder a las constantes que esten definidas dentro de la   
funcion y a variables que este definidas fuera de la funcion, esto se conoce  
como closure.  

en que favorece?  
ya que con los closure podemos realizar composicion, ya sea de objetos o  
tambien de funciones, ya ir modificando el comportamiento.  

# Recursividad
es una funcion que se llama una y otra ves hasta que se cumple una condicion de salida.  
~~~
const conteoRegresivo = (a) => {
	if (a < 0) return 
	console.log(a)
	return conteoRegresivo(a - 1)
}

conteoRegresivo(10)
~~~
recursividad es una funcion que se llama asi misma, hasta  
que cumple cierta condicion, cuando se halla cumplido esa  
condicion, la funcion dejara de llamarse así misma, esto  
funciona muy bien en remplazo de los loops, for, while, etc.  

# Spread Operator
Crea una copia del objeto y sus propiedades, creando nuevos  
objetos, copiando sus propiedades y es completamente reutilizables.  

~~~
const gato = {
	nombre: 'felix tomas',
	edad: 7
}

const gata = { ...gato }

gata.nombre = 'lala'
gata.edad = 8

const michu = { ...gato }

michu.nombre = 'michin'
michu.edad = 5


const gatos = [gato, gata, michu]
console.log(gatos)
~~~
***Resultados***  
~~~
[ 
  { nombre: 'felix tomas', edad: 7 },  
  { nombre: 'lala', edad: 8 },  
  { nombre: 'michin', edad: 5 } 
]
~~~  









