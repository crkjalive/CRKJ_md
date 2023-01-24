# Javascript DOM, BOM, Events, localStorage

***Manipulacion de DOM***   
1. document. ***acceder al documento html***
2. .getElementById('principal') ***seleccion elemento por id***
3. .getElementsByClassName('titulo') ***seleccion por clase en array***
4. .getElementsByTagName('div') ***DEVUELVE elementos HTML en array***
5. .getElementsByName('') ***selecciona elemento por su nombre***
6. .querySelector('') ***me trae el primer elemento que encuentre***
7. .querySelectorAll('') ***devuelve un NodeList o array con todos los elementos***
8. .innerHTML ***accedo al contenido del elemento HTML***
9. .style.propiedadCSS ***damos estilos css al elemento***
10. .className ***damos clase al elemento desde js***

~~~
const h1 = document.getElementById('h1').innerHTML
console.log(h1)
h1.innerHTML = 'Nuevo contenido'
console.log(h1)
h1.style.backgroundColor = 'red'
const divs = document.getElementByTagName('div')
const div3 = divs[2]
~~~

***Manipulacion de BOM***
1. window ***referencia al navegador***
2. window.innerHeight ***alto de la ventana en px***
3. window.innerWidth ***ancho de la ventana en px***
4. screen.height  ***alto de la pantalla en px***
5. screen.width ***ancho de la pantalla en px***
6. window.location ***me muestra la url actual o asigna '/'***
7. window.location.href = url ***abre un nueva url***
8. window.open(url) ***abre nueva pestaña con la nueva url***
9. window.open(url,"", "width=600, height=300") ***abre nueva ventana***

~~~
const url = 'https://google.com'
window.open(url, "", "width=600, height=300")
console.log(window.location)
~~~

# Eventos del navegador
los eventos son funciones que se ejecutan en interaccion con el usuario  
click en elementos, movimiento del mouse, escritura en input, redimensión de las ventanas  

1. onclick ***click sobre un elemento***
2. ondbclick ***doble click en el elemento***
3. onchange ***si elemento cambia***
4. onsubmit='return false' ***bloquea el envio del formulario***

~~~
<button onclick="cambiarColor()"> Presioname </button>
~~~

# addEventListener 
encapsular los eventos en funciones  

1. addEventListener('click'. () => {}) ***Sintaxis***
2. onclick ***click sobre elementos***
3. mouseover ***mouse sobre elemento***
4. mouseout ***mouse fuera del elemento***
5. submit ***evento para formularios***
6. focus ***dentro del input***
7. blur ***salgo del input***
8. keydown ***al presionar una tecla***
9. keyup ***suelto tecla***
10. keypress ***tecla presionada***
11. String.fromCharCode(event.keyCode) ***me muestra que tecla se oprimio***

~~~
const cambiarColor = () => {
	let bg = h1.style.backgroundColor;
	if (bg == "lightgreen") { h1.style.backgroundColor = 'dodgerblue'; } 
  else { h1.style.backgroundColor = 'lightgreen';}
	return true;
}
boton.addEventListener('onclick', () => cambiarColor())
boton.addEventListener('mouseover', () => boton.style.backgroundColor = 'red')
boton.addEventListener('mouseout', () => boton.style.backgroundColor = 'gold')
~~~

~~~
input.addEventListener('keydown', (event)=> {
	h2.style.backgroundColor = 'gold';
	h2.textContent = "esta presionando teclas";

	console.log("Pulsaste la tecla", String.fromCharCode(event.keyCode));
});
~~~

~~~
input.addEventListener('keyup', ()=> {
	let mimimi = '';
	mimimi = input.value;
	h1.textContent = mimimi
	h2.style.backgroundColor = 'gold';
	h2.textContent = "soltaste la tecla";
});
~~~

# Load 
Carga los elementos antes que el script  
podemos usar esta funcion para cargar los script en el head  
~~~
window.addEventListenner('load', () => {
	// Code...
});
~~~

# Timers
Funciones de tiempo  
1. setTimeout() ***se ejecuta 1 sola vez, callback en milisegundos***
2. setInterval() ***se ejecutará cada X segundos, callback en milisegundos***
3. clearInterval() ***frena el bucle setInterval***

***setTimeout***  
~~~
const tiempo = setTimeout( () => console.log('el setInterval se va a ejecutar cada 3 segundos') , 3000)
~~~

***setInterval***  
~~~
const intervaloDeTiempo = setInterval( () => console.log('el setInterval se va a ejecutar cada 3 segundos') , 3000)
~~~

***clearInterval***  
~~~
elemento.addEventListener('click', () => clearInterval (intervaloDeTiempo) )
~~~

***Ejercicio***  
intervalo que inicie y frene un lapso de tiempo  
~~~
const start = () => {
	const timer = setInterval( () => console.log('el setInterval se va a ejecutar cada 3 segundos') , 3000)
	return timer;
}

elemento.addEventListener('click', () => start())
elemento.addEventListener('click', () => clearInterval (start))
~~~

# This
hace referencia al mismo objeto  
~~~
const boton = document.getElementById('boton');

boton.addEventListener('click', () => {
	if ( this.style.backgroundColor == 'dodgerblue' ) {
    this.style.backgroundColor = 'lime'
		this.style.color = 'black'
	} 
  else {
		this.style.backgroundColor = 'dodgerblue'
		this.style.color = 'white'
	}
})
~~~

# JSON
array asociativo  
objeto.propiedad
~~~
const heroe = {
	title: "Batman y Robin",
	origin: "USA",
	year: 1950
};

console.log(heroe.title, heroe.origin, heroe.year);
~~~

## Iterar JSON en Array
~~~
const peliculas = [
	{title: 'ironman', origin:'use', year:2008}
	{title: 'batman', origin:'use', year:2000}
	{title: 'spiderman', origin:'use', year:2006}
	{title: 'matrix', origin:'use', year:2000}
]

let mostrar = document.querySelector('#contenedorPeliculas')

for (let pelicula in peliculas) {
	let elemento = document.createElement('p')
	elemento.append(`${peliculas[pelicula].title` - ${peliculas[pelicula].year})
	mostrar.append(elemento)
}
~~~

# localStorage
almacenamiento en el navegador  

***valida que se pueda usar el local storage del navegador***  
~~~
if (typeof(Storage) !== 'undefined') {
	console.log("localstorage disponible")
} 
else {
	console.log("localstorage NO disponible")
}
~~~
1. existe un local storage disponible por dominio
2. file:// es nuestro dominio
3. se almacena la informacion (key, value)
4. se comprueba en el devtools, almacenamiento

***guardar datos en localStorage***  
> localStorage.setItem('key','value')

~~~
localStorage.setItem("titulo1", "Curso Master Javascript");
localStorage.setItem("titulo2", "Curso Master PHP");
localStorage.setItem("titulo3", "Curso Master NodeJs");
~~~

***mostrar datos del localStorage***  
> localStorage.getItem('key')
~~~
document.querySelector("#titulo1").innerHTML = localStorage.getItem('titulo1'); 
document.querySelector("#titulo2").innerHTML = localStorage.getItem('titulo2'); 
document.querySelector("#titulo3").innerHTML = localStorage.getItem('titulo3'); 
~~~

***guardar un JSON en localStorage***  
1. para guardar se debe convertir el json en string
2. JSON.stringify()
3. localStorage.setItem("json_stringify", JSON.stringify(user))
4. almacena valor id y el json en string

~~~
const user = {
	id: "101010",
	nombre: "crkj",
	email: "crkj@email.com",
	web: "crkj.com",
}

localStorage.setItem(`${user.id}`, JSON.stringify(user))
~~~

***recuperar el JSON del localStorage***  
1. recuperar el JSON_String a JSON_Object 

~~~
const user = JSON.parse(localStorage.getItem(`${user.id}`))
console.log(user);
~~~
> {id: '101010', nombre: 'crkj', email: 'crkj@email.com', web: 'crkj.com'}

***Mostrar en HTML***  
~~~
const mostar = document.querySelector("#mostar")
mostrar.innerHTML = `
	<h2>Objeto JSON</h2>
	<div>
		<p>nombre: ${user.nombre}</p>
		<p>email: ${user.email}</p>
		<p>web: ${userJson.web}</p>
	</div>
`
~~~

***borrar el localStorage***  
> localStorage.removeItem(`101010`)

***limpiar el localstorage***  
> localStorage.clear(); 






