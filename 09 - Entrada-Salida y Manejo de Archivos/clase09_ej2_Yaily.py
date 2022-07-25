'''

2) Crear un script con el nombre "clase09_ej2.py2" que reciba como un valor de temperatura en 
grados centígrados, un valor de humedad y por último si llovio (Con True o False). Y que cada 
vez que sea invocado, cargue en el archivo provisto "clase09_ej2.csv" una marca de tiempo y esa 
información.

Para trabajar con tipos de datos relacionados con la medición del tiempo, como ser fechas,
horarios o marcas de tiempo se puede utilizar la clase *datetime* de python:

import datetime

x = datetime.datetime.now()
marca_de_tiempo = datetime.datetime.timestamp(objeto_datetime)
print("timestamp =", marca_de_tiempo)

'''

import sys
import datetime
import os


print("""Introduzca los datos solicitados en el siguiente orden: temperatura(grados centígrados), 
humedad relativa y si llovió (True) o no (False)""")

if len(sys.argv) == 4:
    temperatura = sys.argv[1]
    humedad = sys.argv[2]
    llovio = sys.argv[3]
    print(f"El día de hoy la temperatura es de", temperatura,"°C con una humedad del", humedad, "%")
    if bool(llovio) == True:
        print("Con lluvias")
    else:
        print("Sin lluvias")

    # Creo la marca de tiempo
    fechaActual = datetime.datetime.now()
    marcaDeTiempo = datetime.datetime.timestamp(fechaActual)
    # Creo la linea que voy a añadir en el fichero
    registroLinea = str(marcaDeTiempo)+','+temperatura+','+humedad+','+llovio
    # Abro el fichero y escribo en el
    fichero = open('clase09_ej2_Yaily.cvs', 'a')
    fichero.write(registroLinea+'\n')
    fichero.close()


else:
    print("Introdujo un número de datos incorectos!!!")
    print("La forma correcta es: clase09_ej2_Yaily.py 34 96 True")

print(f"Estamos trabajando con el fichero titulado: ", sys.argv[0])