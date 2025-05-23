from requerimiento import Requerimiento
class Maquina:
    codigo_maquina = 0
    def __init__(self, descripcion):
        Maquina.codigo_maquina += 1

        self.codigo = Maquina.codigo_maquina
        self.descripcion = descripcion
        self.requerimientos=[]
    
    def agregar_requerimiento(self, pieza, cantidad):
        requerimiento = Requerimiento(self, pieza, cantidad)
        self.requerimientos.append(requerimiento)

