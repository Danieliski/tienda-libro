
from datetime import datetime
from functools import reduce
from logging import exception



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


    @property
    def cantidad(self):
       return self._cantidad


    @property
    def fecha(self):
        return self._fecha      

class Libro:
    def __init__(self, isbn, titulo, precio_compra, precio_venta, cantidad_actual) -> None:
        self.isbn = isbn
        self.titulo = titulo
        self.precio_compra = precio_compra
        self.precio_venta = precio_venta
        self.cantidad_actual = cantidad_actual
        self.Transaccion = list()


    @property
    def cantidad_actual(self):
        return self._cantidad_actual


    @cantidad_actual.setter
    def cantidad_actual(self, nueva_cantidad):
        if nueva_cantidad < 0:
            raise exception("la cantidad de unidades de un libro no puede ser negativa")  

        self._cantidad_actual = nueva_cantidad   

    def vender(self, cantidad) -> bool:
        """
        Este metodo vende una catidad dada de ejemplares del libro. si no hay esa cantidad, no se realiza la venta y el metodo returna false, si la venta se realiza, el metodo returna True
        """
        if self.cantidad_actual >= cantidad:
            self.cantidad_actual -= cantidad
            transaccion = Transaccion(Transaccion.venta, cantidad)
            self.Transaccion.append(Transaccion)
            return True
        else:
            return False

    def abastecer(self, cantidad):
        self.cantidad_actual += cantidad
        Transaccion = Transaccion(Transaccion.Abastecimiento, cantidad)
        self.Transaccion.append(Transaccion)

    def informar_ejemplares_venta(self) -> int:
        if len(self, transacciones) > 0:
            
            # cantidades=[t.cantidad for t in self. transacciones if t.tipo == Transaccion.Venta]
            # total_ejemplares = reduce(lambda x, y: x + y, cantidad)
            # return total_ejemplares
            
            cantidad_ejemplares = 0
            for trans in self,transacciones: 
                if trans.tipo == Transaccion.Venta:
                    cantidad_ejemplares += trans.cantidad 
            return cantidad_ejemplares
        else:
            return 0


    def __str__(self) -> str:
        return f"ISBN: {self.isbn}\nTitulo: {self.titulo}"        
                      



class Tienda:
    def __init__(self):
        self.diner_en_caja = 1000000
        self.catalogo = dict()

    def register_libro_en_catalogo(self, titulo, isbn, precio_venta, precio_compra, cantidad_actual): 
        if isbn not in self.catalogo.keys():
            libro = Libro( titulo, isbn, precio_venta, precio_compra, cantidad_actual)
            self.catalogo[isbn] = libro

        else:
            raise Exception(f"ya existe un libro con el isbn")

    def eliminar_libro_de_catalogo(self, isbn):
        if isbn in self.catalogo.keys():
            del self.catalogo[isbn]
        else:
            raise Exception(f"no existe un libro con el isbn")             


libro = Libro("1234","El principito", 50000, 60000, 10)





        
