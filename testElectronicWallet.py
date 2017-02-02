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
        return
    
    # 5.- Recarga y consumo decimal
    def testRecargaConsumoDecimal(self):
        return
    
    # 6.- Recarga y consumo entero
    def testRecargaConsumoEntero(self):
        return


if __name__ == "__main__":
    unittest.main()