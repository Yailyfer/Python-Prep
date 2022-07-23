'''
8) Crear un archivo .py aparte y ubicar allí la clase generada en el punto anterior. 
Luego realizar la importación del módulo y probar alguna de sus funciones

        7) Es necesario que la clase creada en el punto 5 contenga una lista, 
        sobre la cual se aplquen las funciones incorporadas

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
