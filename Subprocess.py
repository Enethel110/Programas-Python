from subprocess import Popen 
import time 

# Ejecuta el comando 'notepad.exe' para abrir el Bloc de notas en Windows
for j in range (0,10):
    process = Popen(['notepad.exe'])

# Espera a que el proceso hijo termine y obtiene su código de salida
process.wait()

print("Proceso completado")


#Popen('python C:\\Users\\shiol\\Downloads\\MensajesPruebas.py')
