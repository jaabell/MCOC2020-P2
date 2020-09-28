import numpy as np

class Reticulado(object):
    def __init__(self):
        super(Reticulado, self).__init__()
        self.xyz = np.zeros((0,3), dtype=np.double)
        self.Nnodos = 0
        self.barras = 0
        self.cargas = {}
        self.restricciones = {}
    def agregar_nodo(self, x, y, z=0):
        self.xyz.resize((self.Nnodos+1,3))
        self.xyz[self.Nnodos,:] = [x,y,z]
        self.Nnodos +=1
        return
    def agregar_barra(self, barra):
        self.barras+=barra
        return
    def obtener_coordenada_nodal(self, n): 
        if n>= self.Nnodos:
                return
        return self.xyz[n,:]
    def calcular_peso_total(self):
        return
    def obtener_nodos(self):
        n = np.zeros((self.Nnodos,4), dtype=np.double)
        for i in range(self.Nnodos):
            n[i,0] = round(i,)
            for j in range(3):
                n[i,j+1] = self.xyz[i,j]
        return n
    def obtener_barras(self):
    	n=[]
    	for i in range(self.barras):
    		for j in range(self.barras):
    			if i!=j and j>i:
    				n.append(np.array([i,j]))
    	return n
    def agregar_restriccion(self, nodo, gdl, valor=0.0):
        return
    def agregar_fuerza(self, nodo, gdl, valor):
        return
    def ensamblar_sistema(self):
        return
    def resolver_sistema(self):
        return
    def recuperar_fuerzas(self):
        return
    def __str__(self):
        s = "nodos:\n"
        s += f"{round(Reticulado.obtener_nodos(self)[0,0])} : ({Reticulado.obtener_nodos(self)[0,1]} {Reticulado.obtener_nodos(self)[0,2]} {Reticulado.obtener_nodos(self)[0,3]})\n"
        s += f"{round(Reticulado.obtener_nodos(self)[1,0])} : ({Reticulado.obtener_nodos(self)[1,1]} {Reticulado.obtener_nodos(self)[1,2]} {Reticulado.obtener_nodos(self)[1,3]})\n"
        s += f"{round(Reticulado.obtener_nodos(self)[2,0])} : ({Reticulado.obtener_nodos(self)[2,1]} {Reticulado.obtener_nodos(self)[2,2]} {Reticulado.obtener_nodos(self)[2,3]})\n"
        s += "barras:\n"
        for i in range(self.barras):
        	s += f"{i} : {Reticulado.obtener_barras(self)[i]}\n"
        return s

ret=Reticulado()
ret.agregar_nodo(0,0)
ret.agregar_nodo(1,0)
ret.agregar_nodo(1,1)
ret.agregar_barra(3)
print (ret)
