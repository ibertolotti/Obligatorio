from requerimiento import Requerimiento
from pieza import Pieza

class Maquina:
    codigo_maquina = 0
    def __init__(self, descripcion):
        Maquina.codigo_maquina += 1

        self.__codigo = Maquina.codigo_maquina
        self.__descripcion = descripcion
        self.__requerimientos=[]
        self.costo_produccion = 0
        self.disponibilidad = False

    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def descripcion(self):
        return self.__descripcion
    
    @property
    def requerimientos(self):
        return self.__requerimientos

    def agregar_requerimiento(self, pieza, cantidad):
        requerimiento = Requerimiento(pieza, cantidad)
        self.__requerimientos.append(requerimiento)

    def costo(self):
        total = 0
        for requerimiento in self.requerimientos:
            total = total + requerimiento.pieza.costo_USD * requerimiento.cantidad_requerida 
            self.costo_produccion = total
        return self.costo_produccion
    
    def cambiar_disponibilidad(self):
        for r in self.requerimientos:
            if r.pieza.cantidad_stock >= r.cantidad_requerida:
                self.disponibilidad = True
        return self.disponibilidad  