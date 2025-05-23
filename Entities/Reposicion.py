from datetime import datetime
from pieza import Pieza

class Reposicion:

    def __init__(self, cantidad_lotes, fecha_reposicion):
        self.cantidad_lotes=cantidad_lotes
        self.fecha_reposicion=datetime.now()

    def costo(self):
        return Pieza.costo_USD*Pieza.lote*self.cantidad_lotes