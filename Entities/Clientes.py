from abc import ABC, abstractmethod

class Cliente(ABC):
    contador_id=0
    def __init__(self, telefono, correo):
        Cliente.contador_id += 1
        self.__id = Cliente.contador_id
        self.__telefono = telefono
        self.__correo = correo

    @property
    def id(self):
        return self.__id
    
    @property
    def telefono(self):
        return self.__telefono
    
    @property
    def correo(self):
        return self.__correo

class ClienteParticular(Cliente):
    def __init__(self, telefono, correo, cedula, nombre_completo):
        super().__init__(telefono, correo)
        self.__cedula = cedula
        self.__nombre_completo = nombre_completo

    @property
    def cedula(self):
        return self.__cedula
    
    @property
    def nombre_completo(self):
        return self.__nombre_completo
    
class Empresa(Cliente):
    def __init__(self, telefono, correo, rut, nombre, web):
        super().__init__(telefono, correo)
        self.__rut = rut
        self.__nombre= nombre
        self.__web = web

    @property
    def rut(self):
        return self.__rut
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def web(self):
        return self.__web