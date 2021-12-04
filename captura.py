import pyautogui
import pynput

print(" LARGAMOS EL PROGRAMA PRINCIPAL ")
print("Estamos agregando una rama de prueba")
print("ESTOY PARA MEJORAR EL CODIGO EN RALIDAD VER DE EMPEZAR A EJECUTAR ALGO")

#INGRESO DE NOMBRE DE ARCHIVO A SALVAR
nombre=input("Ingrese el nombre del archivo a salvar sin extension [mipantalla]: ")
# En caso de no dar nombre el defalul sera mipantalla
if (nombre==""):
  nombre="mipantalla"

# CAPTURADOR DE PANTALLA SALVARA EN ARCHIVO con nombre en directorio de trabajo
pyautogui.screenshot(nombre+".png")

print("me vacunaron...")
