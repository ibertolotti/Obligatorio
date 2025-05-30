from datetime import datetime

class Reposicion:
    def __init__(self, pieza, cantidad_lotes):
        self.__pieza = pieza 
        self.__cantidad_lotes = cantidad_lotes
        self.__fecha_reposicion = datetime.now()
        self.__costo_USD = self.__pieza.costo_USD() * self.__pieza.lote() * self.__cantidad_lotes

    @property
    def cantidad_lotes(self):
        return self.__cantidad_lotes
    
    @property
    def fecha_reposicion(self):
        return self.__fecha_reposicion
    
    @property
    def pieza(self):
        return self.__pieza

    # def costo(self): 
    #     return pieza().costo_USD*pieza().lote*cantidad_lotes()