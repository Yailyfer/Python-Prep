# Importante: No modificar ni el nombre ni los argumetos que reciben las funciones, sólo deben escribir
# código dentro de las funciones ya definidas.

from ast import Raise
from math import factorial
from pyparsing import null_debug_action


def Factorial(numero):
    '''
    Esta función devuelve el factorial del número pasado como parámetro.
    En caso de que no sea de tipo entero y/o sea menor que 1, debe retornar nulo.
    Recibe un argumento:
        numero: Será el número con el que se calcule el factorial
    Ej:
        Factorial(4) debe retornar 24
        Factorial(-2) debe retornar nulo
    '''
    #Tu código aca:
    # Método factorial de un número
    try:
        if numero == 1:
            factorialNum = 1
        elif (numero > 1):
            # Si el elemento de la lista no es un entero arroja error
            if not isinstance(numero, int):
                factorialNum = None
            else:
                cont = 2
                factorialNum = 1
                while cont <= numero:
                    factorialNum = factorialNum * cont
                    cont += 1
        else:
            factorialNum = None
    except TypeError:
        factorialNum = None
    return(factorialNum)

print(Factorial(1))


def EsPrimo(valor):
    '''
    Esta función devuelve el valor booleano True si el número reibido como parámetro es primo, de lo 
    contrario devuelve False..
    En caso de que el parámetro no sea de tipo entero debe retornar nulo.
    Recibe un argumento:
        valor: Será el número a evaluar
    Ej:
        EsPrimo(7) debe retornar True
        EsPrimo(8) debe retornar False
    '''
    #Tu código aca:
    # Si no es un entero el elemento de la lista arroja un error
    if not isinstance(valor, int):
        isNumPrimos = None
    else:
        flatPrimo = 1
        divisor = 2
        while divisor <= round(abs(valor) / 2):
            if abs(valor) % divisor == 0:
                flatPrimo = 0
                break
            divisor += 1
        if flatPrimo == 1 and valor != 0:
            isNumPrimos = True # Indica que SI es primo 
        else:
            isNumPrimos = False # Indica que NO es primo
    return(isNumPrimos)
    
def ClaseAnimal(especie, color):
    '''
    Esta función devuelve un objeto instanciado de la clase Animal, 
    la cual debe tener los siguientes atributos:
        Edad    (Un valor de tipo de dato entero, que debe inicializarse en cero)
        Especie (Un valor de tipo de dato string)
        Color   (Un valor de tipo de dato string)
    y debe tener el siguiente método:
        CumplirAnios  (este método debe sumar uno al atributo Edad y debe devolver ese valor)
    Recibe dos argumento:
        especie: Dato que se asignará al atributo Especie del objeto de la clase Animal
        color: Dato que se asignará al atributo Color del objeto de la clase Animal
    Ej:
        a = ClaseAnimal('perro','blanco')
        a.CumpliAnios() -> debe devolver 1
        a.CumpliAnios() -> debe devolver 2
        a.CumpliAnios() -> debe devolver 3
    '''
    #Tu código aca:
    class Animal:
        def __init__(self, especie, color):
            self.especie = especie
            self.color = color
            self.edad = 0

        # Definiendo el método 
        def CumplirAnios(self):
            self.edad += 1
            return self.edad

    animalTest = Animal(especie, color)  
    return animalTest 