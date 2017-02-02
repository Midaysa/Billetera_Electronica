'''
Create on 01/2/2017

@author: Midaysa Palacios
@author: Lalezka Duque
'''

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -⁻- coding: UTF-8 -*-

import unittest, datetime, decimal, re
from ElectronicWallet import *

class billeteraElectronicaTeste(unittest.TestCase):
    
    getcontext().prec = 15
    
    # Caso: Crear Billetera
    def testCrearBilletera(self):
        andrea = Persona('Andrea', 'Costa', 21800451, '12345')
        andrea_billetera = BilleteraElectronica('12345', andrea)
        
        self.assertMultiLineEqual(andrea_billetera.persona.nombres, 'Andrea')
        self.assertMultiLineEqual(andrea_billetera.persona.apellidos, 'Costa')
        self.assertEqual(andrea_billetera.persona.ci, 21800451)
        self.assertMultiLineEqual(andrea_billetera.persona.pin, '12345')
    
    # Caso: Recarga correcta
    def testRecargaCorrecta(self):
        andres = Persona('Andres', 'Gonzalez', 21450451, '12345')
        andres_billetera = BilleteraElectronica('12345', andres)        
        nueva_recarga = Credito(150, '12500971')
        andres_billetera.recargar(nueva_recarga)
        
        self.assertEqual(andres_billetera.creditos[-1].monto, 150)
        self.assertAlmostEqual(andres_billetera.creditos[-1].id_recarga, '12500971')
    
    # Caso: Consumo correcto
    def testConsumoCorrecto(self):
        andrea = Persona('Andrea', 'Costa', 21800451, '12345')
        andrea_billetera = BilleteraElectronica('12345', andrea)
        nueva_recarga = Credito(150, '20123920')
        nuevo_consumo = Debito(89, '30110043')
        andrea_billetera.recargar(nueva_recarga)
        andrea_billetera.consumir(nuevo_consumo)
        
        self.assertEqual(andrea_billetera.saldo(), 61)

    # Caso: Recargas y consumos
    def testRecargasConsumos(self):
        andres = Persona('Andres', 'Gonzalez', 21450451, '12345')
        andres_billetera = BilleteraElectronica('12345', andres)        
        primera_recarga = Credito(150, '12500971')
        andres_billetera.recargar(primera_recarga)
        primer_consumo = Debito(46, '10101024')
        andres_billetera.consumir(primer_consumo)
        segunda_recarga = Credito(215, '52139021')
        andres_billetera.recargar(segunda_recarga)
        segundo_consumo = Debito(12, '32012311')
        andres_billetera.consumir(segundo_consumo)
        
        self.assertEqual(andres_billetera.saldo(), 307)
        
        
    # Casos esquina
    # 2.- Crear billetera con pin incorrecto
    def testCrearBilleteraPinIncorrecto(self):
        self.assertRaises(TypeError, Persona, ['Andres', 'Gonzalez', 21450451, 31234])

    # 3.- Verificacion de fechas
    def testVerificacionFecha(self):
        nueva_recarga = Credito(120, '65014932')
        fecha_actual = datetime.datetime.now()
        
        # Para la recarga
        self.assertEqual(nueva_recarga.fecha_recarga.year, fecha_actual.year)
        self.assertEqual(nueva_recarga.fecha_recarga.month, fecha_actual.month)
        self.assertEqual(nueva_recarga.fecha_recarga.day, fecha_actual.day)
        self.assertEqual(nueva_recarga.fecha_recarga.hour, fecha_actual.hour)
    
    # 4.- Recarga y consumo con decimales pequeños
    def testRecargaConsumoDecimalesPequenos(self):
        andrea = Persona('Andrea', 'Costa', 21800451, '12345')
        andrea_billetera = BilleteraElectronica('12345', andrea)
        nueva_recarga = Credito(1.145534, '20123920')
        nuevo_consumo = Debito(0.000006, '30110043')
        andrea_billetera.recargar(nueva_recarga)
        andrea_billetera.consumir(nuevo_consumo)
        self.assertEqual(andrea_billetera.saldo(), Decimal(1.145534)-Decimal(0.000006))
    
    
    # 5.- Recarga y consumo negativos
    def testRecargaConsumoNegativos(self):
        andrea = Persona('Andrea', 'Costa', 21800451, '12345')
        andrea_billetera = BilleteraElectronica('12345', andrea)
        nueva_recarga = Credito(-150, '20123920')
        nuevo_consumo = Debito(-89, '30110043')
        andrea_billetera.recargar(nueva_recarga)
        andrea_billetera.consumir(nuevo_consumo)
        
        self.assertEqual(andrea_billetera.saldo(), 0)
    
    # 6.- Nombres
    def testNombres(self):
        self.assertRaises(TypeError, Persona, [246703, 'Gonzalez', 21450451, '31234'])
    
    def testApellidos(self):
        self.assertRaises(TypeError, Persona, ['Andres', 35762 , 21450451, 31234])
    
    # 8.- Nombres con caracteres especiales
    def testNombreCaracteresEspeciales(self):
        with self.assertRaises(Exception) as context:
            andrea = Persona('Andr@', 'Da Costa Coronado', 21800451, '12345')
        self.assertTrue("Se ingreso un caracter especial en el nombre" in str(context.exception))
    
    # 9.- Apellidos con caracteres especiales
    def testApellidosCaracteresEspeciales(self):
        with self.assertRaises(Exception) as context:
            andrea = Persona('Andrea', 'Costa$?/', 21800451, '12345')
        self.assertTrue("Se ingreso un caracter especial en el apellido" in str(context.exception))
    
    # 10.- Consumo con otro tipo de datos distinto
    def testDatosConsumoErroneos(self):
        self.assertRaises(TypeError, Debito, [500, 30110043])
    
    # 11.- Datos de las persona con tipos de datos distintos
    def testDatosPersonaErroneos(self):
        self.assertRaises(TypeError, Persona, [2345, 244, '21450451', 31234])
    
    # 12.- Recarga con tipo de datos distinto
    def testDatosRecargaErroneos(self):
        self.assertRaises(TypeError, Credito, [100, 31234])
    
    
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