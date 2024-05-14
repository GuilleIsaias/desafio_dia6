from abc import ABC, abstractmethod
from producto import Producto
class Tienda(ABC):

    def __init__(self, nombre_tienda: str, costo_delivery: int):
        self.__nombre_tienda = nombre_tienda
        self.__productos = []
        self.__costo_delivery = costo_delivery

    @property
    def get_nombre_tienda(self):
        return self.__nombre_tienda
    
    @property
    def get_productos(self):
        return self.__productos
    
    @property
    def get_costo_delivery(self):
        return self.__costo_delivery

    def agregar_productos(self, productos: Producto):
        self.__productos.append(productos)
        return self.__productos

    '''def nueva_tienda(self, nombre: str, costo: int):
        self.__nombre_tienda = nombre
        self.__costo_delivery = costo
        return self.__nombre_tienda, self.__costo_delivery'''
    
    def listar_productos():
        

    def venta(self):
        pass

class TiendaRestaurante(Tienda):
    nombre = "Restaurante"
    costo_delivery = 1500
    def __init__(self):
        self.__items = []

    def agregar_items(self):
        self.__items = Tienda.agregar_productos()
        return self.__items
    
class TiendaSupermercado(Tienda):
    nombre = "Supermercado"
    costo_delivery = 2000
    def __init__(self):
        self.__items = []

    def agregar_items(self):
        self.__items = Tienda.agregar_productos()
        return self.__items
    
class TiendaFarmacia(Tienda):
    nombre = "Farmacia"
    costo_delivery = 1000
    def __init__(self):
        self.__items = []

    def agregar_items(self):
        self.__items = Tienda.agregar_productos()
        return self.__items
    

    





