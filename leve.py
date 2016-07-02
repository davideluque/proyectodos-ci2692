def levenshtein(nombre,pista):
    N = len(nombre)
    P = len(pista)
    
    if len(nombre) > len(pista):
        nombre,pista = pista,nombre
        N, P = N,P
        
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
nombre = 'casa'
pista = 'calle'
X = levenshtein(nombre,pista)

print(X)