#!/usr/bin/python3

class Rectangulo:
  
  def __init__(self, ancho, alto):
    self.ancho = ancho
    self.alto = alto
    
  # @property - Se usa para indicar que se va a definir una propiedad.
  @property
  def area(self):
    return self.ancho * self.alto

  # __str__ : que permite retornar una cadena de caracteres para identificar al objeto
  def __str__(self):
    return f"\n[+] Propiedades del rectangulo: [Ancho: {self.ancho}][Alto: {self.alto}]"
  
  # __eq__ : que permite comparar dos objetos de la misma clase y calcular si son equivalentes.
  def __eq__(self, otro):
    return self.ancho == otro.ancho and self.alto == otro.alto
  
rect1 = Rectangulo(20, 31)
rect2 = Rectangulo(40, 12)

print(rect1)
print(f"\n[+] El área es {rect1.area}")
print(f"\n[+] ¿Son iguales? -> {rect1 == rect2}")