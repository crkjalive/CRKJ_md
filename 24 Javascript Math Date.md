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

1. Tue Jan 24 2023 17:09:20 GMT-0500 (hora estándar de Colombia) ***fecha del sistema***
2. let year = fecha.getFullYear() ***mostrar el año***
3. let mes = fecha.getMonth() ***mostrar el mes contando desde cero***
4. let dia = fecha.getDay() ***muestra el dia de la semana***
5. let hora = fecha.getHours() ***muestra la hora***
6. let min = fecha.getMinutes() ***muestra los minutos***
7. let sec = fecha.getSeconds() ***muestra los segundos***
8. let milSec = fecha.getMilliseconds() ***muestra los milisegundos***
9. let utcDate = fecha.getUTCDate() ***fecha en numero***