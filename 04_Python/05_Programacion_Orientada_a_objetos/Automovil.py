###!/usr/bin/ppython3

class Automovil:
  
  def __init__(self, marca, modelo):
    self.marca = marca
    self.modelo = modelo
    
  @classmethod
  def deportivos(cls, marca):
    return cls(marca, "Deportivo")
  
  @classmethod
  def sean(cls, marca):
    return cls(marca, "Sean")
  
  def __str__(self):
    return f"La marca {self.marca} es un modelo {self.modelo}"
  
deportivoo = print(Automovil.deportivos("Ferrari"))
sean = print(Automovil.sean("Toyota"))