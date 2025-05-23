from datetime import datetime
from pieza import Pieza

class Reposicion:

    def __init__(self, cantidad_lotes):
        self.__cantidad_lotes=cantidad_lotes
        self.__fecha_reposicion=datetime.now()

    @property
    def cantidad_lotes(self):
        return self.__cantidad_lotes
    
    @property
    def fecha_reposicion(self):
        return self.__fecha_reposicion

    def costo(self):
        return Pieza.costo_USD*Pieza.lote*self.cantidad_lotes