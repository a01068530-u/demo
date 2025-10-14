# Pensamiento Computacional 
En este proyecto se considera que en la vida cotidiana es común tener múltiples pendientes o sin hacer, ya sean trabajos académicos, compromisos personales o cosas laborales. Un gestor de tareas permitiría organizar dichos pendientes de forma estructurada facilitando el registro y el cumplimiento de las mismas; con este proyecto se busca utilizar la programación para resolver esta necesidad de manera práctica y sencilla.

# Objetivo
Desarrollar un programa que funcione comom un gestor de tareas, dejando que el usuario cree, modifique y elimine sus tareas para que pueda llevar un control básico de sus actividades

# Algoritmo
Inicio del programa

Se importa la biblioteca datetime para manejar fechas y horas.

Se inicializa una lista vacía llamada tareas donde se almacenarán todas las tareas.

Mostrar menú principal

Se imprime un menú con las siguientes opciones:
1️ Agregar tarea
2️ Ver tareas
3️ Completar tarea
4️ Salir

Leer opción del usuario

El programa solicita al usuario que elija una opción mediante input().

Si el usuario elige "1. Agregar tarea":

Se pide al usuario que escriba una descripción de la tarea.

Se agrega una sublista a la lista principal tareas con el formato:
["nombre de tarea", "pendiente"].

Se muestra un mensaje de confirmación.

Si el usuario elige "2. Ver tareas":

Se recorre la lista tareas con un ciclo for.

Se muestran todas las tareas con su número de orden y estado actual.

Si la lista está vacía, se muestra el mensaje “No hay tareas registradas”.

Si el usuario elige "3. Completar tarea":

Se muestra la lista de tareas disponibles.

El usuario elige el número de tarea que desea marcar como completada.

El programa obtiene la fecha y hora actual usando datetime.datetime.now().

Se actualiza el estado de la tarea a:
"completada (fecha y hora)".

Se muestra un mensaje confirmando el cambio.

Si el usuario elige "4. Salir":

El ciclo principal termina.

Se muestra un mensaje de despedida:
"¡Gracias por usar el administrador de tareas!".

Si el usuario ingresa una opción incorrecta:

Se muestra un mensaje de error y se repite el menú.

Fin del programa


# Referencias API
"datetime" (https://docs.python.org/3/library/datetime.html): se usa para obtener la fecha actual de cada gasto.
