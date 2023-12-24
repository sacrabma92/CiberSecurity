#!/usr/bin/python3

class Animal:
  
  def __init__(self, nombre):
    self.nombre = nombre
    
  def hablar(self):
    raise NotImplementedError("Las subclases definidas deben implementar este método") 

class Gato(Animal): # Hereda de la clase Animal

  def hablar(self):
    return "¡Miau!"
  
class Perro(Animal): # Hereda de la clase Animal
  
  def hablar(self):
    return "¡Guau!"
  
def hacer_hablar(objeto):
   print(f"{objeto.nombre} dice {objeto.hablar()}")
  
gato = Gato("Coco")
perro = Perro("Lucas")

hacer_hablar(gato)
hacer_hablar(perro)