'''
6) Agregar casos de pruebas para el método verifica_primos() realizando el cambio en la clase, 
para que devuelva una lista de True o False en función de que el elemento en la posisicón sea 
o no primo

'''

import Yaily_Homework_08_Respuestas as funcion
import unittest

class CajaNegraTest(unittest.TestCase):
    # Defino los casos de prueba
    def test_caso1 (self):
        # Defino las variables
        listNum = list(range(1,11))
        # Creo el objeto
        primosSiNoObj = funcion.AnalMatListNum(listNum)
        # Llamo a la funcion
        primosSiNo = primosSiNoObj.YesOrNoPrimo()
        resultBool = primosSiNo[0]
        # Evaluo la igualdad de resultBool con el resultado esperado [True,True,True,False,True,False,True,False,False,False]
        self.assertEqual(resultBool,[True,True,True,False,True,False,True,False,False,False])

    def test_caso2 (self):
        # Defino las variables
        listNum = [2,21,29,34,31,46,17,0]
        # Creo el objeto
        primosSiNoObj = funcion.AnalMatListNum(listNum)
        # Llamo a la funcion
        primosSiNo = primosSiNoObj.YesOrNoPrimo()
        resultBool = primosSiNo[0]
        # Evaluo la igualdad de resultBool con el resultado esperado [True,True,True,False,True,False,True,False,False,False]
        self.assertEqual(resultBool,[True,False,True,False,True,False,True,False])

    def test_caso3 (self):
        # Defino las variables
        listNum = [2,21,29,34,31,46,17,'hola']
        # Creo el objeto
        primosSiNoObj = funcion.AnalMatListNum(listNum)
        # Llamo a la funcion
        primosSiNo = primosSiNoObj.YesOrNoPrimo()
        resultBool = primosSiNo[0]
        # Evaluo la igualdad de resultBool con el resultado esperado [True,True,True,False,True,False,True,False,False,False]
        self.assertEqual(resultBool,[True,False,True,False,True,False,True])
        #self.assertRaises(TypeError, funcion.AnalMatListNum.YesOrNoPrimo(),listNum)

    
    def test_caso4 (self):
        # Defino las variables
        listNum = [2,21,'otro',34,31,46,17,'hola']
        # Creo el objeto
        primosSiNoObj = funcion.AnalMatListNum(listNum)
        # Llamo a la funcion
        primosSiNo = primosSiNoObj.YesOrNoPrimo()
        resultBool = primosSiNo[0]
        # Evaluo la igualdad de resultBool con el resultado esperado [True,True,True,False,True,False,True,False,False,False]
        self.assertEqual(resultBool,[True,False])



# Pido info de los test en base a los casos de prueba
unittest.main(argv=[''],verbosity=2,exit=False)
        