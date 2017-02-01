'''
Created on 29 ene. 2017

@author: Midaysa
@author: Lalezka
'''

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datatime
import decimal


class Persona(object):
	def __init__(self, nombres, apellidos, ci, pin):
		self.nombres = nombres
		self.apellidos = apellidos
		self.ci = ci
		self.pin = pin

class Credito(object):
	def __init__(self, monto, id_recarga):
		self.monto = decimal.Decimal(monto)
		self.fecha_recarga = datetime.datetime.now()
		self.id_recarga = id_recarga


class Debito(object):
	def __init__(self, monto, id_consumo):
		self.monto = decimal.Decimal(monto)
		self.fecha_consumo = datetime.datetime.now()
		self.id_consumo = id_consumo

class BilleteraElectronica(object):
	def __init__(self, id, persona):
		self.id = id
		self.persona = persona
		self.credito = []
		self.debito = []
		self.saldo = decimal.Decimal(0)
	
	def saldo(self):
		return self.saldo
	
	def recargar(self,recarga):
		return None
	
	def consumir(self,consumo):
		return None