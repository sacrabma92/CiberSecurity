#!/usr/bin/python3

class Calculadora:
  
  @staticmethod
  def suma(num1, num2):
    return num1 + num2
  
  @staticmethod
  def resta(num1, num2):
    return num1 - num2

  @staticmethod
  def multiplicacion(num1, num2):
    return num1 * num2
  
  @staticmethod
  def division(num1, num2):
    return num1 / num2 if num2 != 0 else f"\n[!] Error: No se puede dividir un numero entre cero \n"
  
print(Calculadora.suma(2,3))
print(Calculadora.resta(2,3))
print(Calculadora.multiplicacion(2,3))
print(Calculadora.division(2,5))