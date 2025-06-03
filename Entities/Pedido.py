from datetime import datetime
from clientes import ClienteParticular, Empresa
from maquina import Maquina

class Pedido:
    def __init__(self, cliente, maquina):
        self.__cliente = cliente
        self.__maquina = maquina
        self.__fecha_realizado = datetime.now()
        self.__fecha_entregado = 0
        self.__estado = ""
        self.precio_pedido = 0

    @property
    def cliente(self):
        return self.__cliente

    @property
    def maquina(self):
        return self.__maquina

    @property
    def fecha_realizado(self):
        return self.__fecha_realizado

    @property
    def fecha_entregado(self):
        return self.__fecha_entregado

    @property
    def estado(self):
        return self.__estado
    
    @fecha_entregado.setter
    def fecha_entregado(self, fecha):
        self.__fecha_entregado = fecha

    @estado.setter
    def estado(self, estado):
        self.__estado = estado