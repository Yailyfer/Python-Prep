'''
1) Crear un script con el nombre "clase09_ej1.py" que reciba 3 parametros a elección,
 verificando que sean exactamente esa cantidad, y muestre como salida los parámetros recibidos

'''

import sys


print("Introduzca los datos solicitados en el siguiente orden: nombre, escuela y edad de su hijo")

if len(sys.argv) == 4:
    nombre = sys.argv[1]
    escuela = sys.argv[2]
    edad = int(sys.argv[3])
    print(f"El(La) niño(a)", nombre,"de", edad, "años de edad, iniciará el siguiente ciclo escolar en la escuela",escuela)

else:
    print("Introdujo un número de datos incorectos!!!")

print(f"Estamos trabajando con el fichero titulado: ", sys.argv[0])
