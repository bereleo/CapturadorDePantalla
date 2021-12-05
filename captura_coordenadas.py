import pyautogui
import pynput
from pynput import keyboard
import os
import time

# PRECAUCION AL HACERLO EJECUTABLE PORQUE PUEDEN NO CARGAR LAS LIBRERIAS OCULTAS Y NO EJECUTARSE CORRECTAMENTE, USAR:
# PyInstaller your_program.py --onefile  --hidden-import=pynput.keyboard._win32 --hidden-import=pynput.mouse._win32


#Defino las fucniones a ejecutarse cuando tomo coordenada superior izquierda

def presiono_ctrl_shift_a():
  # las coordenadas deben ser globales para transmitirla de funcion en funcion
  global aaa
  # leo las coordenadas y las cargo en la tupla aaa
  aaa=pyautogui.position()
  print(" Coordenadas superior izquierda seleccionada: "+str(aaa))
  
def presiono_ctrl_shift_z():
  global ii
  global zzz
  global nombre
  ii=1+ii
  zzz=pyautogui.position()
  print(" Coordenadas inferior derecha seleccionada: "+str(zzz))
  mapa=(aaa[0],aaa[1],zzz[0]-aaa[0],zzz[1]-aaa[1])
  print("Coordenadas de captura: "+str(aaa)+", "+str(zzz))
  pyautogui.screenshot(nombre+str(ii)+".png",region=mapa)  
  print("Se salvo en su directorio archivo de captura: "+nombre+str(ii)+".png")
  print("")
  print("    Reingrese coordenadas de interes para nueva captura")

def presiono_salir():
  print("Gracias por usar este programa de captura de pantalla")
  time.sleep(1)
  os.exit(0)
  
  
  
## INICIO DEL PROGRAMA
print("USO DE TECLAS:")
print(" ")
print("    COORDENADA SUPERIOR IZQUIERDA: <ctrl>+<shift>+a ")
print("    COORDENADA INFERIOR DERECHA: <ctrl>+<shift>+z ")
print("    SALIR: <ctrl>+x ")
print(" ")
print("... use combinacion teclas antes mencionada cuando quiera capturar regiones de pantalla ....")
print(" ")

## cuado largue el programa las coordenadas deberan ser globales por eso en las funciones las coloco como globales
aaa=(0,0)
zzz=(10,10)
ii=0
nombre=input("Ingrese nombre de archivo a salvar: ")

if (nombre.strip()==""):
  nombre="mipantalla"

teclasCalientes={"<ctrl>+<shift>+a":presiono_ctrl_shift_a, "<ctrl>+<shift>+z":presiono_ctrl_shift_z,"<ctrl>+x":presiono_salir}

#PARA SELECCIONAR REGIONES QUEDA EN BUCLE INFINITO ESPERANDO COMBINACION DE TECLAS SI NO SALGO EXPRESAMENTE DEL PROGRAMA
with keyboard.GlobalHotKeys(teclasCalientes) as escucha:
  escucha.join()
