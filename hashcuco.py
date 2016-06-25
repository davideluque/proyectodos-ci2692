from math import floor

################################################################################
# Clase Entrada Cuco
# Descripcion: Crea un nodo tipo entrada.
# Atributos: Clave y dato del nodo.
# Métodos: Ninguno.
################################################################################

class EntradaCuco(object):
	def __init__(self,clave,dato):
		self.clave = clave
		self.dato = dato

################################################################################
# Clase Hash Cuco
# Descripcion: Crea una Tabla de Hash Cuco.
# Atributos: Tabla y número de slots.
# Métodos: hash1, hash2, buscar, agregar, eliminar, eliminarelemento, imprimir, 
#		   rehash
################################################################################

class HashCuco(object):
	def __init__(self,n):
		self.tabla = [None for i in range(n)]
		self.slots = n

################################################################################
# Método: hash1
# Descripcion: Función de hash que calcula la posicion de un elemento.
# Atributos: Clave del elemento.
################################################################################

	def hash2(self,clave):
		A = (1 - (5)**0.5) / 2 
		h = floor( self.slots * ( (clave * A) - floor(clave * A) ) )

		return int(h)

################################################################################
# Método: hash2
# Descripcion: Función de hash que calcula la posicion de un elemento.
# Atributos: Clave del elemento.
################################################################################

	def hash1(self, clave):
		h = clave % self.slots

		return h

################################################################################
# Método: rehash
# Descripcion: Aumenta de tamaño la tabla de hash.
# Atributos: Clave del elemnto.
################################################################################

	def rehash(self):
		self.slots = self.slots*10
		self.tabla = [None for i in range(self.slots)]

		return self.slots

################################################################################
# Método: buscar
# Descripcion: Busca en la Tabla de Hash Cuco un elemento.
# Atributos: Clave del elemento.
################################################################################		

	def buscar(self, clave):
		pos1 = self.hash1(clave)
		pos2 = self.hash2(clave)

		if self.tabla[pos1] != None and self.tabla[pos1].clave == clave:
			return self.tabla[self.hash1(clave)].dato
		if self.tabla[pos2] != None and self.tabla[pos2].clave == clave:
			return self.tabla[self.hash2(clave)].dato
		else:
			return None

################################################################################
# Método: agregar
# Descripcion: Agrega en la Tabla de Hash Cuco un elemento.
# Atributos: Elemento a agregar.
################################################################################

	def agregar(self,elemento):
		pos = self.hash1(elemento.clave)

		for i in range(self.slots+1):
			if self.tabla[pos] == None:
				self.tabla[pos] = elemento
				return True
				
			elif elemento.clave == self.tabla[pos].clave:
				if pos == self.hash1(elemento.clave):
					pos = self.hash2(elemento.clave)

				else:
					pos = self.hash1(elemento.clave)
		
			else:
				self.tabla[pos], elemento = elemento, self.tabla[pos]
				if pos == self.hash1(elemento.clave):
					pos = self.hash2(elemento.clave)

				else:
					pos = self.hash1(elemento.clave)

		#self.rehash()
		#self.agregar(elemento)

################################################################################
# Método: eliminarelemento
# Descripcion: Elimina un elemento de la Tabla de Hash Cuco.
# Atributos: Elemento a eliminar.
################################################################################

	def eliminarelemento(self,elemento):
		pos1 = self.hash1(elemento.clave)
		pos2 = self.hash2(elemento.clave)

		if self.tabla[pos1] is not None and self.tabla[pos1].clave == elemento.clave:
			elemento.dato = self.tabla[pos1].dato
			self.tabla[pos1] = None

			return elemento.dato

		elif self.tabla[pos2] is not None and self.tabla[pos2].clave == elemento.clave:
			elemento.dato = self.tabla[pos2].dato
			self.tabla[pos2] = None

			return elemento.dato

		else:
			return None

################################################################################
# Método: eliminar
# Descripcion: Elimina un elemento d ela Tabla de Hash Cuco.
# Atributos: Clave del elemento a eliminar.
################################################################################

	def eliminar(self,clave):
		pos1 = self.hash1(clave)
		pos2 = self.hash2(clave)

		if self.tabla[pos1] is not None and self.tabla[pos1].clave == clave:
			dato = self.tabla[pos1].dato
			self.tabla[pos1] = None

			return dato

		elif self.tabla[pos2] is not None and self.tabla[pos2].clave == clave:
			dato = self.tabla[pos2].dato
			self.tabla[pos2] = None

			return dato

		else:
			return None

################################################################################
# Método: imprimir
# Descripcion: Muestra en pantalla todos los elementos de la Tabla de HAsh Cuco.
# Atributos: Ninguno.
################################################################################

	def imprimir(self):
		for i in range (self.slots): 
			if self.tabla[i] is not None:
				print (self.tabla[i].clave, self.tabla[i].dato)
			else:
				pass	

Tablita = HashCuco(20)

A = EntradaCuco(1, 'One')
B = EntradaCuco(1, 'Uno')
C = EntradaCuco(2, 'Dos')
D = EntradaCuco(3, 'Tres')
I = EntradaCuco(3, 'Three')
E = EntradaCuco(4, 'Cuatro')
F = EntradaCuco(5, 'Cinco')
G = EntradaCuco(5, 'Five')

Tablita.agregar(A)
Tablita.agregar(B)
Tablita.agregar(C)
Tablita.agregar(D)
Tablita.agregar(E)
Tablita.agregar(F)
Tablita.agregar(G)
Tablita.agregar(I)

print('se elimino',Tablita.eliminar(1))
print('se elimino',Tablita.eliminar(5))

print('se elimino',Tablita.eliminarelemento(C))

print('Se busca', Tablita.buscar(4))

Tablita.imprimir()