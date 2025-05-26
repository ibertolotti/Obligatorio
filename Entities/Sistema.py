from datetime import datetime
from clientes import ClienteParticular, Empresa
from pieza import Pieza
from maquina import Maquina
from pedido import Pedido
from reposicion import Reposicion
from requerimiento import Requerimiento

class Sistema:
    def __init__(self):
        self.lista_pieza = []
        self.lista_maquina = []
        self.lista_cliente_particular = []
        self.lista_empresa = []
        self.lista_pedido = []
        self.lista_contabilidad=[]


    def registrar_pieza(self, descripcion, costo_USD, lote, cantidad_stock=0):
        pieza = Pieza(descripcion, costo_USD, lote, cantidad_stock)
        self.lista_pieza.append(pieza)
        return pieza

    def registrar_maquina(self, descripcion, all_requerimientos):
        maquina=Maquina(descripcion)
        for pieza, cantidad in all_requerimientos:
            maquina.agregar_requerimiento(pieza, cantidad)
        self.lista_maquina.append(maquina)
        return maquina
    
    def registrar_cliente_particular(self, telefono, correo, cedula, nombre_completo):
        cliente_particular=ClienteParticular(telefono, correo, cedula, nombre_completo)
        self.lista_cliente_particular.append(cliente_particular)
        return cliente_particular
    
    def registrar_empresa(self, telefono, correo, rut, nombre, web):
        cliente_empresa=Empresa(telefono, correo, rut, nombre, web)
        self.lista_empresa.append(cliente_empresa)
        return cliente_empresa
    
    def registrar_pedido(self, cliente, maquina, estado):
        
        pedido=Pedido(cliente, maquina, estado)
        self.lista_pedido.append(pedido)
        return pedido