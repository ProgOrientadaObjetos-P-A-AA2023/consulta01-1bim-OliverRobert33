"""
Crear dos clases en Python
Usted defina el nombre y los atributos
Puede usar las mismas clases usadas en Java en los ejemplos estudiados
"""



# clase 01
class CalcularSueldo():        
    def __init__(self, n, a, e, na, c, dT, cD):
        self.nombre = n
        self.apellido = a
        self.edad = e
        self.nacionalidad = na
        self.cedula = c
        self.diasTrabajados = dT
        self.costoDia = cD

    def calcular(self):
        self.sueldo = self.diasTrabajados * self.costoDia
        
    def __str__(self):
        return f"Nombre: {self.nombre}\nApellido: {self.apellido}\nEdad: {self.edad}\n\
Nacionalidad: {self.nacionalidad}\nCedula: {self.cedula}\nDias Trabajados: {self.diasTrabajados}\n\
Costo del dia: ${self.costoDia}\nSueldo:${self.sueldo}"
        



# clase 02
# Los profesores de un instituto tienen algunas características: nombre, apellido, 
# sueldo básico, sueldo total y cédula. El sueldo total es igual al sueldo básico 
# más el 20% del sueldo básico.

class Sueldo():
    nombre = ""
    apellido = ""
    cedula = ""
    sueldoBasico = 0.0
    def __init__(self, n, a, c, sB):
        self.nombre = n
        self.apellido = a
        self.cedula = c
        self.sueldoBasico = sB
    def calcular(self):
        self.sueldoTotal = (self.sueldoBasico * 0.20) + self.sueldoBasico
    
    def __str__(self):
        return f"Nombre: {self.nombre}\nApellido: {self.apellido}\nCedula: {self.cedula}\n\
Sueldo Basico: {self.sueldoBasico}\nSueldo Total: {self.sueldoTotal}\n"
 

