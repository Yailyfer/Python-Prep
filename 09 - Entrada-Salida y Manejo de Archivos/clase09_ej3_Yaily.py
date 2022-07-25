'''

3) Crear un archivo a partir de los datos presentes en el diccionario provisto. El cual debe 
contener en la primera fila el nombre de las claves y luego cada línea los elementos i-ésimos 
de las listas de valores contiguos y separados por coma ','. Este archivo debe llamarse 
clase09_ej3.csv

``` python
montañas = {'nombre':[  'Everest','K2','Kanchenjunga','Lhotse','Makalu',
                        'Cho Oyu','Dhaulagiri','Manaslu','Nanga Parbat','Annapurna I'],
            'orden':[1,2,3,4,5,6,7,8,9,10],
            'cordillera':['Himalaya','Karakórum','Himalaya','Himalaya','Himalaya'
                        ,'Himalaya','Himalaya','Himalaya','Karakórum','Himalaya'],
            'pais': ['Nepal','Pakistán','Nepal','Nepal','Nepal','Nepal','Nepal','Nepal',
                    'Pakistán','Nepal'],
            'altura':[8849,8611,8586,8516,8485,8188,8167,8163,8125,8091]}
```


'''

import os


print("Se muestran los datos en un fichero a partir del diccionario dado")

montañas = {'nombre':[  'Everest','K2','Kanchenjunga','Lhotse','Makalu',
                        'Cho Oyu','Dhaulagiri','Manaslu','Nanga Parbat','Annapurna I'],
            'orden':[1,2,3,4,5,6,7,8,9,10],
            'cordillera':['Himalaya','Karakórum','Himalaya','Himalaya','Himalaya'
                        ,'Himalaya','Himalaya','Himalaya','Karakórum','Himalaya'],
            'pais': ['Nepal','Pakistán','Nepal','Nepal','Nepal','Nepal','Nepal','Nepal',
                    'Pakistán','Nepal'],
            'altura':[8849,8611,8586,8516,8485,8188,8167,8163,8125,8091]}

nombresClaves = list(montañas.keys())

# Abro el fichero
fichero = open('clase09_ej3_Yaily.cvs', 'a')
# Creo la linea de encabezados
cont = 1
for clave in nombresClaves:
    if cont == len(nombresClaves):
        fichero.write(clave+'\n')
    else:
        fichero.write(clave+',')
    cont += 1


# Creo las lineas que voy a añadir en el fichero con los contenidos de cada key
for clave in range(len(montañas['nombre'])):
    fichero.write(montañas['nombre'][clave]+',')
    fichero.write(str(montañas['orden'][clave])+',')
    fichero.write(montañas['cordillera'][clave]+',')
    fichero.write(montañas['pais'][clave]+',')
    fichero.write(str(montañas['altura'][clave])+'\n')


# Cierro el fichero
fichero.close()

