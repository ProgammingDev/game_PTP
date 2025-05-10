🔵 Usuario hace un request HTTP (por ejemplo: POST /mesa)
⬇️
🟡 Route detecta esa URL y llama al controlador
⬇️
🟢 Controller recibe datos, llama a un service
⬇️
🔴 Service ejecuta la lógica usando objetos del dominio
⬇️
🟢 Controller arma el DTO y lo convierte a JSON
⬆️
🟡 Route responde al navegador o cliente con HTTP 200/201/etc

#
🧩 1. Domain (core/)
El corazón del sistema: contiene las entidades y las reglas del negocio.

Define qué es una Mesa, un Jugador, un Juego.

Define cómo se comportan: mesa.asignar_jugador(), juego.resolver_ronda()

No sabe nada de HTTP, bases de datos ni Flask.

#
🛠 2. Service (services/)
Orquesta acciones más complejas usando objetos del dominio.

Coordina la lógica entre varias entidades.

Hace tareas como: "crear una mesa y asignar dos jugadores", "validar si se puede jugar", etc.

No devuelve JSON ni maneja request.

#
🎮 3. Controller (controllers/)
Traduce lo que viene del usuario (API) y lo conecta con los servicios.

Recibe la request (POST, GET, etc.)

Llama al service correspondiente

Prepara el resultado para la response

Puede validar datos, hacer logging o manejo de errores

#
 4. Routes (blueprints/<tipo>/)
Define las URLs y a qué controlador llaman.

