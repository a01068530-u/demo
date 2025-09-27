"""
Avance 5
Algoritmo: Gestor de Tareas con ciclos
Descripción:
El usuario puede agregar tareas, mostrarlas con un ciclo o salir.
"""

def agregar_tarea(lista, tarea):
    return lista + [tarea]

def mostrar_tareas(lista):
    if lista == []:
        return "No hay tareas registradas"
    else:
        texto = ""
        numero = 1
        for tarea in lista:  # recorre cada tarea en la lista
            texto = texto + str(numero) + " " + tarea + " "
            numero = numero + 1
        return texto

tareas = []
seguir = 1

while seguir == 1:
    print("MENÚ")
    print("Agregar Tarea")
    print("Mostrar Tareas")
    print("Salir")

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
