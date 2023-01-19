# Sistema de diseño 

### Container 
es un estandar adaptado a unas unidades, adaptado a los procesos de diseño.
conjunto de reglas que se modifica deacuerdo a las necesidades.

### Partes del Design System:
- Principios: marcan la pauta y las reglas de nuestro producto
- Sistema: Cual va a ser el flujo de creación (tiempos y forma)
- Fundations: Bases de todo lo visual
- Componentes: Partes que forman un todo

herramientas
1. verbe
2. evernote
3. notion

hiperlink

### notion: 
1. Design System 

1. principios ***marcan la logica de nuestro producto***
2. sistema ***que partes intervienen***
3. fundations ***son las bases que contienen todo el sistema***
4. componentes ***partes que conforman el sistema***

En notion se crean pagina para ordenan lo que vamos a documentar

Los principios del diseño son la base fundamental de los paradigmas y metodologías que aplicaremos en nuestro sistema. Todas las decisiones que tomemos deben tener en cuenta y fundamentarse en estos principios, así evitamos cometer errores o generar conflictos, ya que todos los caminos serian correctos.

Principios del sistema de diseño:

- Accesibilidad: Nuestro producto debería ser usable para cualquier usuario, debemos construir productos perceptibles, operables, entendibles y robustos.

- Consistencia: Todo el equipo deben tener los mismos objetivos y deben hablarle de la misma forma a los usuarios, sea visualmente o por escrito.

- Reusabilidad: Cada hora que invirtamos trabajando en algún componente debe servir para construir otros componentes y evitar que tu o alguien más tenga que reconstruir nuestro trabajo.

- Shareable: Debemos construir y trabajar con herramientas que nos permitan compartir todo nuestro trabajo.

Podemos añadir otros principios que se adecuen correctamente a nuestra empresa, pero debemos tener cuidado de que todos estos principios sean compatibles entre sí.

En nuestro caso, añadiremos los principios de User Control (el usuario debe tener la sensación de control sobre el producto), Forgiveness (debemos permitir que el usuario pueda cambiar de opinión o volver a empezar algún proceso) y Perceived stability (aún con plataformas robustas y complejas, el usuario debe percibir los procesos tan simples y familiares como sea posible).

Principios:
1. consistencia
2. accesible
3. user control
4. forgiveness
5. preceived stability


## Niveles de sistematizacion 
SD Team 

- Solitario: tú construyes, los demás consumen
- Centralizado: tú consultas a los demás departamentos y construyes un SD
- Confederado: varios equipos dentro de varios departamentos y todos construyen el sistema

building design systems 

El Design System Workflow nos ayuda a entender mucho mejor cómo entra, por dónde sale y por cuáles puntos pasa nuestro trabajo cuando trabajamos con sistemas de diseño.

En este workflow o flujo de trabajo comenzamos diseñando y documentando para después hacer deploy (un término de programación para los momentos en que pasamos nuestro trabajo a producción, una versión funcionando en vivo), en esta etapa de deploy debemos tener muy claro para cuál plataforma o entorno estamos trabajando, así tendremos mucho más claro todo lo que vamos a necesitar construir (por ejemplo, cuando construimos páginas web trabajamos en archivos .css con los estilos de nuestros productos).

Pero el trabajo no termina aquí, después de hacer deploy entramos a la etapa de testing para evaluar la efectividad de estos estilos y seguirlos mejorando.

También vamos a aprender sobre Building Design Systems, donde construimos herramientas para que todos puedan usar e implementar las guías y los estilos que estamos trabajando. Para organizarnos y sistematizar estos procesos podemos implementar el modelo solitario, dónde tú, el diseñador haces todo el trabajo para que alguien más lo consuma, pero existen otros modelos como el centralizado o el confederado donde trabajamos con otras personas o incluso otros equipos y pedimos feedback dependiendo de la organización de nuestras empresas.

## https://coggle.it/
para hacer el sistema de diseño, en el flujo de trabajo

# Coggle
Como funciona 

# Paradigmas: diseño atómico, diseño procedural y DRY 
procedural: son elementos ya hechos que van hacer que el resultado sea variado, funciones que a futuro se van a construir asi mismas 
1. varios tipos de elementos para que al armar se conbinen y se creen resultados procedurales

Diseño atómico: principio de bren bros. 
1. darle organizacion 
- atomos
- moleculas
- organismos
- templates
- paginas

atomos: 
- label
- input
- button

molecula:
- es cuadno se juntan dos atomos

organismos:
- cuando juntamos 2 moleculas

template:
- jusntamos organismos

paginas:
- elementos ya personalizados con la variantes ya personalizados

### no debemos diseñar pantallas si no atomos

# DRY
Dont repeat your self 

no repetir los diseños 

## utilizando Adobe XD vs Figma
1. 

## que es un componente 
Los componentes forman parte de un todo, así como las velas de un pastel, el piso de los edificios o las partes de un motor cada una con su funcionalidad. Lo mismo pasa con las interfaces, vamos a construir diferentes elementos y herramientas para que los usuarios logren cumplir sus objetivos.

Todos los componentes tienen una entrada y una salida, el usuario realiza una acción y los elementos deben responder de alguna forma (feedback), esta es la forma de comunicamos con los usuarios, trabajamos haciendo conversaciones para informar que todo esta funcionando correctamente y qué pasos deben seguir a continuación. Este proceso de comunicación lo conocemos como interacción.

Partes de un componente:

- Nombre (así evitamos diferentes definiciones y establecemos los objetivos y funciones de nuestros componentes)
- Descripción y solución (en qué problema estamos trabajando y cómo deberíamos implementar estas soluciones)
- Behavior (el comportamiento de nuestros componentes dentro del sistema)
- States (las variaciones y distintos comportamientos que pueden tener nuestros componentes dependiendo de su contexto)

es una pieza que hace parte de un todo para crear un componente

en un componente debe haber una entrada y una salida, (feetback)

usuario - componente = interaccion

partes de un componente.
1. nombre: NO ventanita, module, cajita
2. descripcion: de que es
3. behavior
4. states: como cambia el componente

## Notion: <br>
### Componentes:
#### atomos
- Labels
- Buttons
- Inputs
- Text 
- Modal

#### Moleculas
- Input Search
- alerts

#### organismos
- Top Navbar
	- Esta es la barra de navegacion superior que le ayuda al usuario para navegar por toda la plataforma
	- nombre: top_mavbar
	- descripcion: Aqui es donde el usario tiene a la mano las herramientas necesarias para navegar por la plataforma y le permite hacer acciones como 
		- Login
		- logout
		- embet ***(imagen)*** como se veria
		- states: normal, hover, focus
		- behavior


- Alerts System
- Footer

#### Paginas Los componentes forman parte de un todo, así como las velas de un pastel, el piso de los edificios o las partes de un motor cada una con su funcionalidad. Lo mismo pasa con las interfaces, vamos a construir diferentes elementos y herramientas para que los usuarios logren cumplir sus objetivos.

Todos los componentes tienen una entrada y una salida, el usuario realiza una acción y los elementos deben responder de alguna forma (feedback), esta es la forma de comunicamos con los usuarios, trabajamos haciendo conversaciones para informar que todo esta funcionando correctamente y qué pasos deben seguir a continuación. Este proceso de comunicación lo conocemos como interacción.

Partes de un componente:

Nombre (así evitamos diferentes definiciones y establecemos los objetivos y funciones de nuestros componentes)
Descripción y solución (en qué problema estamos trabajando y cómo deberíamos implementar estas soluciones)
Behavior (el comportamiento de nuestros componentes dentro del sistema)
States (las variaciones y distintos comportamientos que pueden tener nuestros componentes dependiendo de su contexto)
- Main Page 

#### Templates
- Login
- Course
- Profile Page 

#### Patrones 
- Login flow
- Conversion flow

___

# fundations 

Los sistemas de diseño son un conjunto de reglas que organizamos con nuestros equipos, y los fundations son las partes más básicas que podemos configurar en nuestro sistema. Vamos a repasar cada una de estas bases mientras escribimos la documentación en Notion:

- Tipografía
- Colores
- Layout y spaces (son las formas y espacios fundamentales que utilizamos para ordenar los elementos de nuestro sistema)
- Iconografía
- Styles (nuestra marca puede presentarse con estilos juguetones o realistas, lo importante es definir tan claro como sea posible qué intentamos transmitir)
- Tono (con qué personalidad o de qué forma debemos hablar con nuestra audiencia)

son los elementos, que vamos a crear para luego utilizarlos 

conjunto de reglas que definen el producto

# Tipografía

Cuando trabajamos con tipografía para software debemos tener en cuenta las implicaciones que estas pueden generar si trabajamos para dispositivos móviles o los requerimientos técnicos de alguna pantalla en particular. Un buen lugar para encontrar tipografías listas para el desarrollo y diseño de nuestros productos es Google Fonts.

Para definir y clasificar las características y peculiaridades en los elementos de nuestro diseño podemos basarnos las etiquetas de HTML para títulos y encabezados (H1, H2, H3, H4, H5 y H6), párrafos (p) y párrafos más pequeños (small). Podemos definir que los títulos se trabajen en negrita y con tamaños de fuente más grandes, lo importante es que estas reglas se acomoden al sistema de diseño que estamos trabajando.

Google fonts

Extensiones Chrome
1. Whatfont
2. FontFace

h1 bold -> 50px
h2 bold -> 25px
h3 bold -> 20px

parrafo -> normal 13px
Small -> normal -> 10px
Bold -> bold -> 13px

# Como evitar colores constrastantes 

# Paleta de colores

COLORES PARA PALETAS DE COLORES

Primarios: Rojo - Azul - Amarillo

- Monocromático: Un color con diferente opacidad
- Análoga: Un primario + un secundario + un terciario
- Complementaria: Primario + Inverso Secundario
- Triádica: En triangulo (Tres del mismo tipo)
- Tétrada: En rectángulo (2 primarios + 2 secundarios)

Esto lo aprendí en el curso de Diseño para programadores

# Paleta de colores 
Material Design
1. primarios
2. secundarios 

Action colors 
	colores de acciones dentro de la pagina

Brand colors
	los colores de la marca

Gray
escala de blanco a grises 

Backgrounds 
dan contraste a nuestros colores 
se requiere paradicmas desicion de color 

boolean colors

material design: es un sistema de diseño

# Reglas de espaciado 

UI design -> Software

se debe definir reglas de espaciado, para no tener anormalizadades y definir una estandarizacion a nuestros elementos.

ritmo de la aplicacion: dejando descansar el ritmo visual 

margin, padding, border: afectan nuestro elemento, 
elemento + border + margin = 52px, ya no es el elemento de 50px

layout se debe definir el orden antes de

sistema de columnas: botstrap 

unidades son sumadas 
10px
se deben usar 1 2 o 3 unidades de espaciado 

1 unidad es 10px
2 unidades serain 20 px

documentacion.

Margin: unidad de 10px, afectando a todos los items a su alrededor 

Padding: tendremos una unidad (10px) de cada lado cuando los componentes contengan contenido 

Unidades de espaciado: una unidad de espaciado es igual a 10px, por lo tanto 2 unidades serian 20px, 
	Es libre la configuracion de estas unidades mientras se usen en totales y medias (1,2,2,5,3,3,5), y no parciales de (2,4,6)

# animacion 
que pasa con las animaciones dentro de un sistema de diseño

principios de animacion de disney
1. Estirar y encoger: 
2. anticipacion: manda la vista hacia un lugar
3. entradas lentas y salidas lentas: fadein fadeout
4. acciones secundarias: accion despues del click, informacion adicioanl al usuario
5. timing: muchos frames, ayudan a mejorar y dan mas dentalle dando sensacion
6. exageracion: eliminacion, si hay error ya no se puede hacer nada 

documentar 
animation: En esta seccion explicamos las animaciones permitidas de nuestro sistema y en que situaciones las utilizaremos.

Referencia de animaciones: https://daneden.github.io/animate.css/

Fade in <br>
Cuando un elemento independiente de la pantalla tiene la necesidad de entrar o aparecer

Fade out <br>
Cuando un elemento tienen la necesidad de salie de la vision del usuario

1. configuracion de estas animaciones son: left right up down

animate.css

# consejos para animar usando After Effects

# Voz y tono 
- de como escribir, 
- let's rock

especifica como vamos a comunicarnos con el usuario 

categorizacion:
1. buzzwords: instrumentos musicales traidos por dios, o guitarras
2. phrases: compilacion de varias palabras
3. objetivo: que queremos comunicar. 
4. caracteristias: tipo de palabras con las que comunicamos.

Documentacion
Voz y tono: 
Terget: Genero: Ambos <br>
Edad: 18-50 años

Características

El tono que utilizaremos para este producto se guiara por las siguientes caracteristicas:

### Tono neutro
Utilizaremos palabras con interpretacion internacional a todos los de habla hispana

### Usuario centered
Le hablamos al usuario en 1 persona, esto siginifica que las acciones se representaran de la siguiente manera: 

-> Terminar
-> Hacerlos de nuevo

### Uso de emojis
El uso de emojis queda permitido para aplicaciones sobre párrafo descriptivo en páginas estáticas y emails, Queda restringido o bajo evaluacion cuando lo apliquemos en instruccones o acciones dentro de la plataforma.

# Iconografía
Icon system 

libreria existente: fontosom

libreria personal:

Grid: linamiento de espaciado, medidas
Shapes: fromas, border redondos, circulos, cuadrados,
Tamaños: en proporcion uniforme, flujo y aplicacions
Styles: de

Documentación
grid, chapes, style

Se debe ser claros, consisos, ya que se debe entregar la informacion para que la entienda nuestro equipo, ya que diseñar un sistema lleva demasiado tiempo

# Hitos
marcadores personales,

logos en icono, que interactual entresi, que ya se sabe quiene son

comunicacion, personalizando en una animacion

Documentacion:

### Hitos
Estos son elementos importantes para nuestro sistema y tiene caracteristicas particulares dentro de nuestra aplicacion pues son una representacion de todos los conceptos que queremos comunicar.

Icono <br>
loader <br>

# UI kit 
DS files

libreria general de UI elements 

# DesignSystem basado en personas
concepto: product -> team -> Design System 

vision: direccion de como se queria

produccion: ya tiene todo definido

marketing: 

difucion:

finanzas: 

Let's Flow -> coggle 

nuestro sistema de diseño conlleva el uso de varias tecnologias, conocimiento de varias cosas, muchas personas haciendo este producto, 

Es la planeacion de un flujo, para la creacion de un producto, y la creacion de herramientas para que todos puedan crearlos de manera mas rapida y efectiva

# iteremos 
como vamoa iterar un producto cuando ya lo terminamos 

objetivos principales. 

se recibe el feedback de los componentes que puede que no esten funcionando correctamente

prodeso de iteracion
1. necesitamos un nombre
2. por que estamos iterando
3. describiendo el problema
4. cambios y estimaciones de conflicto


Documentacion

Proceso de iteracion 

En esta seccion guardaremos un historial de los procesos que vamos mejorando y sus conclusiones: 
- Template

### {{ Nombre }} 
Nombre del componente

#### Description: 
Desarrollaremos el objetivo de nuestro, desarrollando tambien el nuevo problema a solucionar 

#### Solucion: 
Aqui puedes escribir la solucion a la que llego el equipo para solucionar el motivo de porque estamos iterando 

#### Cambios y estimacion de conflictos
Describiremos puntualmente las acciones pertinentes para que la solucion se lleve a cabo, ademas de darle a estas acciones y asi saber cual es el tiempo de desarrollo.

___