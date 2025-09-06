"""
Avance 3
Algoritmo: Gestor de Tareas con operadores y funciones
Descripción:
Este algoritmo permite al usuario registrar tareas pendientes en una lista.
Se pueden agregar nuevas tareas, mostrar las tareas actuales o finalizar el programa.
"""

def agregar_tarea(lista, tarea):
    lista = lista + [tarea]  
    return lista


def mostrar_tareas(lista):
    if len(lista) == 0:
        return "No hay tareas registradas"
    elif len(lista) == 1:
        return "1" + lista[0]
    elif len(lista) == 2:
        return "1" + lista[0] + "2" + lista[1]
    else:
        return "1" + lista[0] + "2" + lista[1] + "3" + lista[2]

tareas = []    
seguir = 1      

while seguir == 1:
    print("Menu")
    print("1. Agregar Tarea")
    print("2. Mostrar Tareas")
    print("3. Salir")

    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        nueva = input("Escribe una tarea: ")
        tareas = agregar_tarea(tareas, nueva)
        print("Tarea guardada")

    elif opcion == 2:
        print(mostrar_tareas(tareas))

    elif opcion == 3:
        print("Programa finalizado")
        seguir = 0   
    else:
        print("Opción no válida")

   
