from abc import ABC, abstractmethod

class Producto(ABC):
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio

    @abstractmethod
    def mostrarinfo(self):
        pass

    @property
    def precio(self):
        return self._precio
    
    @property
    def nombre(self):
        return self._nombre
    
class Camisa(Producto):
    def mostrarinfo(self):
        print(f'Camisa: {self._nombre}, Precio: ₲{self._precio:.2f}')

class Pantalon(Producto):
    def mostrarinfo(self):
        print(f'Pantalón: {self._nombre}, Precio: ₲{self._precio:.2f}')

class Zapato(Producto):
    def mostrarinfo(self):
        print(f'Zapato: {self._nombre}, Precio: ₲{self._precio:.2f}')

class Categoria:
    def __init__(self, nombre):
        self._nombre = nombre
        self._productos = []
        
    def agregar_productos(self, producto):
        self._productos.append(producto)

    def mostrar_productos(self):
        print(f'\nCategoría: {self._nombre}')
        for idx, producto in enumerate(self._productos, 1):
            producto.mostrarinfo()
            print(f'[{idx}]')  

class Tienda:
    def __init__(self, nombre):
        self._nombre = nombre
        self.categorias = []
        self.total = 0 

    def agregar_categorias(self, categoria):
        self.categorias.append(categoria)
        
    def mostrar_categorias(self):
        print(f'{self._nombre}')
        for idx, categoria in enumerate(self.categorias, 1):
            print(f'{idx}. {categoria._nombre}')   

    def mostrar_productos_categoria(self, indice):
        if 0 <= indice < len(self.categorias):
            self.categorias[indice].mostrar_productos()
        else:
            print("Categoría no válida.")

    def procesar_compra(self, categoria_idx, producto_idx):
        categoria = self.categorias[categoria_idx]
        producto = categoria._productos[producto_idx]
        self.total += producto.precio  
        print(f"\nAgregado: {producto.nombre} por ₲{producto.precio:.2f}")    

    def mostrar_total(self):
        print(f'Total a pagar: ₲{self.total:.2f}') 

    def reset_total(self):
        self.total = 0  

camisa1 = Camisa("Camisa de Algodón", 25000)
camisa2 = Camisa("Camisa Formal", 45000)
pantalon1 = Pantalon("Vaqueros", 60000)
pantalon2 = Pantalon("Pantalón de Vestir", 65000)
zapato1 = Zapato("Zapatos Deportivos", 70000)
zapato2 = Zapato("Zapatos de Vestir", 90000)

categoria_camisas = Categoria("Camisas")
categoria_camisas.agregar_productos(camisa1)
categoria_camisas.agregar_productos(camisa2)

categoria_pantalones = Categoria("Pantalones")
categoria_pantalones.agregar_productos(pantalon1)
categoria_pantalones.agregar_productos(pantalon2)

categoria_zapatos = Categoria("Zapatos")
categoria_zapatos.agregar_productos(zapato1)
categoria_zapatos.agregar_productos(zapato2)

tienda = Tienda("Todo x menos de 100mil")
tienda.agregar_categorias(categoria_camisas)
tienda.agregar_categorias(categoria_pantalones)
tienda.agregar_categorias(categoria_zapatos)

while True:
    tienda.mostrar_categorias()
    try:
        seleccion_categoria = int(input("\nSeleccione una categoría ")) - 1
        if seleccion_categoria == -1:
            print('Gracias por su compra')
            break  
        
        if not (0 <= seleccion_categoria < len(tienda.categorias)):
            print("Seleccione una opción válida")
            continue

        tienda.mostrar_productos_categoria(seleccion_categoria)
        
        productos_seleccionados = []  

        while True:
            seleccion_producto = int(input("\nSeleccione el número del producto que desea agregar (0 para finalizar) ")) - 1
            if seleccion_producto == -1:
                break  
            
            if not (0 <= seleccion_producto < len(tienda.categorias[seleccion_categoria]._productos)):
                print("Producto no válido, ingrese un número válido")
                continue
            
            tienda.procesar_compra(seleccion_categoria, seleccion_producto)  

        tienda.mostrar_total()
        tienda.reset_total()  
    except ValueError:
        print('Seleccione un número válido')
