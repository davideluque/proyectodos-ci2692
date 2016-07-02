#!/usr/bin/env python
# Universidad Simón Bolívar
# CI2692: Laboratorio de Algoritmos y Estructuras II
# Proyecto 2: El misterio del robo de DACE
# Autores: David Cabeza (13-10191), Fabiola Martínez (13-10838)
# Ult. Modif: 01 Jul 2016

class documento(object):
	"""Documento que el usuario pretende retirar

	Atributos:
		nombre: Nombre del documento, es único.
		tipo: Tipo del documento, puede repetirse.
	"""
	def __init__(self, nombre, tipo):
		self.nombre = nombre
		self.tipo = tipo

class pago(object):
	"""Comprobante de pago del documento que la persona pretende retirar

	Atributos:
		nombre: Nombre del pago, es único.
		tipo: Tipo del pago, se puede repetir.
	"""
	def __init__(self, nombre, tipo):
		self.nombre = nombre
		self.tipo = tipo

class hash_table(object):
	"""Tabla de hash que guarda los documentos y los pagos
	
	El método utilizado para esta tabla es el hashing cuco que utiliza dos fun-
	ciones de hash en vez de una para evadir las colisiones.

	Atributos:
		tabla: Arreglo de m slots que guarda los valores
		slots: Número de slots (espacios) quee tiene la tabla
	"""
	def hash1(x):
		pass

	def hash2(x):
		pass

	def agregar(x):
		pass

- to map abcdario use ord(name[0]) return integer
- al crear la tabla de hash, asegurarse de que el numero de slots sea primo
- el a y b son los unicos que se cambian 

c = documento('Constancia de Estudios', 'Normal')
d = documento('Constancia de Buena Conducta', 'Certificado por el rector')
			.
			.
x = pago('Constancia de Estudios', 'Normal')

E = Entry('David Cabeza', c)
docs_table = hash_table()
docs_table.add(E)
en .add: 
if E.key.isupper() <- La clave solo es la inicial del nombre
if E.key.istitle() <- La clave es el nombre completo pero se inserta y se valida
					  usando la primera letra 

then: CAPITALIZE.

if len(name) <= 3:
	invalid (no colocar en hash_table) -> documento or pago 

if in name are special characters then:
	remove chars



DUDAS:
- El nombre en las condiciones de los documentos y pagos es el nombre del documento o del pago
- Con la primera letra se guardan pero la clave al guardarlo es el nombre completo?
- ejemplo de un pago?
