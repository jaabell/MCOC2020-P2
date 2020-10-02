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
        return [self.ni, self.nj]

    def calcular_area(self):
        A = np.pi*(self.R**2) - np.pi*((self.R-self.t)**2)
        return A

    def calcular_largo(self, reticulado):
        """Devuelve el largo de la barra. 
        ret: instancia de objeto tipo reticulado
        """
        xi = reticulado.obtener_coordenada_nodal(self.ni)
        xj = reticulado.obtener_coordenada_nodal(self.nj)
        dij = xi-xj
        return np.sqrt(np.dot(dij,dij))

    def calcular_peso(self, reticulado):
        """Devuelve el largo de la barra. 
        ret: instancia de objeto tipo reticulado
        """
        L = self.calcular_largo(reticulado)
        A = self.calcular_area()
        return self.ρ * A * L * g





    def obtener_rigidez(self, ret): ###3
        """Devuelve la rigidez ke del elemento. Arreglo numpy de (4x4)
        ret: instancia de objeto tipo reticulado
        """
        L = self.calcular_largo(ret)
        A = self.calcular_area()
        k = self.E * A / L
        
        xi = ret.obtener_coordenada_nodal(self.ni)
        xj = ret.obtener_coordenada_nodal(self.nj)

        dji = xj-xi

        cosθ = dji[0]/L
        senθ= dji[1]/L
        
        T_θ = np.array([ [-cosθ],   [-senθ],    [cosθ], [senθ]])
        ke = k * T_θ @ T_θ.T
        
        return ke

    def obtener_vector_de_cargas(self, ret):
        """Devuelve el vector de cargas nodales fe del elemento. Vector numpy de (4x1)
        ret: instancia de objeto tipo reticulado
        """

        W_2= self.calcular_peso(ret)/2    # Peso de la barra / 2 
        F = -W_2
        fe = (np.array([0 ,1 , 0 ,1 ]).T)*F

        return fe


    def obtener_fuerza(self, ret):
        """Devuelve la fuerza se que debe resistir la barra. Un escalar tipo double. 
        ret: instancia de objeto tipo reticulado
        """
        
        
        L = self.calcular_largo(ret)
        A = self.calcular_area()
        k = self.E * A / L
        
        xi = ret.obtener_coordenada_nodal(self.ni)
        xj = ret.obtener_coordenada_nodal(self.nj)

        dji = xj-xi
        
        cosθ = dji[0]/L
        senθ = dji[1]/L
        
        T_θ = np.array([ -cosθ,   -senθ,    cosθ, senθ])
        
        u2i   = 2*self.ni
        u2i_1 = 2*self.ni+1
        u2j   = 2*self.nj
        u2j_1 = 2*self.nj+1

        ue = np.array([ret.u[u2i], ret.u[u2i_1], ret.u[u2j], ret.u[u2j_1]])
        delta = T_θ @ ue
        se = k * delta

        return se




