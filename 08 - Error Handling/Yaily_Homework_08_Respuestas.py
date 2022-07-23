'''
1) Con la clase creada en el módulo 7, tener en cuenta diferentes casos en que el código 
pudiera arrojar error. Por ejemplo, en la creación del objeto recibimos una lista de números 
enteros pero ¿qué pasa si se envía otro tipo de dato?

'''

from traitlets import Instance


class AnalMatListNum():
    def __init__(self, listNum: list):
        # Si no es una lista el paramentro de entrada que devuelva un error
        if not isinstance(listNum, list):
            raise TypeError('The entrance parameter must be a list')
        self.listNum = listNum
    

    # Método verificar si es primo

    def YesOrNoPrimo(self):
        listNumPrimos = []
        listIsNumPrimos = []
        for number in self.listNum:
            # Si no es un entero el elemento de la lista arroja un error
            if not isinstance(number, int):
                return(listIsNumPrimos,listNumPrimos)
                raise TypeError('The elements in the argument list must be the type int')
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
        bandParametros = 0
        try:
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
                        bandParametros = 1
                        break
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
                        bandParametros = 1
                        break
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
                        bandParametros = 1
                        listTempCnvert.append('void')
                        break
                else:
                    bandParametros = 1
                    listTempCnvert.append('void')
                    break
            if bandParametros == 1:
                print("\n NO se encontró una opción válida para alguno de los parámetros de entrada")
            print("Las opciones permitidas para los mismos son: celsius, kelvin y farenheit")
        except TypeError:
            print("No se permiten datos de tipo string")
        return(listTempCnvert)

   
    # Método factorial de un número

    def factorial (self):
        listFactorialNum = []
        for number in self.listNum:
            try:
                if number == 1:
                    factorialNum = 1
                elif (number > 1):
                    # Si el elemento de la lista no es un entero arroja error
                    assert type(number) == int, 'NO se permiten datos de tipo FLOAT en la lista'
                    cont = 2
                    factorialNum = 1
                    while cont <= number:
                        factorialNum = factorialNum * cont
                        cont += 1
                else:
                    factorialNum = 'No válido'
                listFactorialNum.append(factorialNum)
            except TypeError:
                listFactorialNum = 'Void'
                print("el tipo de datos no es adecuado")
                break
        return(listFactorialNum)

print("*********************************************************************")
'''
# Probando los métodos de la clase
#listNumber = list(range(1,11))# Lista ok con numeros enteros
listNumber = [5,3,4]
unidadMedidaOrigen = 'farenhet'
unidadMedidaDestino = 'kelvin'
print(AnalMatListNum(listNumber).convMedidTemp(unidadMedidaOrigen,unidadMedidaDestino))

'''

print("*********************************************************************")

'''
3) Importar el modulo "unittest" y crear los siguientes casos de pruebas sobre la clase 
utilizada en el punto 2<br>:
Creacion del objeto incorrecta<br>
Creacion correcta del objeto<br>
Metodo valor_modal()<br>

Se puede usar "raise ValueError()" en la creación de la clase para verificar el error.
Investigar sobre esta funcionalidad.

'''
import unittest

class CajaNegraTest(unittest.TestCase):
    # Definiendo los casos de prueba para detectar si los objetos se crean adecuadamente o no
    def test_objCorrect(self):
        #Defino los parametros de entrada
        listNumber = [1, 2, 3, 4]
        # Creo el objeto o llamo la función
        listNumberAnal = AnalMatListNum(listNumber)
        # comparo los parametros que deben ser iguales
        self.assertEqual(listNumber, listNumberAnal.listNum)
        
    def test_objIncorrect(self):
        listNumber = 'h'
        self.assertRaises(TypeError, AnalMatListNum, listNumber)
        
# Pido info de los test en base a los casos de prueba
unittest.main(argv=[''],verbosity=2,exit=False)

# listNumber = 'h'
# listNumberAnal = AnalMatListNum(listNumber)

print("*********************************************************************")

'''
4) Probar una creación incorrecta y visualizar la salida del "raise"
# COMENTAR ESTA ACTIVIDAD PARA PODER EJECUTAR EL TEST

'''
'''
#Defino los parametros de entrada
listNumber = 3.2
# Creo el objeto o llamo la función
print("\n Visualizando el error programado porque no se crea el objeto ya que el parametro de entrada NO es una lista")
print("\n")
listNumberAnal = AnalMatListNum(listNumber)
'''

print("*********************************************************************")