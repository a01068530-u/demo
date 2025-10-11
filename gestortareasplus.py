"""
Avance 7
Algoritmo: Gestor de Tareas con listas anidadas
Descripción:
El usuario puede agregar tareas, verlas, marcarlas como hechas o salir.
"""

def agregar_tarea(lista, tarea):
    nueva_tarea = [tarea, "pendiente"]   
    lista = lista + [nueva_tarea]
    return lista

def mostrar_tareas(lista):
    if lista == []:
        return "No hay tareas registradas"
    else:
        texto = ""
        numero = 1
        for tarea in lista:
            texto = texto + str(numero) + ". " + tarea[0] + " (" + tarea[1] + ") "
            numero = numero + 1
        return texto

def marcar_hecha(lista, numero):
    if numero > 0 and numero <= len(lista):
        lista[numero - 1][1] = "hecha"
        print("Tarea marcada como hecha")
    else:
        print("Número de tarea no válido")
    return lista

tareas = []
seguir = 1

while seguir == 1:
    print("MENÚ")
    print("1. Agregar Tarea")
    print("2. Mostrar Tareas")
    print("3. Marcar como Hecha")
    print("4. Salir")

    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        nueva = input("Escribe una tarea: ")
        tareas = agregar_tarea(tareas, nueva)
        print("Tarea guardada")

    elif opcion == 2:
        print(mostrar_tareas(tareas))

    elif opcion == 3:
        print(mostrar_tareas(tareas))
        num = int(input("Número de tarea para marcar como hecha: "))
        tareas = marcar_hecha(tareas, num)

    elif opcion == 4:
        print("Programa finalizado")
        seguir = 0

    else:
        print("Opción no válida")
