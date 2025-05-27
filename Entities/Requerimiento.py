from pieza import Pieza


class Requerimiento:
    def _init_(self,pieza,cantidad_requerida):
        self.__pieza = pieza
        self.__cantidad_requerida = int(cantidad_requerida)

    @property
    def pieza(self):
        return self.__pieza
    
    @pieza.setter
    def nueva_pieza(self, nueva_pieza):
        self.__pieza = nueva_pieza

    @property
    def cantidad_requerida(self):
        return self.__cantidad_requerida
    
    @cantidad_requerida.setter
    def nueva_cantidad_requerida(self, nueva_cantidad):
        self.__cantidad_requerida = nueva_cantidad