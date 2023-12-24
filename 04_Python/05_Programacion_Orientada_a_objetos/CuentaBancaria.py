#!/usr/bin/python3

class CuentaBancaria:
  
  def __init__(self, cuenta, nombre, dinero=0):
    self.cuenta = cuenta
    self.nombre = nombre
    self.dinero = dinero
  
  def depositar_dinero(self, dinero): # CuentaBancaria.depositar_dinero(carlos)
    self.dinero += dinero
    
    return f"\n[+] Se han depositado {dinero} euros, actualmente el balance de la cuenta es de {self.dinero} pesos"
  
  def retirar_dinero(self, dinero):
    if dinero > self.dinero:
      return f"\n[!] Operación denegada: Fondos Insuficientes\n"
    
    self.dinero -= dinero # self.dinero = self.dinero - dinero
    
    return f"\n[+] Se han depositado {dinero} pesos, actualmente el balance de la cuenta es de {self.dinero} pesos"
  
carlos = CuentaBancaria("00000001", "Carlos Ramirez", 500)
print(carlos.depositar_dinero(500))
print(carlos.retirar_dinero(900))