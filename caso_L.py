from reticulado import Reticulado
from barra import Barra
from graficar3d import ver_reticulado_3d
from math import *

def caso_L():
	# Unidades base
	m = 1.
	kg = 1.
	s = 1. 
	
	#Unidades derivadas
	N = kg*m/s**2
	cm = 0.01*m
	mm = 0.001*m
	KN = 1000*N
	KGF = 9.8067*N
	Pa = N / m**2
	KPa = 1000*Pa
	MPa = 1000*KPa
	GPa = 1000*MPa
	
	#Parametros
	L = 5.0 * m
	F = 100 * KN
	B = 2.0 * m
	H = 3.5 * m
	q = 400 * kg / m**2
	#Inicializar modelo
	ret = Reticulado()
	
	#Nodos
	ret.agregar_nodo(0     , 0   ,  0         ) #NODO 0
	ret.agregar_nodo(L     , 0   ,  0         ) #NODO 1
	ret.agregar_nodo(2*L   , 0   ,  0         ) #NODO 2
	ret.agregar_nodo(3*L   , 0   ,  0         ) #NODO 3
	
	ret.agregar_nodo(L/2   , B/2 ,  H         ) #NODO 4
	ret.agregar_nodo(3*L/2 , B/2 ,  H         ) #NODO 5
	ret.agregar_nodo(5*L/2 , B/2 ,  H         ) #NODO 6
	
	ret.agregar_nodo(0     , B   ,  0         ) #NODO 7
	ret.agregar_nodo(L     , B   ,  0         ) #NODO 8
	ret.agregar_nodo(2*L   , B   ,  0         ) #NODO 9
	ret.agregar_nodo(3*L   , B   ,  0         ) #NODO 10
	
	
	#Barras
	# A = (1.1*cm)**2
	# r = sqrt(A/3.141593)
	
	R = 8*cm
	t = 5*mm
	
	"        R  t     E         ρ         σy"
	props = [R, t, 200*GPa, 0*7600*kg/m**3, 420*MPa]
	
	
	
# ------------------------------------	
# BARRAS LONGITUDINALES INFERIORES

	ret.agregar_barra(Barra(0,  1,   *props))   # BARRA 0
	ret.agregar_barra(Barra(1,  2,   *props))   # BARRA 1
	ret.agregar_barra(Barra(2,  3,   *props))   # BARRA 2
	
	ret.agregar_barra(Barra(7,  8,   *props))   # BARRA 3
	ret.agregar_barra(Barra(8,  9,   *props))   # BARRA 4
	ret.agregar_barra(Barra(9,  10,  *props))   # BARRA 5
	
# BARRAS TRANSVERSALES INFERIORES

	ret.agregar_barra(Barra(0,  7,  *props))    # BARRA 6
	ret.agregar_barra(Barra(1,  8,  *props))    # BARRA 7
	ret.agregar_barra(Barra(2,  9,  *props))    # BARRA 8
	ret.agregar_barra(Barra(3,  10, *props))    # BARRA 9

# BARRAS DIAGONALES CRUZADAS INFERIORES

	ret.agregar_barra(Barra(1,  7,  *props))    # BARRA 10
	ret.agregar_barra(Barra(2,  8,  *props))    # BARRA 11
	ret.agregar_barra(Barra(3,  9,  *props))    # BARRA 12

	ret.agregar_barra(Barra(0,  8,  *props))    # BARRA 13
	ret.agregar_barra(Barra(1,  9,  *props))    # BARRA 14
	ret.agregar_barra(Barra(2,  10, *props))    # BARRA 15
	
# BARRAS DIAGONALES SUPERIORES

	ret.agregar_barra(Barra(4,  7,  *props))    # BARRA 16
	ret.agregar_barra(Barra(5,  8,  *props))    # BARRA 17
	ret.agregar_barra(Barra(6,  9,  *props))    # BARRA 18
	ret.agregar_barra(Barra(0,  4,  *props))    # BARRA 19
	ret.agregar_barra(Barra(1,  5,  *props))    # BARRA 20
	ret.agregar_barra(Barra(2,  6,  *props))    # BARRA 21
	ret.agregar_barra(Barra(4,  8,  *props))    # BARRA 22
	ret.agregar_barra(Barra(5,  9,  *props))    # BARRA 23
	ret.agregar_barra(Barra(6,  10, *props))    # BARRA 24
	ret.agregar_barra(Barra(1,  4,  *props))    # BARRA 25
	ret.agregar_barra(Barra(2,  5,  *props))    # BARRA 26
	ret.agregar_barra(Barra(3,  6,  *props))    # BARRA 27

# BARRAS LONGITUDINALES SUPERIORES

	ret.agregar_barra(Barra(4,  5,  *props))    # BARRA 28
	ret.agregar_barra(Barra(5,  6,  *props))    # BARRA 29
	
	
	
	
	
# ------------------------------------	
# RESTRICCIONES EN LOS NODOS

	ret.agregar_restriccion(0, 0, 0)
	ret.agregar_restriccion(0, 1, 0)
	ret.agregar_restriccion(0, 2, 0)
	
	ret.agregar_restriccion(7, 0, 0)
	ret.agregar_restriccion(7, 1, 0)
	ret.agregar_restriccion(7, 2, 0)
	
	
	ret.agregar_restriccion(3,  1, 0)
	ret.agregar_restriccion(3,  2, 0)
	ret.agregar_restriccion(10, 1, 0)
	ret.agregar_restriccion(10, 2, 0)
	


# ------------------------------------	
# FUERZAS

	F_int = L*B/2*q*KGF 
	F_ext = L/2*B/2*q*KGF
	
	ret.agregar_fuerza(0,  2, -F_ext) 
	ret.agregar_fuerza(1,  2, -F_int)
	ret.agregar_fuerza(2,  2, -F_int)
	ret.agregar_fuerza(3,  2, -F_ext)
	ret.agregar_fuerza(7,  2, -F_ext)
	ret.agregar_fuerza(8,  2, -F_int)
	ret.agregar_fuerza(9,  2, -F_int)
	ret.agregar_fuerza(10, 2, -F_ext)
	
	return ret

