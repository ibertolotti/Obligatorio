from requerimiento import Requerimiento
from pieza import Pieza

class Maquina:
    codigo_maquina = 0

    def __init__(self, descripcion):
        Maquina.codigo_maquina += 1

        self.codigo = Maquina.codigo_maquina
        self.descripcion = descripcion
        self.requerimientos=[]

    # def costo_produccion(self):
    #     total = 0
    #     for pieza,cantidad_requerida in self.requerimientos:
    #         total = total + pieza.costo_USD * cantidad_requerida 

    # def disponibilidad(self):
    #     for requerimiento in self.requerimientos:
    #         if requerimiento.pieza.cantidad_stock < requerimiento.cantidad_requuerida:
    #             return False
    #     return true

    def agregar_requerimiento(self, pieza, cantidad):
        requerimiento = Requerimiento(self, pieza, cantidad)
        self.requerimientos.append(requerimiento)