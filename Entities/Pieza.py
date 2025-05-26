class Pieza:
    codigo_pieza = 0
    def __init__(self, descripcion, costo_USD, lote, cantidad_stock=0):
        Pieza.codigo_pieza += 1
        
        self.__codigo = Pieza.codigo_pieza
        self.__descripcion = descripcion
        self.__costo_USD = float(costo_USD)
        self.__lote = int(lote)
        self.__cantidad_stock = int(cantidad_stock)

    #GETTERS
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
    
    #SETTERS
    @descripcion.setter
    def cambiar_descripcion(self, descripcion_nueva):
        self.__descripcion=descripcion_nueva 

    @costo_USD.setter
    def cambiar_costo(self, costo_USD_nuevo):
        self.__costo_USD=costo_USD_nuevo

    @lote.setter
    def cambiar_lote(self, lote_nuevo):
        self.__lote=lote_nuevo

    @cantidad_stock.setter
    def cambiar_cantidad_stock(self, stock_nuevo):
        self.__cantidad_stock=stock_nuevo

#Capaz que aumentar stock tiene que estar en sistema:
    def aumentar_stock(self, cantidad_lotes):
        self.__cantidad_stock = self.__cantidad_stock + cantidad_lotes*self.lote
        return cantidad_lotes