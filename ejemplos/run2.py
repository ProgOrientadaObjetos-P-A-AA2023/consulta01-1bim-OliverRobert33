# Crear dos objetos de la clase 02
# objeto 01
# crear
# Presentar objeto; usar el método __st__
# objeto 02
# crear ingresando valores por teclado
# Presentar objeto; usar el método __st__

from mis_clases import CalcularSueldo

print("\nIngrese datos para el Primer Objeto")
nombre = input("Ingrese sus nombres: ")
apellido = input("Ingrese sus apellidos: ")
edad =  int(input("Ingrese su edad: "))
cedula = input("Ingrese su identificacion: ")
nacionalidad = input("Ingrese su nacionalidad: ")
dias_trabajados =  int(input("Ingrese los dias trabajados: "))
costo_dia =  float(input("Ingrese el costo del dia de trabajo: "))

usuario1 = CalcularSueldo(nombre, apellido, edad, cedula, nacionalidad,\
                           dias_trabajados, costo_dia) # Primer objeto
usuario1.calcular()

print("\nIngrese datos para el Segundo Objeto")
nombre = input("Ingrese sus nombres: ")
apellido = input("Ingrese sus apellidos: ")
edad =  int(input("Ingrese su edad: "))
cedula = input("Ingrese su identificacion: ")
nacionalidad = input("Ingrese su nacionalidad: ")
dias_trabajados =  int(input("Ingrese los dias trabajados: "))
costo_dia =  float(input("Ingrese el costo del dia de trabajo: "))

usuario2 = CalcularSueldo(nombre, apellido, edad, cedula, nacionalidad,\
                           dias_trabajados, costo_dia) # Segundo objeto
usuario2.calcular()


# Imprimir los datos del objeto
print("----------------------------------------------")
print(usuario1)
print("----------------------------------------------")
print(usuario2)
print("----------------------------------------------")
