'''
Created on 29 ene. 2017

@author: Midaysa Palacios
@author: Lalezka Duque
'''

#!/usr/bin/env python
# -⁻- coding: UTF-8 -*-
# -*- coding: utf-8 -*-

import datetime
from decimal import *


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
			print("Error en los datos del usuario.")
			self.nombres = None
			self.apellidos = None
			self.ci = None
			self.pin = None

class Credito(object):
	
	getcontext().prec = 15
	
	def __init__(self, monto, id_recarga):
		try:
			assert(type(monto) is int or type(monto) is float)
			self.monto = Decimal(monto)
			self.fecha_recarga = datetime.datetime.now()
			self.id_recarga = id_recarga
		except:
			print("Error en la recarga.")
			self.fecha = None
			self.id_recarga = None
			self.monto = None

class Debito(object):
	
	getcontext().prec = 15
	
	def __init__(self, monto, id_consumo):
		try:
			assert(type(monto) is int or type(monto) is float)
			self.monto = Decimal(monto)
			self.fecha_consumo = datetime.datetime.now()
			self.id_consumo = id_consumo
		except:
			print("Error en el consumo")
			self.fecha = None
			self.id_consumo = None
			self.monto = None

class BilleteraElectronica(object):
	
	getcontext().prec = 15
	
	def __init__(self, id, persona):
		self.id = id
		self.persona = persona
		self.creditos = []
		self.debitos = []
		self.saldo_actual = Decimal(0)
	
	def saldo(self):
		return self.saldo_actual
	
	def recargar(self, recarga):
		if (recarga.monto <= 0):
			print("El saldo a recargar debe ser un numero natural.")
			return -1
		
		self.creditos.append(recarga)
		self.saldo_actual += recarga.monto
		
	def consumir(self, consumo):
		if (self.persona.pin != self.id):
			print("El PIN ingresado no coincide con el del usuario.")
			return -1
		
		if (consumo.monto > self.saldo_actual):
			print("El consumo es mayor al saldo disponible.")
			return -1
		
		if (consumo.monto <= 0):
			print("El consumo a realizar debe ser un numero natural.")
			return -1
		
		self.debitos.append(consumo)
		self.saldo_actual -= consumo.monto
		