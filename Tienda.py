from curses.ascii import isblank
from datetime import datetime
from typing_extensions import Self


class Transaccion:

    Venta = 1
    Abastecimiento = 2
    
    
    def __init__(self,tipo: int, cantidad: int):
        self._tipo = tipo
        self._cantidad = cantidad
        self._fecha = datetime.now() 


    @property
    def tipo(self):
        return self._tipo


    @tipo.setter
    def tipo(self, valor):
        if valor == 1 or valor == 2:
            self.tipo = valor  

class Libro:
    def __init__(self, isbn, titulo, precio_compra, precio_venta, cantidad_actual) -> None:
        self.isbn = isbn
        self.titulo = titulo
        self.precio_compra = precio_compra
        self.precio_venta = precio_venta
        self.cantidad_actual = cantidad_actual
        self.transaccion = list()




class Tienda:
    def __init__(self):
        self.diner_en_caja = 1000000
        self.catalogo = dict()



if __name__ == "__main__":
    trans_1 = Transaccion(Transaccion.Venta,5) 
    trans_2 = Transaccion(Transaccion.Abastecimiento,10)

    print(f"tipo t1:{trans_1.cantidad}") 
    print(f"tipo t2:{trans_2.cantidad}") 

        
