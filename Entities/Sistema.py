# from datetime import datetime
from clientes import ClienteParticular, Empresa
from pieza import Pieza
from maquina import Maquina
from pedido import Pedido
from reposicion import Reposicion
# from requerimiento import Requerimiento

class Sistema:
    def __init__(self):
        self.__lista_pieza = []
        self.__lista_maquina = []
        self.__lista_clientes = []
        self.__lista_pedido = []
        self.__lista_contabilidad = []

    @property
    def lista_pieza(self):
        return self.__lista_pieza
    
    @property
    def lista_maquina(self):
        return self.__lista_maquina
    
    @property
    def lista_clientes(self):
        return self.__lista_clientes
    
    @property
    def lista_pedido(self):
        return self.__lista_pedido
    
    @property
    def lista_contabilidad(self):
        return self.__lista_contabilidad

    def registrar_pieza(self, descripcion, costo_USD, lote, cantidad_stock=0):
        pieza = Pieza(descripcion, costo_USD, lote, cantidad_stock)
        self.lista_pieza.append(pieza)
        return self.lista_pieza

    def registrar_maquina(self, descripcion):
        maquina = Maquina(descripcion)
        return maquina
    
    def registrar_cliente_particular(self, telefono, correo, cedula, nombre_completo):
        cliente_particular = ClienteParticular(telefono, correo, cedula, nombre_completo)
        self.lista_clientes.append(cliente_particular)
        return self.lista_clientes
    
    def registrar_empresa(self, telefono, correo, rut, nombre, web):
        cliente_empresa = Empresa(telefono, correo, rut, nombre, web)
        self.lista_clientes.append(cliente_empresa)
        return self.lista_clientes
    
    def registrar_pedido(self, cliente, maquina):
        pedido = Pedido(cliente, maquina)
        self.lista_pedido.append(pedido)
        return self.lista_pedido
    
    def registrar_reposicion(self, pieza, cantidad_lotes):
        reposicion = Reposicion(pieza, cantidad_lotes)
        return reposicion