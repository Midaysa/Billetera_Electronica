'''
Created on 1 feb. 2017

@author: Midaysa
'''
from ElectronicWallet import BilleteraElectronica, Persona, Debito, Persona, Credito
import unittest


class TestElectronicWallet(unittest.TestCase):


    def testPinErrado(self):
        with self.assertRaises(ValueError) as context:
            nuevo_debito = Debito(40, '900464456')
            pedro = Persona('Pedro', 'Camejo', 1715630, '12345')
            BilleteraElectronica('23417', pedro).consumir(nuevo_debito)
            
        self.assertTrue('El PIN ingresado no coincide con el del usuario' in str(context.exception))
        

    def testPinCorrecto(self):
        nuevo_debito = Debito(40, '90013422')
        pedro = Persona('Pedro', 'Camejo', 1715630, '12345')
        pedro_billetera = BilleteraElectronica('12345', pedro)
        nuevo_credito = Credito(100, '94320110')
        pedro_billetera.recargar(nuevo_credito)
        pedro_billetera.consumir(nuevo_debito)
            
        self.assertEqual(pedro_billetera.saldo(), 60)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()