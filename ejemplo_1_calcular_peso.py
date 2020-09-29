from reticulado import Reticulado
from barra import Barra
from graficar2d import ver_reticulado_2d

# Unidades
cm = 1e-2
mm = 1e-3
kg = 1.0
GPa = 1e+9
MPa = 1e+6
KN = 1e3
m = 1.0

#Inicializar modelo
ret = Reticulado()


#Nodos
ret.agregar_nodo(0,0)
ret.agregar_nodo(1,0)
ret.agregar_nodo(1,1)

print(ret)

# #Barras
# b1 = Barra(0, 1, 20*cm, 4*mm, 200*GPa, 7600*kg/m**3, 420*MPa)
# b2 = Barra(1, 2, 20*cm, 4*mm, 200*GPa, 7600*kg/m**3, 420*MPa)
# b3 = Barra(0, 2, 20*cm, 4*mm, 200*GPa, 7600*kg/m**3, 420*MPa)

# ret.agregar_barra(b1)
# ret.agregar_barra(b2)
# ret.agregar_barra(b3)

# peso_total = ret.calcular_peso_total()

# print(f"peso_total = {peso_total}")

# ver_reticulado_2d(ret)