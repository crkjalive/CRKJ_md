# Javascript Fetch Promesas y try_catch 
Fetch: nos permite hacer peticiones ajax a una API REST,  
api en la nube con datos de prueba  

> https://jsonplaceholder.typicode.com/

# fetch
peticiones api al servidor
1. index.html
2. api.js 

# promesas y fetch 
con las promesas evitamos el callback hell  
ideal para trabajar con datos asincronos  

1. then.html
2. then.js
los then son las promesas o peticiones que hace al servidor, esperando  
a que se complete y continue con la siguiente promesa  

***promesa***  
~~~
getUsuarios()
	.then(data => data.json())
	.then(users => { 
		listarUsuarios(users.data);
		return getJanet();
	})
	.then(data => data.json())
	.then(user => {
		mostrarJanet(user.data);
	});
~~~

# try catch
todo codigo suceptible a errores podemos validarlo con este metodo try-catch  
~~~
try{
	// codigo a prueba
}
catch (error) {
	// error
}
~~~