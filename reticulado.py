import numpy as np
from scipy.linalg import solve

class Reticulado(object):
	"""Define un reticulado"""
	__NNodosInit__ = 100

	def __init__(self):
		super(Reticulado, self).__init__()
		
		self.xyz = np.zeros((Reticulado.__NNodosInit__,3), dtype=np.double)
		self.Nnodos = 0
		self.barras = []
		self.cargas = {}
		self.restricciones = {}
		self.Ndimensiones = 2
		self.has_solution = False

	def agregar_nodo(self, x, y, z=0):
		if self.Nnodos+1 > Reticulado.__NNodosInit__:
			self.xyz.resize((self.Nnodos+1,3))
		self.xyz[self.Nnodos,:] = [x, y, z]
		self.Nnodos += 1
		if z != 0.:
			self.Ndimensiones = 3

	def agregar_barra(self, barra):
		self.barras.append(barra)

	def obtener_coordenada_nodal(self, n):
		if n >= self.Nnodos:
			return 
		return self.xyz[n, :]

	def calcular_peso_total(self):
		peso = 0.
		for b in self.barras:
			peso += b.calcular_peso(self)
		return peso

	def obtener_nodos(self):
		return self.xyz[0:self.Nnodos,:].copy()

	def obtener_barras(self):
		return self.barras








	def agregar_restriccion(self, nodo, gdl, valor=0.0):

		if nodo not in self.restricciones:
			self.restricciones[nodo] = [[gdl, valor]]
		else:
			self.restricciones[nodo].append([gdl, valor])


	def agregar_fuerza(self, nodo, gdl, valor):
		"""
		Agrega una fuerza al sistema en el 'nodo', 
		y 'gdl' especificados con el 'valor' dado. 
		"""
		if nodo not in self.cargas:
			self.cargas[nodo] = [[gdl, valor]]
		else:
			self.cargas[nodo].append([gdl, valor])


	def ensamblar_sistema(self):
		
		Ngdl = self.Nnodos * self.Ndimensiones

		self.K = np.zeros((Ngdl,Ngdl), dtype=np.double)
		self.f = np.zeros((Ngdl), dtype=np.double)
		self.u = np.zeros((Ngdl), dtype=np.double)

		#Iterar sobre las barras:
		for i,b in enumerate(self.barras):
			ke = b.obtener_rigidez(self)
			fe = b.obtener_vector_de_cargas(self) 

			ni, nj = b.obtener_conectividad()


			#MDR
			if self.Ndimensiones == 2:
				d = [2*ni, 2*ni+1, 2*nj, 2*nj+1]
			else:
				d = [3*ni, 3*ni+1, 3*ni+2 , 3*nj, 3*nj+1, 3*nj+2]

			for i in range(self.Ndimensiones*2):  
				p = d[i]
				for j in range(self.Ndimensiones*2):
					q = d[j]
					self.K[p,q] += ke[i,j]
				self.f[p] = fe[i]
		




	def resolver_sistema(self):

		# 0 : Aplicar restricciones
		Ngdl = self.Nnodos * self.Ndimensiones
		gdl_libres = np.arange(Ngdl)
		gdl_restringidos = []

		#Pre-llenar el vector u

		for nodo in self.restricciones:
			for restriccion in self.restricciones[nodo]:
				gdl = restriccion[0]
				valor = restriccion[1]

				gdl_global = self.Ndimensiones*nodo + gdl
				self.u[gdl_global] = valor

				gdl_restringidos.append(gdl_global)

		# con gdl_restringidos encuentro  gdl_libres
		gdl_restringidos = np.array(gdl_restringidos)
		gdl_libres = np.setdiff1d(gdl_libres, gdl_restringidos)


		for nodo in self.cargas:
			for carga in self.cargas[nodo]:
				gdl = carga[0]
				valor = carga[1]

				gdl_global = self.Ndimensiones*nodo + gdl
				self.f[gdl_global] = valor


		#1 Particionar:


		Kff = self.K[np.ix_(gdl_libres, gdl_libres)]
		Kfc = self.K[np.ix_(gdl_libres, gdl_restringidos)]
		Kcf = Kfc.T
		Kcc = self.K[np.ix_(gdl_restringidos, gdl_restringidos)]
 
		uf = self.u[gdl_libres]
		uc = self.u[gdl_restringidos]

		ff = self.f[gdl_libres]
		fc = self.f[gdl_restringidos]

		# Solucionar Kff uf = ff
		uf = solve(Kff, ff - Kfc @ uc)

		self.u[gdl_libres] = uf

		self.has_solution = True



	def obtener_desplazamiento_nodal(self, n):
		if self.Ndimensiones == 2:
			dofs = [2*n, 2*n+1]
		else: 
			dofs = [3*n, 3*n+1, 3*n+2]
		return self.u[dofs]


	def recuperar_fuerzas(self):
		
		fuerzas = np.zeros((len(self.barras)), dtype=np.double)
		for i,b in enumerate(self.barras):
			fuerzas[i] = b.obtener_fuerza(self)

		return fuerzas


	def recuperar_factores_de_utilizacion(self, f):
		
		FU = np.zeros((len(self.barras)), dtype=np.double)
		for i,b in enumerate(self.barras):
			FU[i] = b.obtener_factor_utilizacion(f[i])

		return FU



	def rediseñar(self, Fu, ϕ=0.9):
		for i,b in enumerate(self.barras):
			b.rediseñar(Fu, self, ϕ)













	def __str__(self):
		s = "nodos:\n"
		for n in range(self.Nnodos):
			s += f"  {n} : ( {self.xyz[n,0]}, {self.xyz[n,1]}, {self.xyz[n,2]}) \n "
		s += "\n\n"

		s += "barras:\n"
		for i, b in enumerate(self.barras):
			n = b.obtener_conectividad()
			s += f" {i} : [ {n[0]} {n[1]} ] \n"
		s += "\n\n"
		
		s += "restricciones:\n"
		for nodo in self.restricciones:
			s += f"{nodo} : {self.restricciones[nodo]}\n"
		s += "\n\n"
		
		s += "cargas:\n"
		for nodo in self.cargas:
			s += f"{nodo} : {self.cargas[nodo]}\n"
		s += "\n\n"

		if self.has_solution:
			s += "desplazamientos:\n"
			if self.Ndimensiones == 2:
				uvw = self.u.reshape((-1,2))
				for n in range(self.Nnodos):
					s += f"  {n} : ( {uvw[n,0]}, {uvw[n,1]}) \n "
		s += "\n\n"

		if self.has_solution:
			f = self.recuperar_fuerzas()
			s += "fuerzas:\n"
			for b in range(len(self.barras)):
				s += f"  {b} : {f[b]}\n"
		s += "\n"
		s += f"Ndimensiones = {self.Ndimensiones}"

		return s
