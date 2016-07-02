#!/usr/bin/env python
# Universidad Simón Bolívar
# CI2692: Laboratorio de Algoritmos y Estructuras II
# Proyecto 2: El misterio del robo de DACE
# Autores: David Cabeza (13-10191), Fabiola Martínez (13-10838)
# Ult. Modif: 01 Jul 2016

import sys
from math import floor

class Pila():
    """ Implementación de Pilas."""
    def __init__(self, n):
        self.pila = [None for x in range(n)]
        self.top = -1
        self.elementos = n

    def push(self, x):
        """ Agrega un elemento a la pila."""
        self.top += 1
        self.pila[self.top] = x

    def pop(self):
        """ Elimina un elemento de la pila."""
        if self.top == -1:
            raise IndexError('La pila está vacía, no se puede eliminar otro ' +
                             'elemento.')
        self.top -= 1
        return self.pila[self.top + 1]

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

	def buscar(self, t):
		x = self.head
		while x != None and x.tipo != t:
			x = x.next
		return x 

	def eliminar(self, x):
		elemento = buscar(x)
		if elemento.prev != None: elemento.prev.next = elemento.next
		if elemento.next != None: elemento.next.prev = elemento.prev
		if elemento.prev == None: self.head = elemento.next
		self.nelements -= 1

	def _busqueda(self):
		x = self.head
		a = []
		while x != None:
			a.append(x.tipo)
			x = x.next
		return a 

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

def levenshtein(nombre , pista):
    N = len(nombre)
    P = len(pista)
    
    if len(nombre) > len(pista):
        nombre, pista = pista, nombre
        N, P = N, P
        
    distancia = range(N+1)
    for i in range(1,(P+1)):
        previous, distancia = distancia, [i]+[0]*N
        for j in range(1,N+1):
            agregar, eliminar = previous[j]+1, distancia[j-1]+1
            sustituir = previous[j-1]
            if nombre[j-1] != pista[i-1]:
                sustituir = sustituir + 1
            distancia[j] = min(agregar, eliminar, sustituir)
            
    return distancia[N]

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

def producir_salida(salidapagos, nosaldran, sospechosos):

	with open('salida.txt', 'w') as f:
		f.write('pista ')
		for sospechoso in sospechosos:
			f.write(sospechoso+' ')
		
		f.write('\n')
		f.write('\n')
		for element in salidapagos:
			i = element.index(' ')
			nombre = element[:i]
			tipo = element[i+1:]
			f.write(nombre + ' ' + tipo + '\n')

		f.write('\n')

		for element in nosaldran:
			i = element.index(' ')
			nombre = element[:i]
			tipo = element[i+1:]
			f.write(nombre + ' ' + tipo + '\n')


def descifrar_pista(clues):
	""".
	Modifica una expresión, a la Notación Polaca Inversa
	La función usa como operandos binarios las letras: r, e, l, s
	(prioridad desde el más bajo al más alto donde 'r' es menor prioridad y 's'
	mayor prioridad).
	"""
	completa = ''
	for element in clues:
		i = element.index(' ')
		completa += element[i+1:]	
	completa = completa.replace(' ', '')

	cont = Pila(len(completa))
	res = []
	for i in range(len(completa)):
	    if completa[i] == '(':
	        cont.push(completa[i])
	    elif completa[i] != 'r' and completa[i] != 'e' and completa[i] != 'l' \
	            and completa[i] != 's' and completa[i] != ')':
	        res.append(completa[i])
	    elif completa[i] == ')':
	        while cont.top != -1 and cont.pila[cont.top] != '(':
	            res.append(cont.pop())
	        if cont.pila[cont.top] == '(':
	            cont.pop()
	        completa[i].strip(')')
	    else:
	        while cont.top != -1 and cont.pila[cont.top] == 's':
	            res.append(cont.pop())
	        cont.push(completa[i])

	while cont.top != -1:
	    res.append(cont.pop())
	tot = ''
	for i in range(len(res)):
	    tot += res[i]
	return tot

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
			#print('Pago válido añadido a la tabla:', pago.nombre)
		else:
			break

	# Añadimos los documentos válidos a la tabla de hash de pagos
	while True:
		for documento in procesar_documentos(docs):	
			result = tabla_docs.agregar(documento)
			if result == -1:
				print('Rehash was needed. Restart iteration')
				break
			#print('Documento válido añadido a la tabla:', documento.nombre)
		else:
			break

	# Utilizamos la notación polaca inversa para descifrar la pista
	pista = descifrar_pista(clues)
	print(pista)
	
	# Calculamos la distancia entre la pista y las personas de la cola
	distancias = []
	for persona in queue:
		distancia = levenshtein('pista', persona)
		distancias.append(str(distancia) +' pista '+ persona)

	minima = 1000000000000
	for cadenas in distancias:
		minima = min(int(cadenas[0]), minima)

	sospechosos = []

	for x in distancias:
		if str(minima) in x:
			i = x.index(' ')
			final = (i + len('pista'))+2
			sospechosos.append(x[final:])

	# Calculamos los que pudieron retirar documento
	salidapagos = []
	nosaldran = []
	for persona in queue:
		clavepersona = calcular_ascii(persona)
		x, y = tabla_docs.buscar(clavepersona)
		w, z = tabla_pagos.buscar(clavepersona)
		
		wb, zb, docsx, docsy = ['w'], ['z'], ['x'], ['y']
		
		if w != None:
			wb = w._busqueda()
		if z != None:
			zb = z._busqueda()
		if x != None:
			docsx = x._busqueda()
		if y != None:
			docsy = y._busqueda()

		for doc in docsx:
			if doc in wb:
				salidapagos.append(persona+' '+doc)
			if doc in zb:
				salidapagos.append(persona+' '+doc)
			if doc != 'x':
				nosaldran.append(persona+' '+doc)

		for doc in docsy:
			if doc in wb:
				salidapagos.append(persona+' '+doc)
			if doc in zb:
				salidapagos.append(persona+' '+doc)
			if doc != 'y':
				nosaldran.append(persona+' '+doc)

	print(salidapagos)
	print(nosaldran)

	producir_salida(salidapagos, nosaldran, sospechosos)

if (__name__ == '__main__'):
	main()
