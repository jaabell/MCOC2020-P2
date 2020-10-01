from reticulado import Reticulado
from barra import Barra
from graficar2d import ver_reticulado_2d
from math import *
"Prueba"

# Unidades base
m = 1.
kg = 1.
s = 1. 

#Unidades derivadas
N = kg*m/s**2
cm = 0.01*m
mm = 0.001*m
KN = 1000*N

Pa = N / m**2
KPa = 1000*Pa
MPa = 1000*KPa
GPa = 1000*MPa

#Parametros
L = 5.0  *m
F = 100*KN

#Inicializar modelo
ret = Reticulado()

#Nodos
ret.agregar_nodo(0,0)
ret.agregar_nodo(L,0)
ret.agregar_nodo(2*L,0)
ret.agregar_nodo(L/2,sqrt(3)/2*L)
ret.agregar_nodo(3*L/2,sqrt(3)/2*L)


#Barras
A = (1.1*cm)**2
r = sqrt(A/3.141593)


props = [r, r, 200*GPa, 0*7600*kg/m**3, 420*MPa]
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

ver_reticulado_2d(ret)


ret.agregar_fuerza(4, 1, -F)

ret.ensamblar_sistema()
ret.resolver_sistema()
f = ret.recuperar_fuerzas()

print(ret)


ver_reticulado_2d(ret, 
    opciones_nodos = {
        "usar_posicion_deformada": True,
        "factor_amplificacion_deformada": 10.,
    },
    opciones_barras = {
        "color_barras_por_fuerza": True,
        "ver_numeros_de_barras": False,
        "ver_fuerza_en_barras": True
    })
