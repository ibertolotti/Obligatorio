from datetime import datetime
# from clientes import Cliente
# from maquina import Maquina

class Pedido:
    def __init__(self, cliente, maquina, estado):
        self.__cliente = cliente
        self.__maquina = maquina
        self.__fecha_realizado = datetime.now()
        # self.__fecha_entregado = 
        self.__estado = estado

    @property
    def cliente(self):
        return self.__cliente

    @property
    def maquina(self):
        return self.__maquina

    # @property
    # def fecha_realizado(self):
    #     return fecha_realizado

    # @property
    # def fecha_entregado(self):
    #     return fecha_entregado

    @property
    def estado(self):
        return self.__estado
    
    # def precio(self):
    #     #primero hay que terminar el costo de produccion de maquina.