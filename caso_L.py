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
        Pa = N / m**2
        KPa = 1000*Pa
        MPa = 1000*KPa
        GPa = 1000*MPa
        
        #Parametros
        L = 5.0 * m
        B = 2.0 * m
        H = 3.5 * m
        
        # q = 400 * kg / m**2
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
        
        
    #   Barras

        props = [8*cm, 5*mm, 200*GPa, 7600*kg/m**3, 420*MPa]
        
        ret.agregar_barra(Barra(0, 1, *props))   # 0
        ret.agregar_barra(Barra(1, 2, *props))   # 1
        ret.agregar_barra(Barra(2, 3, *props))   # 2
        ret.agregar_barra(Barra(4, 5, *props))   # 3
        ret.agregar_barra(Barra(5, 6, *props))   # 4
        ret.agregar_barra(Barra(7, 8, *props))   # 5
        ret.agregar_barra(Barra(8, 9, *props))   # 6
        ret.agregar_barra(Barra(9, 10, *props))  # 7
        
        ret.agregar_barra(Barra(0, 8, *props))   # 8
        ret.agregar_barra(Barra(1, 7, *props))   # 9
        
        ret.agregar_barra(Barra(1, 9, *props))   # 10
        ret.agregar_barra(Barra(2, 8, *props))   # 11
        
        ret.agregar_barra(Barra(2, 10, *props))  # 12
        ret.agregar_barra(Barra(3, 9, *props))   # 13
        
        ret.agregar_barra(Barra(0, 4, *props))   # 14
        ret.agregar_barra(Barra(1, 4, *props))   # 15
        ret.agregar_barra(Barra(7, 4, *props))   # 16
        ret.agregar_barra(Barra(8, 4, *props))   # 17
        
        ret.agregar_barra(Barra(1, 5, *props))   # 18
        ret.agregar_barra(Barra(2, 5, *props))   # 19
        ret.agregar_barra(Barra(8, 5, *props))   # 20
        ret.agregar_barra(Barra(9, 5, *props))   # 21
        
        
        ret.agregar_barra(Barra(2, 6, *props))   # 22
        ret.agregar_barra(Barra(3, 6, *props))   # 23
        ret.agregar_barra(Barra(9, 6, *props))   # 24
        ret.agregar_barra(Barra(10, 6, *props))  # 25
        
        
        ret.agregar_barra(Barra(0, 7, *props))   # 26
        ret.agregar_barra(Barra(1, 8, *props))   # 27
        ret.agregar_barra(Barra(2, 9, *props))   # 28
        ret.agregar_barra(Barra(3, 10, *props))  # 29
        
        
        ret.agregar_restriccion(0, 0, 0)
        ret.agregar_restriccion(0, 1, 0)
        ret.agregar_restriccion(0, 2, 0)
        
        ret.agregar_restriccion(7, 0, 0)
        ret.agregar_restriccion(7, 1, 0)
        ret.agregar_restriccion(7, 2, 0)
        
        
        ret.agregar_restriccion(3, 1, 0)
        ret.agregar_restriccion(3, 2, 0)
        ret.agregar_restriccion(10, 1, 0)
        ret.agregar_restriccion(10, 2, 0)
        
        return ret

