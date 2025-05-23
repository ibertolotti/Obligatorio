class Pieza:
    contador_codigos = 0
    def __init__(self, descripcion, costo_USD, lote, cantidad_stock=0):
        Pieza.contador_codigos += 1
        
        self.codigo = Pieza.contador_codigos
        self.descripcion = descripcion
        self.costo_USD = float(costo_USD)
        self.lote = int(lote)
        self.cantidad_stock = int(cantidad_stock)

