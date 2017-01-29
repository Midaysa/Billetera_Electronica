'''
Created on 29 ene. 2017

@author: Midaysa
'''

#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Dueño(object):
	def __init__(self, nombre, apellido, ci, pin):
		self.nombre = nombre
		self.apellido = apellido
		self.ci = ci
		self.pin = pin


class Credito(object):
	def __init__(self, monto, fecha_trans, id_recarga):
		self.monto = monto
		self.fecha_trans = fecha_trans
		self.id_recarga = id_recarga


class Debito(object):
	def __init__(self, monto, fecha_trans, id_consumo):
		self.monto = monto
		self.fecha_trans = fecha_trans
		self.id_consumo = id_consumo


class BilleteraElectronica(object):
	def __init__(self, dueño):
		self.id = id
		self.dueño = dueño
		self.credito = []
		self.debito = []
