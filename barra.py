import numpy as np

g = 9.81 #kg*m/s^2


class Barra(object):

	"""Constructor para una barra"""
	def __init__(self, ni, nj, R, t, E, ρ, σy):
		super(Barra, self).__init__()
		self.ni = ni
		self.nj = nj
		self.R = R
		self.t = t
		self.E = E
		self.ρ = ρ
		self.σy = σy


	def obtener_conectividad(self):
		"""Implementar"""

		return 

	def calcular_area(self):
		R = self.R
		t = self.t
		A = np.pi*(R**2 - (R-t)**2)
		
		return A

	def calcular_largo(self, reticulado):
		xi = reticulado.obtener_coordenada_nodal(self.ni)
		xj = reticulado.obtener_coordenada_nodal(self.nj)
		dif_x = xi[0]- xj[0]
		dif_y = xi[1]- xj[1]
		L = (dif_x**2 + dif_y**2)**0.5
		return L

	def calcular_peso(self, reticulado):
		L = self.calcular_largo(reticulado)
		A = self.calcular_area()
		densidad =self.p
		return densidad * A * L * g









