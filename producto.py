class Producto():
    stock = 0
    def __init__(self, nombre_producto: str, precio_producto: int, stock: int):
        self.__nombre_producto = nombre_producto
        self.__precio_producto = precio_producto
        self.__stock = stock

    @property
    def get_nombre_producto(self):
        return self.__nombre_producto
    
    @property
    def get_precio_producto(self):
        return self.__precio_producto
    
    @property
    def get_stock(self):
        return self.__stock
    
    @get_nombre_producto.setter
    def set_nombre_producto(self, nombre: str):
        self.__nombre_producto = nombre

    @get_precio_producto.setter
    def set_precio_producto(self, precio: int):
        self.__precio_producto = precio
    
    @get_stock.setter
    def set_stock(self, stock: int):
        self.__stock = stock
        if stock < 0:
            stock == 0 
