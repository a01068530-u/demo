"""
Proyecto Final - Gestor de Tareas Mejorado
Guillermo Pérez Ayala 
A01068530
Descripción general:
Este programa simula un gestor de tareas donde el usuario puede agregar, ver y marcar tareas como hechas.
Además, guarda un registro con la fecha de ejecución.
Instrucciones para ejecutar:
1. Ejecuta el programa en donde programes.
2. El menú aparecerá automáticamente.
3. Usa los números 1 a 4 para navegar entre las opciones.
"""

# bibliotecas
import datetime   # para agregar fecha y hora al registro

# funciones principales 

def agregar_tarea(lista, tarea):
    """
    (uso de operadores y funciones)
    Agrega una tarea a la lista con estado pendiente.
    """
    return lista + [[tarea, "pendiente"]]

def mostrar_tareas(lista):
    """
    Muestra todas las tareas con su estado.
    """
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
    """
    Marca una tarea como hecha si el número es válido.
    """
    if numero > 0 and numero <= len(lista):
        lista[numero - 1][1] = "hecha"
    return lista

def calcular_porcentaje(tareas):
    """
    (uso de operadores aritméticos)
    Calcula el porcentaje de tareas hechas.
    """
    total = len(tareas)
    hechas = 0
    for t in tareas:
        if t[1] == "hecha":
            hechas = hechas + 1
    if total > 0:
        return (hechas / total) * 100
    else:
        return 0

#  menú 

def menu():
    """
    Función principal del programa
    Muestra el menú y controla la interacción con el usuario.
    """
    tareas = []
    seguir = 1

    print("Gestor de Tareas - Proyecto Final")
    print("Ejecutado el:", datetime.datetime.now().strftime("%d/%m/%Y %H:%M"))

    while seguir == 1:
        print(" MENÚ ")
        print("1. Agregar Tarea")
        print("2. Mostrar Tareas")
        print("3. Marcar como Hecha")
        print("4. Ver resumen y salir")

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
            print("Tarea actualizada")

        elif opcion == 4:
            print("Saliendo del programa...")
            porcentaje = calcular_porcentaje(tareas)
            restantes = len(tareas) - int(porcentaje * len(tareas) / 100)  # ejemplo de uso de *
            print("Completaste", porcentaje, "% de tus tareas.")
            print("Te faltan", restantes, "tareas por hacer.")
            seguir = 0

        else:
            print("Opción no válida")

    print(" Programa finalizado. ¡Gracias por usar el Gestor de Tareas!")

# Llamada al programa
menu()
