'''
Created on 29 ene. 2017

@author: Midaysa Palacios
@author: Lalezka Duque
'''

#!/usr/bin/env python
# -⁻- coding: UTF-8 -*-
# -*- coding: utf-8 -*-

import datetime
import decimal


class Persona(object):
	def __init__(self, nombres, apellidos, ci, pin):
		try:
			assert(type(nombres) is str)
			assert(type(apellidos) is str)
			assert(type(ci) is int)
			assert(type(pin) is str)
			
			self.nombres = nombres
			self.apellidos = apellidos
			self.ci = ci
			self.pin = pin
		except:
			print("Error en los datos del dueño de la billetera.")
			self.nombres = None
			self.apellidos = None
			self.ci = None
			self.pin = None

class Credito(object):
	def __init__(self, monto, id_recarga):
		try:
			assert(type(monto) is int)
			assert(decimal.Decimal(monto))
			
			self.monto = decimal.Decimal(monto)
			self.fecha_recarga = datetime.datetime.now()
			self.id_recarga = id_recarga
		except:
			print("Error en la recarga.")
			self.fecha = None
			self.id_recarga = None
			self.monto = None

class Debito(object):
	def __init__(self, monto, id_consumo):
		try:
			assert(type(monto) is int)
			assert(decimal.Decimal(monto))
			self.monto = decimal.Decimal(monto)
			self.fecha_consumo = datetime.datetime.now()
			self.id_consumo = id_consumo
		except:
			print("Error en el consumo")
			self.fecha = None
			self.id_consumo = None
			self.monto = None

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
		return -1
	
	def consumir(self,consumo):
		return -1