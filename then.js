'use strict'

// Fetch y promesas a peticiones de servicios / apis rest
const listUsuarios = document.querySelector('#root') 
const listJanet = document.querySelector('#janet') 

// peticion fetch usuarios
const getUsuarios = () => {
	return fetch('https://reqres.in/api/users')
}

// peticion fetch a janet
const getJanet = () => {
	return fetch('https://reqres.in/api/users/2')
}

// lista los usuarios
const listarUsuarios = (usuarios) => {
	usuarios.map((user, i) => {
		let nombre = document.createElement('h4');
		nombre.innerHTML = ` ${i+1} Nombre: ${user.first_name} ${user.last_name} <br> Email: ${user.email}`;
		listUsuarios.append(nombre);
		document.querySelector('.cargando').style.display = 'none';
	});
}

// mostrar janet
const mostrarJanet = (user) => {
	let nombre = document.createElement('h4');
	let avatar = document.createElement('img');

	nombre.innerHTML = ` Nombre: ${user.first_name} ${user.last_name} <br> Email: ${user.email}`;
	
	avatar.src = user.avatar;
	avatar.width = '130';

	listJanet.append(avatar);
	listJanet.append(nombre);
	document.querySelector('#janet .cargando').style.display = 'none';
}

// peticion fetch usuarios then es la promesa
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