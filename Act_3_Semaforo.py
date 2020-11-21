#Actividad 3: Realizar una funcion de Python para el funcionamiento del semáforo

#Importar librerias
import RPi.GPIO as GPIO
import time

#Definir los pines de salida
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)

rojo = 2
amarillo = 3
verde = 4

tiempocambio = 5

#Definir la funcion de semaforo
def semaforo():
    print('Ejecución del semaforo en proceso...')
    GPIO.output(rojo, True)
    time.sleep(tiempocambio)

    GPIO.output(verde, True)
    GPIO.output(rojo, False)
    time.sleep(tiempocambio)

    GPIO.output(amarillo, True)
    time.sleep(2)

    GPIO.output(amarillo, False)
    GPIO.output(verde, False)

#Bucle para semaforo    
for b in range(2):
    semaforo()

print('Limpieza de la configuracion del GPIO en proceso...')
GPIO.cleanup()
