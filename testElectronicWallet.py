'''
Create on 01/2/2017

@author: Midaysa Palacios
@author: Lalezka Duque
'''

#!/usr/bin/env python
# -⁻- coding: UTF-8 -*-
# -*- coding: utf-8 -*-

import unittest, datetime
from ElectronicWallet import *

class billeteraElectronicaTeste(unittest.TestCase):
    
    # Caso: Crear Billetera
    def testCrearBilletera(self):
        andrea = Persona('Andrea', 'Da Costa', 21800451, '12345')
        andrea_billetera = BilleteraElectronica('12345', andrea)
        
        self.assertMultiLineEqual(andrea_billetera.persona.nombres, 'Andrea')
        self.assertMultiLineEqual(andrea_billetera.persona.apellidos, 'Da Costa')
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
        andrea = Persona('Andrea', 'Da Costa', 21800451, '12345')
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
        return
    
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
        return
    
    # 2.- Consumo negativo
    def testConsumoNegativo(self):
        return
    
    # 3.- Precision de la recarga
    def testRecargaDecimalesPequenos(self):
        return
    
    # 4.- Precicion del consumo
    def testConsumoDecimalesPequenos(self):
        return
    
    # 5.- Recarga con el máximo entero (32 bits)
    def testRecargaMaxEntero(self):
        return
    
    # 6.- Recarga y consumo total
    def testRecargaConsumoTotal(self):
        return
    
    # 7.- Recarga cero
    def testRecargaCero(self):
        return
    
    # 8.- Consumir cero
    def testConsumoCero(self):
        return
    
    # Casos maliciosos
    # 1.- Consumo mayor que recarga
    def testConsumoMayorQueRecarga(self):
        return
    
    # 2.- Recarga entera y consumo decimal
    def testRecargaEnteraConsumoDecimal(self):
        return
    
    # 3.- Recarga decimal y consumo entero
    def testRecargaDecimalConsumoEntero(self):
        return
    
    # 4.- Consumir con pin incorrecto
    def testConsumoPinIncorrecto(self):
        with self.assertRaises(ValueError) as context:
            nuevo_debito = Debito(40, '900464456')
            pedro = Persona('Pedro', 'Camejo', 1715630, '12345')
            BilleteraElectronica('23417', pedro).consumir(nuevo_debito)
            
        self.assertTrue('El PIN ingresado no coincide con el del usuario' in str(context.exception))
        
    # 5.- Consumir con pin correcto
    def testPinCorrecto(self):
        nuevo_debito = Debito(40, '90013422')
        pedro = Persona('Pedro', 'Camejo', 1715630, '12345')
        pedro_billetera = BilleteraElectronica('12345', pedro)
        nuevo_credito = Credito(100, '94320110')
        pedro_billetera.recargar(nuevo_credito)
        pedro_billetera.consumir(nuevo_debito)
        
        self.assertEqual(pedro_billetera.saldo(), 60)
    
    # 6.- Recarga y consumo decimal
    def testRecargaConsumoDecimal(self):
        return
    
    # 7.- Recarga y consumo entero
    def testRecargaConsumoEntero(self):
        return

if __name__ == "__main__":
    unittest.main()