import numpy as np
from numpy.linalg import inv

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
        
        cos_theta = dji[0]/L
        sen_theta = dji[1]/L
        
        T_theta = [-cos_theta,   -sen_theta,    cos_theta, sen_theta]
        ke = T_theta.T @T_theta * k
        
        #implementar

        return ke

    def obtener_vector_de_cargas(self, ret):
        """Devuelve el vector de cargas nodales fe del elemento. Vector numpy de (4x1)
        ret: instancia de objeto tipo reticulado
        """

        W_2= self.calcular_peso(ret)/2    # Peso de la barra / 2 
        F = -W_2
        fe = ([0 ,1 , 0 ,1 ].T)*F

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
        
        cos_theta = dji[0]/L
        sen_theta = dji[1]/L
        
        T_theta = [-cos_theta,   -sen_theta, cos_theta, sen_theta]
        ke = T_theta.T @T_theta * k
        Ke_1 = inv(ke)
        
        fe= self.obtener_vector_de_cargas(ret)
        
        ue = Ke_1 @ fe
        
        delta = T_theta@ ue
        
        se = k * delta
        

        return se



