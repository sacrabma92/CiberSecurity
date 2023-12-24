#!/usr/bin/python3

class Estudiantes:
  estudiantes = []
  
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad
    
    Estudiantes.estudiantes.append(self)
    
  @staticmethod
  def es_mayor_de_edad(edad):
    return edad >= 18
  
  @classmethod
  def crear_estudiante(cls, nombre, edad):
    if cls.es_mayor_de_edad(edad):
      return cls(nombre, edad)
    else:
      print(f"\n[!] Error: El estudiante {nombre} es menor de dedad")
      
  @staticmethod
  def mostrar_estudiantes():
    for i, estudiante in enumerate(Estudiantes.estudiantes):
      print(f"\t[+] Estudiante numero [{i+1}]: {estudiante.nombre}")
      
Estudiantes.crear_estudiante("Hackermate", 32)
Estudiantes.crear_estudiante("Dxz", 31)
Estudiantes.crear_estudiante("Xerosex", 20)
Estudiantes.crear_estudiante("Hackvis", 15)
Estudiantes.crear_estudiante("Lobotect", 9)

print("\n[i] Listando los estudiantes existentes:\n")

Estudiantes.mostrar_estudiantes()
