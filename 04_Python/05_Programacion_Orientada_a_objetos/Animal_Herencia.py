#!/usr/bin/python3

class Animal:
  
  def __init__(self, nombre):
    self.nombre = nombre
    
  def hablar(self):
    raise NotImplementedError("Las subclases definidas deben implementar este método")

class Gato(Animal): # Hereda de la clase Animal

  def hablar(self):
    return f"{self.nombre} dice ¡Miau!"
  
class Perro(Animal): # Hereda de la clase Animal
  
  def hablar(self):
    return f"{self.nombre} dice ¡Guau!"
  
gato = Gato("Coco")
perro = Perro("Lucas")

print(gato.hablar())
print(perro.hablar())