class Pieza:
    codigo_pieza = 0
    def __init__(self, descripcion, costo_USD, lote, cantidad_stock=0):
        Pieza.codigo_pieza += 1
        
        self.__codigo = Pieza.codigo_pieza
        self.__descripcion = descripcion
        self.__costo_USD = costo_USD
        self.__lote = lote
        self.__cantidad_stock = cantidad_stock

    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def descripcion(self):
        return self.__descripcion
    
    @property
    def costo_USD(self):
        return self.__costo_USD
    
    @property
    def lote(self):
        return self.__lote
    
    @property
    def cantidad_stock(self):
        return self.__cantidad_stock
    
    @cantidad_stock.setter
    def cantidad_stock(self, stock_nuevo):
        self.__cantidad_stock = stock_nuevo