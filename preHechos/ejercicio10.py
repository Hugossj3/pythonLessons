#crea una clase llamada Persona 
class Persona:
 def __init__(self, nombre, edad):
    #  se crea un constructor y define los atributos de la clase Persona
    self.nombre = nombre
    self.edad = edad

 def saludar(self):
     #define una funcion de la clase que imprime un mensaje
    print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")
    
    
# Crear un objeto de la clase Persona
persona1 = Persona("Luis", 30)
# y usa uno de sus metodos
persona1.saludar()