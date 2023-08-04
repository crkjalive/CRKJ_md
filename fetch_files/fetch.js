'use strict'

// Fetch y peticiones a servicios / api rest

const listadoUsuarios = document.querySelector('#root') 

// guardamos los usuarios de la api
let usuarios = [];

/* hacemos la peticion al servidor, 
llamada AJAX, accede a un servidor remoto api */
fetch('https://reqres.in/api/users') 

	// se queda a la espera, recoge los datos y los convirte en json
	.then(data => data.json()) 

	// peticion asyncrona que captura la data de los usuarios (users)
	.then(users => { 
		usuarios = users.data;
		console.log(usuarios);

		// iteramos la data de usuarios
		usuarios.map((user, i) => { 
			let nombre = document.createElement('h4');

			// insertamos info al document
			nombre.innerHTML = `${i+1} Nombre: ${user.first_name} 
				${user.last_name} <br> Email: ${user.email}
			`;

			// agregamos el elemento creado al div contenedor
			listadoUsuarios.append(nombre);

			// damos css para ocultar el span de cargando
			document.querySelector('.cargando').style.display = 'none';
		});
	});
