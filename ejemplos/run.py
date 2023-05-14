"""

"""
# Crear dos objetos de la clase 01
# objeto 01
# crear
# Presentar objeto; usar el método __st__
# objeto 02
# crear ingresando valores por teclado
# Presentar objeto; usar el método __st__

from mis_clases import Sueldo

print("\nIngrese datos para el primer Objeto")
nombre = input("Ingrese sus nombres: ")
apellido = input("Ingrese sus apellidos: ")
cedula = input("Ingrese su identificacion: ")
sueldo_basico =  float(input("Ingrese su sueldo: "))


profesor1 = Sueldo(nombre, apellido, cedula, sueldo_basico)
profesor1.calcular()



# Imprimir los datos del objeto
print("----------------------------------------------")
print(profesor1)
print("----------------------------------------------")


