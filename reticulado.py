import numpy as np

class Reticulado(object):
	"""Define un reticulado"""

	def __init__(self):
		super(Reticulado, self).__init__()
		self.xyz = np.zeros((0,3), dtype=np.double)
		self.Nnodos = 0
		self.barras = []
		self.cargas = {}
		self.restricciones = {}
	def agregar_nodo(self, x, y, z=0):
		self.xyz.resize((self.Nnodos+1,3))
		self.xyz[self.Nnodos,:] = [x,y,z]
		self.Nnodos +=1
		return



#========================================
#	               ENTREGA 1
#========================================


	def agregar_barra(self, barra):
		return self.barras.append(barra)

	def obtener_coordenada_nodal(self, nodo):
		return self.xyz[nodo]

	def calcular_peso_total(self):
		peso_total = 0
		for b in self.barras():
			peso_total += b.calcular_peso(self)
		return peso_total

#========================================







	def obtener_nodos(self):
		"""Implementar"""
		return 

	def obtener_barras(self):
		"""Implementar"""
		return 

	def agregar_restriccion(self, nodo, gdl, valor=0.0):
		"""Implementar"""
		return
	def agregar_fuerza(self, nodo, gdl, valor):
		"""Implementar"""
		return
	def ensamblar_sistema(self):
		"""Implementar"""
		return
	def resolver_sistema(self):
		"""Implementar"""
		return
	def recuperar_fuerzas(self):
		"""Implementar"""
		return




	def __str__(self):
			
		s = "nodos: \n"
		
		for i in range(self.Nnodos):
			x = self.obtener_coordenada_nodal(i)
			s += f"{i} : (  {x[0]}  {x[1]}  {x[2]} ) \n"
			
		s += "barras: \n"
		
		
		for barra in range(len(self.barras)):
			s += f"{barra} : [ {self.barras[barra].ni}  {self.barras[barra].nj} ]\n"
	
		s+= "\n\n"
		
	
		peso_total = Reticulado.calcular_peso_total(self)
		
		s+= f"peso_total = {peso_total} "

	
		return s

