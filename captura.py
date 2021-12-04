import pyautogui
import pynput
import os
import time

print(" LARGAMOS EL PROGRAMA PRINCIPAL ")
print("Estamos agregando una rama de prueba")
print("ESTOY PARA MEJORAR EL CODIGO EN RALIDAD VER DE EMPEZAR A EJECUTAR ALGO")

#Haremos un ciclo para salvar mas de una imagen.
#INGRESO DE NOMBRE DE ARCHIVO A SALVAR
while True:
  nombre=input("Ingrese el nombre del archivo a salvar sin extension [mipantalla]: ")
  # En caso de no dar nombre el defalul sera mipantalla
  if (nombre==""):
    nombre="mipantalla"

  # CAPTURADOR DE PANTALLA SALVARA EN ARCHIVO con nombre en directorio de trabajo
  # En esto no estoy asignando region a salvar sino que es toda la pantalla
  pyautogui.alert("Posicionese en visualizacion deseada")
  time.sleep(.5)
  pyautogui.screenshot(nombre+".png")
  continuar=input("Desea salvar nueva pantalla? [si]")
  
  if(continuar.lower()=="no"):
    break
  


