"""
Proyecto Final: Administrador de Tareas
Guillermo Pérez Ayala A01068530
Descripción general:
Este programa es un pequeño sistema para administrar tareas pendientes.
Permite al usuario agregar tareas, ver la lista de tareas actuales y
marcarlas como completadas. Además, guarda la fecha y hora en que
una tarea fue completada utilizando el módulo estándar 'datetime'.
"""

# bibliotecas 
import datetime   # modulo para trabajar con fechas y horas

# funciones principales

def agregar_tarea(lista_tareas):
    """
    (Uso de listas, funciones, entradas)
    Pide al usuario el nombre de una tarea y la agrega a la lista principal
    como una sublista con estado 'pendiente'.
    """
    tarea = input("Escribe el nombre de la tarea: ")
    lista_tareas.append([tarea, "pendiente"])
    print("Tarea agregada con éxito.")


def ver_tareas(lista_tareas):
    """
    (Uso de ciclos, condicionales)
    Muestra todas las tareas registradas y su estado actual.
    """
    if not lista_tareas:
        print("No hay tareas registradas.")
    else:
        print(" Lista de tareas ")
        for i, tarea in enumerate(lista_tareas):
            print(f"{i+1}. {tarea[0]} - Estado: {tarea[1]}")


def completar_tarea(lista_tareas):
    """
    (Uso de índices, condicionales, biblioteca datetime)
    Permite marcar una tarea como completada. Registra la fecha y hora exacta.
    """
    ver_tareas(lista_tareas)
    if lista_tareas:
        try:
            num = int(input("Número de tarea a marcar como completada: ")) - 1
            if 0 <= num < len(lista_tareas):
                fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                lista_tareas[num][1] = f"completada ({fecha_actual})"
                print("Tarea marcada como completada.")
            else:
                print("Número de tarea inválido.")
        except ValueError:
            print("Debes ingresar un número válido.")

# función principal 

def menu():
    """
    (Uso de ciclos, funciones y estructura de control)
    Muestra un menú con opciones para administrar tareas.
    """
    tareas = []
    opcion = ""

    while opcion != "4":
        print(" MENÚ DE OPCIONES ")
        print("1. Agregar tarea")
        print("2. Ver tareas")
        print("3. Completar tarea")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            agregar_tarea(tareas)
        elif opcion == "2":
            ver_tareas(tareas)
        elif opcion == "3":
            completar_tarea(tareas)
        elif opcion == "4":
            print("¡Gracias por usar el administrador de tareas!")
        else:
            print("Opción no válida, intenta de nuevo.")

