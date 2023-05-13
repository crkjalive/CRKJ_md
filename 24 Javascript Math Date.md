# Javascript funciones matemáticas y funciones date
***matemáticas con Math***  

1. Math.random() ***número aleatorio de 0 a 1***
2. Math.random()*10 ***número aleatorio de 1 a 9 cifras***  
3. Math.random()*100 ***número aleatorio de 2 cifras***  
4. Math.random()*1000 ***número aleatorio de 3 cifras***  
5. Math.ceil(Math.random()*20) ***redondea por arriba del 1 al 20***
6. Math.round(4.5) ***redondea despues de .5 por arriba***
7. Math.round(4.4) ***redondea antes de .5 por abajo***
Buscar más  

***fechas con Date***  
const fecha = new Date  

1. ***fecha es*** Tue Jan 24 2023 17:09:20 GMT-0500 (hora estándar de Colombia) ***fecha del sistema***
2. fecha.getFullYear() ***mostrar el año***
3. fecha.getMonth() ***mostrar el mes contando desde cero***
4. fecha.getDay() ***muestra el dia de la semana***
5. fecha.getHours() ***muestra la hora***
6. fecha.getMinutes() ***muestra los minutos***
7. fecha.getSeconds() ***muestra los segundos***
8. fecha.getMilliseconds() ***muestra los milisegundos***
9.  fecha.getUTCDate() ***fecha en numero***
10. fecha.toDateString() ***pasa a String la fecha -> "Tue Jan 31 2023"***  
11. fecha.toString() ***te entrega Fri Jul 02 2021 14:03:54 GMT+0100 (Horario de verano británico)***  
12. fecha.toLocaleString() ***te entrega 7/2/2021, 2:05:07 PM***
13. fecha.toLocaleDateString() ***te entrega 7/2/2021***  
14. fecha.toGMTString() ***te entrega Fri, 02 Jul 2021 13:06:02 GMT***
15. fecha.toUTCString() ***te entrega Fri, 02 Jul 2021 13:06:28 GMT***
16. fecha.toISOString() ***te entrega 2021-07-02T13:06:53.422Z***

***Formateo de fechas***  
~~~
const fechaActual = new Date();
const opciones = { weekday: 'long', year: 'numeric', month: 'short', day: 'numeric' };

console.log(fechaActual.toLocaleDateString('de-DE', opciones)) //Freitag, 2. Juli 2021
console.log(fechaActual.toLocaleDateString('ar-EG', opciones)) // الجمعة، ٢ يوليو ٢٠٢١
console.log(fechaActual.toLocaleDateString('en-us', opciones)) //Friday, Jul 2, 2021
~~~

***Cambiando opciones***  
~~~
new Date().toLocaleDateString('en-us', { weekday:"long", year:"numeric", month:"short"}) // "Jul 2021 Friday"
new Date().toLocaleDateString('en-us', { year:"numeric", month:"short"}) // "Jul 2021"
~~~