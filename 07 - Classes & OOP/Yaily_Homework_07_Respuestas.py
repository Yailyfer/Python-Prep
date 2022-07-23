print("\n ***********************************************************************")
print("\n _________ INFORMACION DE VEHICULOS _____________________")
'''

1) Crear la clase vehículo que contenga los atributos:<br>
Color<br>
Si es moto, auto, camioneta ó camión<br>
Cilindrada del motor

'''


class Vehículos:
    # El constructor que se ejecuta cuando se instancia el objeto
    def __init__(self, color, cilindraje,tipo = ['moto','auto','camioneta','camión']):
        self.color = color
        self.tipo = tipo
        self.cilindraje = cilindraje


    '''
    2) A la clase Vehiculo creada en el punto 1, agregar los siguientes métodos:<br>
        Acelerar<br>
        Frenar<br>
        Doblar<br>
    
    '''
    def descripcion(self):
        print(f"\n Soy un(una)",self.tipo,"de color",self.color,"y cilindraje del motor de", self.cilindraje,"caballos de fuerza")

    def acelerar(self):
        print("EStoy ACELERANDO")

    def frenar(self):
        print("EStoy FRENANDO")

    def doblar(self):
        print("EStoy DOBLANDO")

    '''
    
    4) Agregar a la clase Vehiculo, un método que muestre su estado, es decir, a que velocidad 
    se encuentra y su dirección. Y otro método que muestre color, tipo y cilindrada
    
    '''
    def estado(self,velocity,direction):
        print(f"Me encuentro a una velocidad de",velocity,"Km/h y en dirección al(a)", direction)

'''
3) Instanciar 3 objetos de la clase vehículo y ejecutar sus métodos, probar luego el resultado

'''
# Instanciando los objetos de la clase vehículos
moto = Vehículos('rojo',200,'moto')
camioneta = Vehículos('verde',180,'camioneta')
auto = Vehículos('azul',350,'auto')
# Ejecutando los métodos de la clase
moto.acelerar()
moto.doblar()
moto.frenar()
moto.descripcion()
moto.estado(200,'Norte')
camioneta.descripcion()
camioneta.estado(80,'Carretera Central')
auto.descripcion()
auto.estado(90,'Guanajuato')

print("\n ***********************************************************************")
print("\n _________ ANALISIS DE NUMEROS _____________________")

'''

5) Crear una clase que permita utilizar las funciones creadas en la práctica del módulo 6<br>
Verificar Primo<br>
Valor modal<br>
Conversión grados<br>
Factorial<br>

'''

class AnalMatNum():
    def __init__(self, number):
        self.number = number

    # Método verificar si es primo

    def YesOrNoPrimo(self):
        flatPrimo = 1
        divisor = 2
        while divisor <= round(abs(self.number) / 2):
            if abs(self.number) % divisor == 0:
                flatPrimo = 0
                break
            divisor += 1
        if flatPrimo == 1 and self.number != 0:
            print(f"\n El número",self.number,"SÍ es primo")
            return(True) # Indica que SI es primo
        elif (flatPrimo == 0 and self.number != 0) or self.number == 0:
            print(f"\n El número",self.number,"NO es primo")
            return(False) # Indica que NO es primo

    # Método conversión de escalas de temperatura

    def convMedidTemp (self, unidadMedidaOrig, unidadMedidaDest):
        if unidadMedidaOrig == 'celsius':
            if unidadMedidaDest == 'farenheit':
                tempCnvert = (self.number * 9 / 5) + 32
                print(f"\n La temperatura de Celsius a Farenheit es:", round(tempCnvert))
            elif unidadMedidaDest == 'kelvin':
                tempCnvert = self.number + 273.15
                print(f"\n La temperatura de Celsius a Kelvin es:", round(tempCnvert))
            else:
                print("\n No se encontró una opción válida")
        elif unidadMedidaOrig == 'farenheit':
            tempFarenToCel = (self.number - 32) * 5 / 9
            if unidadMedidaDest == 'celsius':
                tempCnvert = tempFarenToCel
                print(f"\n La temperatura de Farenheit a Celsius es:", round(tempFarenToCel))
            elif unidadMedidaDest == 'kelvin':
                tempCnvert = tempFarenToCel + 273.15
                print(f"\n La temperatura de Farenheit a Kelvin es:", round(tempCnvert))
            else:
                print("\n No se encontró una opción válida")
        elif unidadMedidaOrig == 'kelvin':
            tempKelToCel = self.number - 273.15
            if unidadMedidaDest == 'celsius':
                tempCnvert = tempKelToCel
                print(f"\n La temperatura de Kelvin a Celsius es:", round(tempKelToCel))
            elif unidadMedidaDest == 'farenheit':
                tempCnvert = (tempKelToCel * 9 / 5) + 32
                print(f"\n La temperatura de Kelvin a Farenheit es:", round(tempCnvert))
            else:
                print("\n No se encontró una opción válida")
        else:
            print("\n No se encontró una opción válida")
        return(tempCnvert)

   
    # Método factorial de un número

    def factorial (self):
        if self.number == 1:
            factorialNumNew = 1
        elif (self.number > 1):
            cont = 2
            factorialNumNew = 1
            while cont <= self.number:
                factorialNumNew = factorialNumNew * cont
                cont += 1
        else:
            factorialNumNew = 'No válido'
        return(factorialNumNew)


'''
6) Probar las funciones incorporadas en la clase del punto 5

'''
# Programa principal para probar los métodos de la clase AnalMatNum
# Definiendo variables
number = -46
unidadMedidaOrigen = 'kelvin'
unidadMedidaDestino = 'farenheit'
# Instanciando el objeto de la clase AnalMatNum
numberObj = AnalMatNum(number)
# Llamada de los métodos de la clase AnalMatNum por el OBJETO numberObj
numberObj.YesOrNoPrimo()
numFactorial = numberObj.factorial()
print(f"\n El factorial de",number,"es: ",numFactorial)
numberObj.convMedidTemp(unidadMedidaOrigen,unidadMedidaDestino)

print("\n ***********************************************************************")
print("\n _________ ANALISIS DE NUMEROS EN UNA LISTA _____________________")

'''
7) Es necesario que la clase creada en el punto 5 contenga una lista, 
sobre la cual se aplquen las funciones incorporadas

'''

'''
class AnalMatListNum():
    def __init__(self, listNum):
        self.listNum = listNum

    # Método verificar si es primo

    def YesOrNoPrimo(self):
        listNumPrimos = []
        listIsNumPrimos = []
        for number in self.listNum:
            flatPrimo = 1
            divisor = 2
            while divisor <= round(abs(number) / 2):
                if abs(number) % divisor == 0:
                    flatPrimo = 0
                    break
                divisor += 1
            if flatPrimo == 1 and number != 0:
                print(f"\n El número",number,"SÍ es primo")
                listNumPrimos.append(number)
                listIsNumPrimos.append(True)
                #return(True) # Indica que SI es primo
            elif (flatPrimo == 0 and number != 0) or number == 0:
                print(f"\n El número",number,"NO es primo")
                listIsNumPrimos.append(False)
                #return(False) # Indica que NO es primo
        return(listIsNumPrimos,listNumPrimos)

    # Método conversión de escalas de temperatura

    def convMedidTemp (self, unidadMedidaOrig, unidadMedidaDest):
        listTempCnvert = []
        for number in self.listNum: 
            if unidadMedidaOrig == 'celsius':
                if unidadMedidaDest == 'farenheit':
                    tempCnvert = (number * 9 / 5) + 32
                    listTempCnvert.append(tempCnvert)
                    print(f"\n La temperatura de Celsius a Farenheit es:", round(tempCnvert))
                elif unidadMedidaDest == 'kelvin':
                    tempCnvert = number + 273.15
                    listTempCnvert.append(tempCnvert)
                    print(f"\n La temperatura de Celsius a Kelvin es:", round(tempCnvert))
                else:
                    print("\n No se encontró una opción válida")
            elif unidadMedidaOrig == 'farenheit':
                tempFarenToCel = (number - 32) * 5 / 9
                if unidadMedidaDest == 'celsius':
                    tempCnvert = tempFarenToCel
                    listTempCnvert.append(tempCnvert)
                    print(f"\n La temperatura de Farenheit a Celsius es:", round(tempFarenToCel))
                elif unidadMedidaDest == 'kelvin':
                    tempCnvert = tempFarenToCel + 273.15
                    listTempCnvert.append(tempCnvert)
                    print(f"\n La temperatura de Farenheit a Kelvin es:", round(tempCnvert))
                else:
                    print("\n No se encontró una opción válida")
            elif unidadMedidaOrig == 'kelvin':
                tempKelToCel = number - 273.15
                if unidadMedidaDest == 'celsius':
                    tempCnvert = tempKelToCel
                    listTempCnvert.append(tempCnvert)
                    print(f"\n La temperatura de Kelvin a Celsius es:", round(tempKelToCel))
                elif unidadMedidaDest == 'farenheit':
                    tempCnvert = (tempKelToCel * 9 / 5) + 32
                    listTempCnvert.append(tempCnvert)
                    print(f"\n La temperatura de Kelvin a Farenheit es:", round(tempCnvert))
                else:
                    print("\n No se encontró una opción válida")
                    listTempCnvert.append('void')
            else:
                print("\n No se encontró una opción válida")
                listTempCnvert.append('void')
        return(listTempCnvert)

   
    # Método factorial de un número

    def factorial (self):
        listFactorialNum = []
        for number in self.listNum:
            if number == 1:
                factorialNum = 1
            elif (number > 1):
                cont = 2
                factorialNum = 1
                while cont <= number:
                    factorialNum = factorialNum * cont
                    cont += 1
            else:
                factorialNum = 'No válido'
            listFactorialNum.append(factorialNum)
        return(listFactorialNum)


# Programa principal para probar los métodos de la clase AnalMatListNum
# Definiendo variables
listNum = list(range(1,11))
print("---------------------------------------------------------")
print(f"\n Esta es la lista de números a analizar:",listNum)
print("---------------------------------------------------------")
unidadMedidaOrigen = 'farenheit'
unidadMedidaDestino = 'celsius'
# Instanciando el objeto de la clase AnalMatNum
listNumberObj = AnalMatListNum(listNum)
# Llamada de los métodos de la clase AnalMatListNum por el OBJETO listNumberObj
ListNumObjPrimos = listNumberObj.YesOrNoPrimo()
ListNumObjFactorial = listNumberObj.factorial()
print(f"\n El factorial de la lista de números",listNum,"es: ",ListNumObjFactorial)
ListNumObjTemp = listNumberObj.convMedidTemp(unidadMedidaOrigen,unidadMedidaDestino)
print("\n ----------------------------------------------------------------------------------")
# Imprimiendo los valores devueltos por la llamada de los metodos de la clase 
print("\n Estos son los valores de las varibles devueltas por los METODOS de la clase AnalMatListNum")
print("\n ----------------------------------------------------------------------------------")
print(f"Lo que devuelve el método de números primos:",ListNumObjPrimos)
print("\n ----------------------------------------------------------------------------------")
print(f"Lo que devuelve el método de Facorial:",ListNumObjFactorial)
print("\n ----------------------------------------------------------------------------------")
print(f"Lo que devuelve el método de conversion de escalas de temperatura:",ListNumObjTemp)

print("\n ***********************************************************************")
'''

# Programa principal para probar los métodos de la clase AnalMatListNum
# Importando  el modulo 
from analMatListNum import *
#import analMatListNum # forma opcional de importacion
# Definiendo variables
listNum = list(range(10,21))
print("---------------------------------------------------------")
print(f"\n Esta es la lista de números a analizar:",listNum)
print("---------------------------------------------------------")
unidadMedidaOrigen = 'farenheit'
unidadMedidaDestino = 'kelvin'
# Instanciando el objeto de la clase AnalMatNum
listNumberObj = AnalMatListNum(listNum)
#listNumberObj = analMatListNum.AnalMatListNum(listNum) # Otra opcion correspondiente a la forma
                                                        # opcional de importacion
# Llamada de los métodos de la clase AnalMatListNum por el OBJETO listNumberObj
ListNumObjPrimos = listNumberObj.YesOrNoPrimo()
ListNumObjFactorial = listNumberObj.factorial()
print(f"\n El factorial de la lista de números",listNum,"es: ",ListNumObjFactorial)
ListNumObjTemp = listNumberObj.convMedidTemp(unidadMedidaOrigen,unidadMedidaDestino)

'''
print("\n ----------------------------------------------------------------------------------")
# Imprimiendo los valores devueltos por la llamada de los metodos de la clase 
print("\n Estos son los valores de las varibles devueltas por los METODOS de la clase AnalMatListNum")
print("\n ----------------------------------------------------------------------------------")
print(f"Lo que devuelve el método de números primos:",ListNumObjPrimos)
print("\n ----------------------------------------------------------------------------------")
print(f"Lo que devuelve el método de Facorial:",ListNumObjFactorial)
print("\n ----------------------------------------------------------------------------------")
print(f"Lo que devuelve el método de conversion de escalas de temperatura:",ListNumObjTemp)
'''
print("\n ***********************************************************************")