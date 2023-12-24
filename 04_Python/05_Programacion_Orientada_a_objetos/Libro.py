##!/usr/bin/python3

class Libro:
  
  IVA = 0.19
  
  def __init__(self, titulo, autor, precio):
    self.titulo = titulo
    self.autor = autor
    self.precio = precio
  
  @staticmethod # Decorador
  def es_bestseller(total_ventas):
    return total_ventas > 5000
  
  @classmethod
  def precio_con_iva(cls, precio):
    return precio + precio * cls.IVA
  
  #Herencia
class LibroDigital(Libro):
  
  IVA = 0.12
  
mi_libro = Libro("¿Como ser un lammer d elos de verdad?", "Marcelo Vasques", 12.3)
mi_libro_digital = LibroDigital("Inicio de un Lammer", "Marcelo Vasques", 9)

print(f"\n[+] El precio del libro con IVA incluido es de {Libro.precio_con_iva(mi_libro.precio)}")
print(f"\n[+] El precio del libro digital con IVA incluido es de {LibroDigital.precio_con_iva(mi_libro_digital.precio)}")