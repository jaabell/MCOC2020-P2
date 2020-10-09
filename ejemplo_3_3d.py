from reticulado import Reticulado
from barra import Barra
from graficar3d import ver_reticulado_3d
from math import *

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
B = 2.0 *m


#Inicializar modelo
ret = Reticulado()

#Nodos
ret.agregar_nodo(0     , 0   ,  0         )
ret.agregar_nodo(L     , 0   ,  0         )
ret.agregar_nodo(2*L   , 0   ,  0         )
ret.agregar_nodo(L/2   , B/2 , sqrt(3)/2*L)
ret.agregar_nodo(3*L/2 , B/2 , sqrt(3)/2*L)
ret.agregar_nodo(0     , B   , 0          )
ret.agregar_nodo(L     , B   , 0          )
ret.agregar_nodo(2*L   , B   , 0          )





#Barras
A = (1.1*cm)**2
r = sqrt(A/3.141593)
props = [r, r, 200*GPa, 7600*kg/m**3, 420*MPa]

props2 = [r, r, 200*GPa, 7600*kg/m**3, 420*MPa]

# props2 = [0.6*r, 0.6*r, 200*GPa, 7600*kg/m**3, 420*MPa]

ret.agregar_barra(Barra(0, 1, *props))   # 0
ret.agregar_barra(Barra(1, 2, *props))   # 1
ret.agregar_barra(Barra(3, 4, *props))   # 2
ret.agregar_barra(Barra(0, 3, *props2))   # 3
ret.agregar_barra(Barra(3, 1, *props2))   # 4
ret.agregar_barra(Barra(1, 4, *props2))   # 5
ret.agregar_barra(Barra(4, 2, *props))   # 6
ret.agregar_barra(Barra(5, 6, *props))   # 7
ret.agregar_barra(Barra(6, 7, *props))   # 8
ret.agregar_barra(Barra(5, 3, *props2))   # 9
ret.agregar_barra(Barra(3, 6, *props2))   # 10
ret.agregar_barra(Barra(6, 4, *props2))   # 11
ret.agregar_barra(Barra(4, 7, *props))   # 12
ret.agregar_barra(Barra(0, 5, *props))   # 13
ret.agregar_barra(Barra(1, 6, *props))   # 14
ret.agregar_barra(Barra(2, 7, *props))   # 15
ret.agregar_barra(Barra(0, 6, *props))   # 16
ret.agregar_barra(Barra(6, 2, *props))   # 17
ret.agregar_barra(Barra(5, 1, *props))   # 18
ret.agregar_barra(Barra(1, 7, *props))   # 19


# ver_reticulado_3d(ret)



ret.agregar_restriccion(0, 0, 0)
ret.agregar_restriccion(0, 1, 0)
ret.agregar_restriccion(0, 2, 0)

ret.agregar_restriccion(2, 2, 0)
ret.agregar_restriccion(5, 2, 0)
ret.agregar_restriccion(7, 2, 0)

ret.agregar_restriccion(5, 0, 0)


ret.agregar_fuerza(4, 2, -F)


peso = ret.calcular_peso_total()

print(f"peso = {peso}")







ret.ensamblar_sistema()
ret.resolver_sistema()
f = ret.recuperar_fuerzas()
fu = ret.recuperar_factores_de_utilizacion(f)


ver_reticulado_3d(ret, 
    opciones_nodos = {
        "usar_posicion_deformada": True,
        "factor_amplificacion_deformada": 30.,
    },
    opciones_barras = {
        "color_barras_por_dato": True,
        "ver_numeros_de_barras": False,
        "ver_dato_en_barras": True,
        "dato": fu,
        "color_fondo": [1,1,1,0.4]
    })

barras_a_rediseñar = [3,4,5, 9, 10, 11]
barras = ret.obtener_barras()
for i in barras_a_rediseñar:
	barras[i].rediseñar(f[i])




ret.ensamblar_sistema()
ret.resolver_sistema()
f1 = ret.recuperar_fuerzas()
fu1 = ret.recuperar_factores_de_utilizacion(f)

peso = ret.calcular_peso_total()

print(f"peso = {peso}")

ver_reticulado_3d(ret, 
    opciones_nodos = {
        "usar_posicion_deformada": True,
        "factor_amplificacion_deformada": 30.,
    },
    opciones_barras = {
        "color_barras_por_dato": True,
        "ver_numeros_de_barras": False,
        "ver_dato_en_barras": True,
        "dato": fu1,
        "color_fondo": [1,1,1,0.4]
    })
