import os

# Mostrando el tamaño del archivo
tamaño_MB = round(os.path.getsize("clase09_ej3_Yaily.cvs")/1024,2)
print(tamaño_MB)

# Creando una carpeta nueva
#os.makedirs("clase09_montañas_altas_Yaily")

#Moviendo el fichero clase09_ej3_Yaily a la carpeta creada anteriormente
#os.system()
os.system('copy clase09_ej3_Yaily.cvs clase09_montañas_altas_Yaily')

# Listar el contenido de la carpeta 
contenido = os.listdir('./clase09_montañas_altas')
print(contenido)