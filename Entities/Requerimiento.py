from pieza import Pieza
from maquina import Maquina

class Requerimiento:
    def __init__(self,pieza,cantidad):
        self.pieza = pieza
        self.maquina = Maquina()