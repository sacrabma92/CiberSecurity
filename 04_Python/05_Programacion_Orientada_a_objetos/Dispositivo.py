##!/usr/bin/python3

class Dispositivo:
  def __init__(self, modelo):
    self.modelo = modelo

  def escaner_vulnerabilidades(self):
    raise NotImplementedError("Este metodo debe de ser definido para el resto de subclases existentes")
  
class Ordenador(Dispositivo):
  def escaner_vulnerabilidades(self):
    return f"[+] Analaisis de vulnerabilidades concluido: Actualizacion de software necesaria, multiples desactualizaciones de software detectados"
  
class Router(Dispositivo):
  def escaner_vulnerabilidades(self):
    return f"[+] Analaisis de vulnerabilidades concluido: Multiples puertos criticos detectados como abuertos, es recomendable cerrar estos puertos"
  
class TelefonoMovil(Dispositivo):
  def escaner_vulnerabilidades(self):
    return f"[+] Analaisis de vulnerabilidades concluido: Multiples aplicaciones detectadas con permisos excesivos"
  
def realizar_escaneo(dispositivo):
  print(dispositivo.escaner_vulnerabilidades())
  
pc = Ordenador("Dell XPS")
router = Router("Tp_link Archer C50")
movil = TelefonoMovil("Samsung Galaxy S21")

realizar_escaneo(pc)
realizar_escaneo(router)
realizar_escaneo(movil)