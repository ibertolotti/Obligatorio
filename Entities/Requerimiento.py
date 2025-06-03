class Requerimiento:
    def __init__(self, pieza, cantidad_requerida):
        self.__pieza = pieza
        self.__cantidad_requerida = int(cantidad_requerida)

    @property
    def pieza(self):
        return self.__pieza

    @property
    def cantidad_requerida(self):
        return self.__cantidad_requerida
    
    @pieza.setter
    def pieza(self, nueva_pieza):
        self.__pieza = nueva_pieza
    
    @cantidad_requerida.setter
    def cantidad_requerida(self, nueva_cantidad_requerida):
        self.__cantidad_requerida = nueva_cantidad_requerida