#!/usr/bin/python3

class Automovil:
  def __init__(self, marca, modelo):
    self.marca = marca
    self.modelo = modelo

  def describir(self):
    return f"Vehiculo: {self.marca} {self.modelo}"
  
class Coche(Automovil):
  def describir(self):
    return f"Coche: {self.marca} {self.modelo}"
  
class Moto(Automovil):
  def describir(self):
    return f"Moto: {self.marca} {self.modelo}"
  
def describir_vehiculo(vehiculo): # Polimorfismo
  print(vehiculo.describir())
  
coche = Coche("Toyota", "Corolla")
moto = Moto("Honda", "CBR")

describir_vehiculo(coche)
describir_vehiculo(moto)