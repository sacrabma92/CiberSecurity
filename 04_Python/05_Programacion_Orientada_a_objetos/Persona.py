#!/usr/bin/python3

class Persona:
  # Metodo constructor
  def __init__(self, nombre, edad): # Persona.__init__(carlos,31)
    self.nombre = nombre
    self.edad = edad
    
    # Metodo saludo
  def saludo(self): # Persona.saludo(carlos)
    return f"Hola, soy {self.nombre} y tengo {self.edad} años"

# Creamos instancia de la clase persona
carlos = Persona("Carlos", 31)
Juan = Persona("Juan", 32)

print(carlos.saludo())