#!/usr/bin/env python
# Universidad Simón Bolívar
# CI2692: Laboratorio de Algoritmos y Estructuras II
# Proyecto 2: El misterio del robo de DACE
# Autores: David Cabeza (13-10191), Fabiola Martínez (13-10838)
# Ult. Modif: 01 Jul 2016

import sys
from random import randint, choice
from math import floor

class pila(object):
	def __init__(self, n):
		self.top = -1
		self.pila = [None for i in range(n)]
		self.lenght = len(self.pila)

	def empty(self):
		return self.top == 0

	def push(self, x):
		if self.top == self.lenght:
			print('La pila está llena')
			return 0
		self.top = self.top + 1
		self.pila[self.top] = x

	def pop(self, x):
		if self.empty():
			print('La pila está vacía')
		elemento = self.top
		self.top = None
		self.top = self.top - 1
		return elemento

class lista_doble_enlazada(object):
	def __init__(self, clave):
		self.head = None
		self.clave = 0
		self.nelements = 0

	def insertar(self, x):
		"""Inserta un elemento en la lista"""
		x.next = self.head
		if self.head != None: self.head.prev = x 
		x.prev = None
		self.head = x
		self.nelements += 1
		return 1

	def buscar(self, x):
		x = self.head
		while x != None and x.clave != k:
			x = x.next
		return x 

	def eliminar(self, x):
		elemento = buscar(x)
		if elemento.prev != None: elemento.prev.next = elemento.next
		if elemento.next != None: elemento.next.prev = elemento.prev
		if elemento.prev == None: self.head = elemento.next
		self.nelements -= 1

class _cola(object):
	"""Clase para crear una cola

	Atributos:
		head: Primer elemento de la cola
		tail: Apunta a un espacio libre si lo hay o a la cabeza si la cola está llena
		nelements: Número de elementos en la cola
		cola: Arreglo con la cola
		lenght: Dimensión de la cola
	"""
	def __init__(self, n):
		self.head = 0
		self.tail = 0
		self.nelements = 0
		self.cola = [None for i in range(n)]
		self.lenght = len(self.cola)
	
	def empty(self):
		return self.nelements == 0

	def enqueue(self, x):
		if (self.nelements == self.lenght):
			print('La cola está llena')
			return 0
		self.cola[self.tail] = x
		self.tail = self.tail + 1
		if self.tail > self.lenght:
			self.tail = 0
		self.nelements = self.nelements + 1

	def dequeue(sef):
		if self.empty():
			print('La cola está vacía')
			return 0
		x = self.cola[self.head]
		self.cola[self.head] = None
		self.head = self.head + 1
		if self.head > self.lenght:
			self.head = 0
		self.nelements = self.nelements - 1
		return x

class documento(object):
	"""Documento que el usuario pretende retirar

	Atributos:
		nombre: Nombre del documento, es único.
		tipo: Tipo del documento, puede repetirse.
	"""
	def __init__(self, clave, nombre, tipo):
		self.nombre = nombre
		self.tipo = tipo
		self.clave = clave
		self.prev = None
		self.next = None

class pago(object):
	"""Comprobante de pago del documento que la persona pretende retirar

	Atributos:
		nombre: Nombre del pago, es único.
		tipo: Tipo del pago, se puede repetir.
	"""
	def __init__(self, clave, nombre, tipo):
		self.nombre = nombre
		self.tipo = tipo
		self.clave = clave
		self.prev = None
		self.next = None

class hash_table(object):
	"""Tabla de hash que guarda los documentos o los pagos
	
	El método utilizado para esta tabla es el hashing cuco que utiliza dos fun-
	ciones de hash en vez de una combinado con listas enlazadas para evitar las 
	colisiones.

	Atributos:
		tabla: Arreglo de m slots que guarda los valores
		slots: Número de slots (espacios) que tiene la tabla
		p:
		c:
		maxiter:
	"""
	def __init__(self, m):
		self.tabla = [lista_doble_enlazada(None) for i in range(m)]
		self.slots = m
		self.maxiter = m+1

	def hash1(self, clave):
		"""Función de hash que utiliza el método de división
		
		Parámetros:
			clave: Clave a calcular el slot en la tabla

		Retorna:
			h: Slot a posicionar la clave 
		"""
		h = clave % self.slots

		return h

	def hash2(self, clave):
		"""Función de hash que utiliza el método multiplicativo
		
		Parámetros:
			clave: Clave a calcular el slot en la tabla

		Retorna:
			h: Slot a posicionar la clave 		
		"""
		A = (1 - (5)**0.5) / 2 
		h = floor( self.slots * ( (clave * A) - floor(clave * A) ) )

		return int(h)
	
	def agregar(self, elemento):

		pos = self.hash1(elemento.clave)

		for i in range(self.maxiter):
			if type(elemento) == pago or type(elemento) == (documento):
				if self.tabla[pos].head == None:
					self.tabla[pos].clave = elemento.clave
					self.tabla[pos].insertar(elemento)
					return 

				elif self.tabla[pos].nelements < 10 and self.tabla[pos].clave == elemento.clave:
					self.tabla[pos].insertar(elemento)
					return
				
				elif self.tabla[pos].nelements == 10 and self.tabla[pos].clave == elemento.clave:
					pos = self.hash2(elemento.clave)
					continue
				else:
					Temporal = elemento
					elemento = self.tabla[pos]
					self.tabla[pos] = lista_doble_enlazada(Temporal.clave)
					self.tabla[pos].insertar(Temporal)

					if pos == self.hash1(elemento.clave):
						pos = self.hash2(elemento.clave)
					else:
						pos = self.hash1(elemento.clave)

			if type(elemento) == lista_doble_enlazada:
				pos = self.hash1(elemento.clave)
				for i in range(self.maxiter):
					if self.tabla[pos].head == None:
						self.tabla[pos] = elemento
						return 
					else:
						elemento, self.tabla[pos] = self.tabla[pos], elemento
						if pos == self.hash1(elemento.clave):
							pos = self.hash2(elemento.clave)
						else:
							pos = self.hash1(elemento.clave)

			return self.rehash()

	def rehash(self):
		self.slots = 2 * self.slots
		self.tabla = [lista_doble_enlazada(None) for i in range(self.slots)]

		return -1


	def buscar(self, k):
		f1, f2 = None, None

		if self.tabla[self.hash1(k)].head != None and self.tabla[self.hash1(k)].clave == k:
			f1 = self.tabla[self.hash1(k)]
		if self.tabla[self.hash2(k)].head != None and self.tabla[self.hash2(k)].clave == k:
			f2 = self.tabla[self.hash2(k)]

		return f1, f2

	def eliminar(self, k):
		
		if self.tabla[self.hash1(k)].clave != None and self.tabla[self.hash1(k)].clave == k:
			self.tabla[self.hash1(k)] = lista_doble_enlazada(None)
		if self.tabla[self.hash2(k)].clave != None and self.tabla[self.hash2(k)].clave == k:
			self.tabla[self.hash1(k)] = lista_doble_enlazada(None)

def generador_primos(ui: int, uf = None):
	"""Generador de un arreglo de números primos en un intervalo dado
	
	parametros:
		ui: entero inicial del intervalo de primos
		uf: entero final del intervalo de primos, si no se especifica, se asumirá
			el valor 2*u + 1
	retorna:
		primos: arreglo que contiene números primos en el intervalo [ui, uf]
	"""
	if not uf: uf = 2*ui + 1
	primos = []
	for p in range(ui, uf):
		primo = True
		for d in range(2, p):
			if p % d == 0:
				primo = False
				break
		if primo:
			primos.append(p)
	
	return primos

def leer_entrada(ent, col):

	if (not '.txt' in ent):
		ent += '.txt'

	if (not '.txt' in col):
		col += '.txt'

	documentos = []
	pagos = []
	pistas = []
	with open(ent, 'r') as f:

		nroPistas = f.readline().replace('\n', '')

		for line in f:
			if (line[:3] == 'pag'):
				pagos.append(line[4:].replace('\n', ''))
				continue
			elif (line[:3] == 'pis'):
				pistas.append(line[6:].replace('\n', ''))
				continue
			else:
				documentos.append(line[4:].replace('\n', ''))
				continue

		f.close()
	
	assert(f.closed)

	cola = []
	with open(col, 'r') as file:

		for line in file: cola.append(line.replace('\n', ''))

		file.close()

	assert(file.closed)

	return documentos, pagos, pistas, cola

def calcular_ascii(string):
	"""Función para calcular la suma de los ascii de un string

	Parámetros:
		string: Cadena a calcular la suma de sus caracteres transformados a ascii

	Retorna:
		ascii_sum: Entero el cual es la suma de los ascii de la cadena.
	"""
	ascii_sum = 0

	for char in string: ascii_sum += ord(char)

	return ascii_sum

def procesar_documentos(docs):
	"""Función para procesar el arreglo que contiene los documentos

	Parámetros:
		docs: Arreglo con elementos de tipo string. El formato del string debe
		ser nombredelapersona espacio tipodeldocumento
	"""
	for element in docs:
		
		i = element.index(' ')
		nombre = element[:i]
		tipo = element[i+1:]

		if not nombre.isalpha(): nombre = ''.join(x for x in nombre if x.isalpha())
		
		if len(nombre) < 3:
			print('Se invalidó el documento de "', nombre,'" por tener menos de 3 '+
				'caracteres')
			continue
		
		if not nombre.istitle(): nombre = nombre.title()

		clave = calcular_ascii(nombre)
		yield documento(clave, nombre, tipo)

def procesar_pagos(pays):
	"""Función para procesar el arreglo que contiene los pagos

	Parámetros:
		pays: Arreglo con elementos de tipo string. El formato del string debe
		ser nombredelapersona espacio tipodelpago
	"""
	for element in pays:	
		
		i = element.index(' ')
		nombre = element[:i]
		tipo = element[i+1:]

		if not nombre.isalpha(): nombre = ''.join(x for x in nombre if x.isalpha())

		if len(nombre) < 3:
			print('Se invalidó el pago de "', nombre,'" por tener menos de '
				 +'3 caracteres')
			continue
		
		if not nombre.istitle(): nombre = nombre.title()

		clave = calcular_ascii(nombre)
		yield pago(clave, nombre, tipo)

def main():
	
	print('\n >> Sistema para identificar al sospechoso del robo de dace << \n')
	
	entrada = sys.argv[1]
	e_cola = sys.argv[2]

	# Se realiza la lectura de los archivos y se almacenan en las variables docs, 
	# pays,clues y queue los documentos, los pagos, las pistas y la cola de personas 
	# respectivamente
	docs, pays, clues, queue = leer_entrada(entrada, e_cola)
	
	# Se crean las tablas de hash de pagos y de documentos
	tabla_pagos = hash_table(len(pays))
	tabla_docs = hash_table(len(docs))

	# Añadimos los pagos válidos a la tabla de hash de pagos
	while True:
		for pago in procesar_pagos(pays):
			result = tabla_pagos.agregar(pago)
			if result == -1:
				print('Rehash was needed. Restart iteration')
				break
			print('Pago válido añadido a la tabla:', pago.nombre)
		else:
			break

	# Añadimos los documentos válidos a la tabla de hash de pagos
	while True:
		for documento in procesar_documentos(docs):	
			result = tabla_docs.agregar(documento)
			if result == -1:
				print('Rehash was needed. Restart iteration')
				break
			print('Documento válido añadido a la tabla:', documento.nombre)
		else:
			break

if (__name__ == '__main__'):
	main()
