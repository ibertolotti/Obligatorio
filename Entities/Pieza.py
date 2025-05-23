class Pieza:
    codigo_pieza = 0
    def __init__(self, descripcion, costo_USD, lote, cantidad_stock=0):
        Pieza.codigo_pieza += 1
        
        self.codigo = Pieza.codigo_pieza
        self.descripcion = descripcion
        self.costo_USD = float(costo_USD)
        self.lote = int(lote)
        self.cantidad_stock = int(cantidad_stock)