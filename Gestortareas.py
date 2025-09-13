"""
Avance 4
Algoritmo: Gestor de Tareas con estructuras de decisión simples
Descripción:
El usuario puede agregar tareas, verlas o salir.
"""

def agregar_tarea(lista, tarea):
    return lista + [tarea]
def mostrar_tareas(lista):
    # Decisión según cuántas tareas hay
    if lista == []:
        return "No hay tareas registradas"
    elif lista[1:] == []:   # si solo hay 1 tarea
        return "1" + lista[0]
    elif lista[2:] == []:   # si hay 2 tareas
        return "1" + lista[0] + "2" + lista[1]
    else:                   # si hay 3 o más
        return "1" + lista[0] + "2" + lista[1] + "3" + lista[2]

tareas = []
seguir = 1

while seguir == 1:
    print("Menú")
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
