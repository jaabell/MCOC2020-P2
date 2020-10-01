


restricciones = {}

def agregar_restriccion(nodo, gdl, valor):
	
	
	
	if nodo not in restricciones:
		restricciones[nodo] = [[gdl, valor]]
		print (nodo,restricciones)
	else:
		restricciones[nodo].append([gdl, valor])


agregar_restriccion(0, 1, 0.)
agregar_restriccion(1, 1, 0.)
agregar_restriccion(2, 1, 0.)


print(f"rest = {restricciones}")