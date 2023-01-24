# Javascript function and methods
las funciones son un bloque de código reutilizable, que recibe  
métodos para variar sus valores internos  
~~~
function saludar () {
  return 'Hola Mundo'
}
~~~
***Parámetros***  
Fat Arrow Functions  
funciones anónimas contenidas en una variable  
~~~
const saludar = (name) => {
  return `Hola ${name}`
}
saludar('CRKJ')
~~~
***ejemplo calculadora***  
parámetro ***flag***, ya viene por defecto para hacer algo de más  
~~~
const calcular = (num1, num2, soloMultiplicar = false) => {
	const sumar = num1 + num2;
	const restar = num1 - num2;
	const multiplicar = num1 * num2;
	const dividir = num1 / num2;
  if(soloMultiplicar == true){
    console.log(`La tabla del ${num2} es: ${num2} * ${num1} es: `, multiplicar)
  } else {
  	console.log(sumar);
  	console.log(restar);
  	console.log(multiplicar);
  	console.log(dividir);
  }
}
calcular(3, 6);
calcular(15, 9);
calcular(5, 2);

for (let i = 1; i <= 10; i++) {
  calcular(i, 6, true)
}
~~~
***Parámetros REST y SPREAD OPERATOR***  
puede capturar más parámetros, detipo object {}
~~~
const frutas = (...demasFrutas) => {
  console.log(...demasFrutas[5])
  console.log("de tipo: "+typeof(demasFrutas))
}
frutas('Coco', 'Naranja', 'Manzana', 'Kiwi', 'Melon', 'Banano', 'Fresa', 'Sandia', 'Pera')
~~~
***Callbacks***  
funciones anonimas que se ejecutan dentro de otras funciones  
cuando termina de ejecutarse vuelve a la funcion contenedora y continua retornando su valor  
~~~
const saludaPrimero = (name) => {
  const names = name.toUpperCase()
  return `Hola ${names}`
}
const sumar = (num1, num2, name) => {
  let hola = saludaPrimero(name)
  const dato = num1 + num2
  return (`${hola} tu dato es: ${dato}`)
}

const fullText = sumar(5, 26,'Wizard')
console.log(fullText)
~~~


