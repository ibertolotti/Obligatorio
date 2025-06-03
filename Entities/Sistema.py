# from datetime import datetime
from clientes import ClienteParticular, Empresa
from pieza import Pieza
from maquina import Maquina
from pedido import Pedido
from reposicion import Reposicion
from exceptionClienteYaExiste import ExceptionClienteYaExiste
from exceptionTipoDeDato import ExceptionTipoDeDato
from exceptionPiezaYaExiste import ExceptionPiezaYaExiste
# from requerimiento import Requerimiento

class Sistema:
    def __init__(self):
        self.__lista_pieza = []
        self.__lista_maquina = []
        self.__lista_clientes = []
        self.__lista_pedido = []
        self.__lista_contabilidad = []

    #Getters
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
        for a in self.lista_pieza:
            if a.descripcion==descripcion:
                raise ExceptionPiezaYaExiste
            
        if isinstance(descripcion, str):
            pass
        else:
            raise ExceptionTipoDeDato
            
        if isinstance(costo_USD, float) and costo_USD>0:
            pass
        elif isinstance(costo_USD, int) and costo_USD>0:
            costo_USD=float(costo_USD)
        else:
            raise ExceptionTipoDeDato
        
        if isinstance(lote, int) and lote>0:
            pass
        else:
            raise ExceptionTipoDeDato
        
        if isinstance(cantidad_stock, int) and cantidad_stock>0:
            pass
        else:
            raise ExceptionTipoDeDato

        pieza = Pieza(descripcion, costo_USD, lote, cantidad_stock)
        self.lista_pieza.append(pieza)
        return self.lista_pieza

    def registrar_maquina(self, descripcion):
        maquina = Maquina(descripcion)
        for req in maquina.requerimientos:
            if req.pieza.cantidad_stock >= req.cantidad_requerida:
                maquina.disponibilidad = True
        return maquina
    
    def registrar_cliente_particular(self, telefono, correo, cedula, nombre_completo):
        for c in self.lista_clientes:
            if c.cedula==cedula:
                raise ExceptionClienteYaExiste
        cliente_particular = ClienteParticular(telefono, correo, cedula, nombre_completo)
        self.lista_clientes.append(cliente_particular)
        return self.lista_clientes
    
    
    def registrar_empresa(self, telefono, correo, rut, nombre, web):
        for e in self.lista_clientes:
            if e.rut==rut:
                raise ExceptionClienteYaExiste
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