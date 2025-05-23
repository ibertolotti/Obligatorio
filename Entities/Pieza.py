class Pieza:
    contador_codigos=1
    def __init__(self,codigo, descripcion, costo_USD, lote, cantidad_stock):
<<<<<<< HEAD
        self.codigo = 
        self.descripcion = 
        self.costo_USD =
        self.lote =
        self.cantidad_stock = 
=======
        contador_codigos=contador_codigos+1
        
        self.codigo = int(codigo)
        self.descripcion = descripcion
        self.costo_USD = float(costo_USD)
        self.lote = int(lote)
        self.cantidad_stock = int(cantidad_stock)
>>>>>>> ebed3d25c6dbb1b7ea740c0d217b42825ba5631b
