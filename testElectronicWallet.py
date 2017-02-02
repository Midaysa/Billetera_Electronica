'''
Create on 01/2/2017

@author: Midaysa Palacios
@author: Lalezka Duque
'''

#!/usr/bin/env python
# -⁻- coding: UTF-8 -*-
# -*- coding: utf-8 -*-

import unittest
from ElectronicWallet import *

class billeteraElectronicaTeste(unittest.TestCase):
    
    getcontext().prec = 15
    
    # Caso: Crear Billetera
    def testCrearBilletera(self):
        return
    
    # Caso: Recarga correcta
    def testRecargaCorrecta(self):
        return
    
    # Caso: Consumo correcto
    def testConsumoCorrecto(self):
        return
    
    # Caso: Recargas y consumos
    def testRecargasConsumos(self):
        return
        
    # Casos esquina
    # 2.- Crear billetera con pin incorrecto
    def testCrearBilleteraPinIncorrecto(self):
        return
    
    # 3.- Verificacion de fechas
    def testVerificacionFecha(self):
        return
    
    # 4.- Recarga y consumo con decimales pequeños
    def testRecargaConsumoDecimalesPequenos(self):
        return
    
    # 5.- Recarga y consumo negativos
    def testRecargaConsumoNegativos(self):
        return 
    
    # 6.- Nombres
    def testNombres(self):
        return
    
    # 7.- Apellidos
    def testApellidos(self):
        return
    
    # 8.- Nombres con caracteres especiales
    def testNombreCaracteresEspeciales(self):
        return
    
    # 9.- Apellidos con caracteres especiales
    def testApellidosCaracteresEspeciales(self):
        return
    
    # 10.- Consumo con otro tipo de datos distinto
    def testDatosConsumoErroneos(self):
        return
    
    # 11.- Datos de las persona con tipos de datos distintos
    def testDatosPersonaErroneos(self):
        return
    
    # 12.- Recarga con tipo de datos distinto
    def testDatosRecargaErroneos(self):
        return
    
    # Casos Frontera:
    # 1.- Recarga negativa
    def testRecargaNegativa(self):
        lalezka = Persona("Lalezka", "Duque", 23689465, "4545")
        miBilletera = BilleteraElectronica("4545", lalezka)
        micredito = Credito(-200, "3399")
        miBilletera.recargar(micredito)
        self.assertEquals(miBilletera.saldo(), Decimal(0))
        
    # 2.- Consumo negativo
    def testConsumoNegativo(self):
        lalezka = Persona("Lalezka", "Duque", 23689465, "4545")
        miBilletera = BilleteraElectronica("4545", lalezka)
        micredito = Credito(500, "3399")
        miBilletera.recargar(micredito)
        midebito = Debito(-200, "3679")
        miBilletera.consumir(midebito)
        self.assertEquals(miBilletera.saldo(), Decimal(500))
                          
    # 3.- Precision de la recarga
    def testRecargaDecimalesPequenos(self):
        lalezka = Persona("Lalezka", "Duque", 23689465, "4545")
        miBilletera = BilleteraElectronica("4545", lalezka)
        micredito = Credito(0.0000001, "5864")
        miBilletera.recargar(micredito)
        self.assertEquals(miBilletera.saldo(), Decimal(0)+Decimal(0.0000001))

    # 4.- Consumir con pin incorrecto
    def testConsumoPinIncorrecto(self):
        pedro = Persona("Pedro", "Camejo", 1715630, "12345")
        miBilletera = BilleteraElectronica("23417", pedro)
        micredito = Credito(80, "90013422")
        miBilletera.recargar(micredito)
        midebito = Debito(40, "900464456")
        miBilletera.consumir(midebito)
        self.assertEquals(miBilletera.saldo(), Decimal(80))
    
    # 5.- Precicion del consumo
    def testConsumoDecimalesPequenos(self):
        lalezka = Persona("Lalezka", "Duque", 23689465, "4545")
        miBilletera = BilleteraElectronica("4545", lalezka)
        micredito = Credito(200, "5864")
        miBilletera.recargar(micredito)
        midebito = Debito(0.00000001, "5864")
        miBilletera.consumir(midebito)
        self.assertEquals(miBilletera.saldo(), Decimal(200)-Decimal(0.00000001))
    
    # 6.- Recarga con el máximo entero (32 bits)
    def testRecargaMaxEntero(self):
        lalezka = Persona("Lalezka", "Duque", 23689465, "4545")
        miBilletera = BilleteraElectronica("4545", lalezka)
        micredito = Credito(245678901388, "5864")
        miBilletera.recargar(micredito)
        self.assertEquals(miBilletera.saldo(), Decimal(245678901388))
    
    # 6.- Recarga y consumo total
    def testRecargaConsumoTotal(self):
        lalezka = Persona("Lalezka", "Duque", 23689465, "4545")
        miBilletera = BilleteraElectronica("4545", lalezka)
        micredito = Credito(99, "5464")
        miBilletera.recargar(micredito)
        midebito = Debito(99, "6666")
        miBilletera.consumir(midebito)
        self.assertEquals(miBilletera.saldo(), Decimal(0))
    
    # 7.- Recarga cero
    def testRecargaCero(self):
        lalezka = Persona("Lalezka", "Duque", 23689465, "4545")
        miBilletera = BilleteraElectronica("4545", lalezka)
        micredito = Credito(99, "3764")
        miBilletera.recargar(micredito)
        micreditocero = Credito(0, "4565")
        miBilletera.recargar(micreditocero)
        self.assertEquals(miBilletera.saldo(), Decimal(99))
    
    # 8.- Consumir cero
    def testConsumoCero(self):
        lalezka = Persona("Lalezka", "Duque", 23689465, "4545")
        miBilletera = BilleteraElectronica("4545", lalezka)
        micredito = Credito(45, "1280")
        miBilletera.recargar(micredito)
        midebito = Debito(0, "3490")
        miBilletera.consumir(midebito)
        self.assertEquals(miBilletera.saldo(), Decimal(45))
    
    # Casos maliciosos
    # 1.- Consumo mayor que recarga
    def testConsumoMayorQueRecarga(self):
        lalezka = Persona("Lalezka", "Duque", 23689465, "4545")
        miBilletera = BilleteraElectronica("4545", lalezka)
        micredito = Credito(45, "1280")
        miBilletera.recargar(micredito)
        midebito = Debito(100, "3490")
        miBilletera.consumir(midebito)
        self.assertEquals(miBilletera.saldo(), Decimal(45))
    
    # 2.- Recarga entera y consumo decimal
    def testRecargaEnteraConsumoDecimal(self):
        lalezka = Persona("Lalezka", "Duque", 23689465, "4545")
        miBilletera = BilleteraElectronica("4545", lalezka)
        micredito = Credito(45, "1280")
        miBilletera.recargar(micredito)
        midebito = Debito(30.45, "3490")
        miBilletera.consumir(midebito)
        self.assertEquals(miBilletera.saldo(), Decimal(45)-Decimal(30.45))
    
    # 3.- Recarga decimal y consumo entero
    def testRecargaDecimalConsumoEntero(self):
        lalezka = Persona("Lalezka", "Duque", 23689465, "4545")
        miBilletera = BilleteraElectronica("4545", lalezka)
        micredito = Credito(10.66, "1280")
        miBilletera.recargar(micredito)
        midebito = Debito(5, "3490")
        miBilletera.consumir(midebito)
        self.assertEquals(miBilletera.saldo(), Decimal(0)+Decimal(10.66)-Decimal(5))
    
    # 4.- Recarga y consumo decimal
    def testRecargaConsumoDecimal(self):
        lalezka = Persona("Lalezka", "Duque", 23689465, "4545")
        miBilletera = BilleteraElectronica("4545", lalezka)
        micredito = Credito(25.78, "1280")
        miBilletera.recargar(micredito)
        midebito = Debito(11.99, "3490")
        miBilletera.consumir(midebito)
        self.assertEquals(miBilletera.saldo(), Decimal(25.78)-Decimal(11.99))
    
    # 5.- Recarga y consumo entero
    def testRecargaConsumoEntero(self):
        lalezka = Persona("Lalezka", "Duque", 23689465, "4545")
        miBilletera = BilleteraElectronica("4545", lalezka)
        micredito = Credito(300, "1280")
        miBilletera.recargar(micredito)
        midebito = Debito(100, "3490")
        miBilletera.consumir(midebito)
        self.assertEquals(miBilletera.saldo(), Decimal(300)-Decimal(100))

if __name__ == "__main__":
    unittest.main()