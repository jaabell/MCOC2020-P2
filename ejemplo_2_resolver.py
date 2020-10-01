from reticulado import Reticulado
from barra import Barra
from graficar2d import ver_reticulado_2d
from math import *


# Unidades
cm = 1e-2
mm = 1e-3
kg = 1.0
GPa = 1e+9
MPa = 1e+6
KN = 1e3
m = 1.0
L = 5.0


#Inicializar modelo
ret = Reticulado()


#Nodos
ret.agregar_nodo(0,0)
ret.agregar_nodo(L,0)
ret.agregar_nodo(2*L,0)
ret.agregar_nodo(L/2,sqrt(3)/2*L)
ret.agregar_nodo(3*L/2,sqrt(3)/2*L)


#Barras
props = [20*cm, 4*mm, 200*GPa, 7600*kg/m**3, 420*MPa]

ret.agregar_barra(Barra(0, 1, *props))
ret.agregar_barra(Barra(1, 2, *props))
ret.agregar_barra(Barra(3, 4, *props))
ret.agregar_barra(Barra(0, 3, *props))
ret.agregar_barra(Barra(3, 1, *props))
ret.agregar_barra(Barra(1, 4, *props))
ret.agregar_barra(Barra(4, 2, *props))

ret.agregar_restriccion(0, 0, 0)
ret.agregar_restriccion(0, 1, 0)
ret.agregar_restriccion(2, 1, 0)

ret.agregar_fuerza(4, 1, -100*KN)

ret.ensamblar_sistema()
ret.resolver_sistema()
ret.recuperar_fuerzas()

print(ret)
ver_reticulado_2d(ret)


