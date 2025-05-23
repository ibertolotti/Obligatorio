class Maquina:
    codigo_maquina = 0
    def __init__(self, descripcion):
        Maquina.codigo_maquina += 1

        self.codigo = Maquina.codigo_maquina
        self.descripcion = descripcion
    
    def costo_produccion(self):
        return 
