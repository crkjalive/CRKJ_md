# Javascript Arrays
los arrays (arreglos) o matrices son una estructura que me permite almacenar  
datos de diferente tipo, que se accede a los datos por la posicion de los  
indices  
1. const arr2 = new Array(10) ***instancia, length fijo a 10***
2. const arr = [] ***array en corchetes***
~~~
const arr = ["chanchito", "Python", "true", "23", {name:'crkj'}]
console.log(arr[0])
console.log(arr[1])
console.log(arr[4].name)
~~~
> 'crkj'

# Iteración en Array

***for***  
~~~
for (let i = 0; i < arr.length; i++) {
  console.log(arr[i])
}
~~~

***forEach***   
1. element ***elemento a mostrar por cada iteracion***
2. index ***indice del recorrido***
3. data ***array original***
~~~
arr.forEach((element, index, data) => {
  console.log(`Indice: ${index} elemento: ${element}, holaMundo ${data}`)
})
~~~

***for in***  
~~~
const peliculas = new Array('Batman','Superman','Spiderman')
for (let hero in peliculas) {
  console.log(peliculas[hero])
}
~~~

***Array Multidimencional***  
arrays dentro de otro array  
~~~
const front = new Array('js', 'html', 'css')
const back = new Array('python', 'node', 'sql')
const fullStack = new Array(front, back)
console.log(fullStack[0][0])
console.log(fullStack[0][1])
console.log(fullStack[0][2])
console.log(fullStack[1][0])
console.log(fullStack[1][1])
console.log(fullStack[1][2])
~~~

***Operaciones***  
1. arr.push('hola') ***agrega al final***
2. arr.unshift('mundo') ***agrega al inicio***
3. arr.pop() ***elimina el ultimo***
4. arr.shift() ***elimina el primero***
5. arr.indexOf('element') ***busca elemento en array y devuelve la posicion***
6. arr.splice(indice,1) ***verifica el indice y borra 1 elemento***
7. arr.join(',') ***array a string entre comas***
8. arr.sort() ***ordena***
9. arr.reverse() ***invierte los elementos del array***
10. arr.split(',') ***string a array, separados donde encuentre la coma***

## Busquedas

***find***  
find recibe un callback que retorna el valor  
~~~
const heroes = new Array('Spiderman','Batman','Superman');
let buscar = heroes.find(heroe => heroe == "Batman")
console.log(buscar)
~~~

***findIndex***  
devuelve el indice
~~~
let buscarIndex = heroes.findIndex(heroe => heroe == "Batman")
console.log(buscarIndex)
~~~

***some***  
compara valores, devuelve true o false  
~~~
const numeros = new Array(10, 20, 30, 40, 50, 80);
let numeroMayor = numeros.some(mayor => mayor > 40)
console.log(numeroMayor)
~~~












