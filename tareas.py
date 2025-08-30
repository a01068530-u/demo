"""
Proyecto tareas python
Simulador de Tareas
"""

#Lista donde se guardan las tareas
lista = []

while True: #para que se repita siempre
   print("MENU")
   print("1. Agregar Tarea")
   print("2. Mostrar tarea")
   print(3. Salir")

   opcion = int(input("Elige una opcion"))
   if opcion == 1:
      tarea = input("Escribe una tarea")
      lista = lista + [tarea]
      print("tarea guardada")
   elif opcion == 2: 
      print("Tus tareas son:)
      for tarea in lista:
          print("-", tarea)
   elif opcion == 3:
     print("No tiene tarea pendiente")
   
