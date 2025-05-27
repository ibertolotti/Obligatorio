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
        requerimiento = Requerimiento(self, pieza, cantidad)
        self.__requerimientos.append(requerimiento)

    #Funcion auxiliar:
    def costo(self):
        total = 0
        for requerimiento in self.requerimientos:
            total = total + requerimiento.pieza.costo_USD * requerimiento.cantidad_requerida 
        return total

    # Disponibilididad tiene que ser booleano
    # def disponibilidad(self):
    #     for requerimiento in self.requerimientos:
    #         if requerimiento.pieza.cantidad_stock < requerimiento.cantidad_requerida:
    #             return False
    #     return True


