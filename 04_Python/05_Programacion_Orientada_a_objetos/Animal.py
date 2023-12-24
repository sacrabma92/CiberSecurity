#!/usr/bin//python3

class Animal:

  def __init__(self, nombre, animal):   # Aniaml.__init__(gato,nombre,animal)
    self.nombre = nombre
    self.animal = animal
    
  def descripcion(self): # Animal.descripcion(obj)
    print(f"{self.nombre} es un {self.animal}")
    
gato = Animal("Coco", "Gato")
perro = Animal("Porky", "Perro")

gato.descripcion()
perro.descripcion()