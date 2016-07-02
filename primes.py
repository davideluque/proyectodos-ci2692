def generador_primos_y(ui: int, uf = None):
	"""Generador de un arreglo de números primos en un intervalo dado
	
	parametros:
		ui: entero inicial del intervalo de primos
		uf: entero final del intervalo de primos, si no se especifica, se asumirá
			el valor 2*u + 1
	retorna:
		generador de números primos
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
			yield p

def generador_primos_a(ui: int, uf = None):
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

numeros = generador_primos_a(81)
print(numeros)
for x in generador_primos_y(81):
	print(x)