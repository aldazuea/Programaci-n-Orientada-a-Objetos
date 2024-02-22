class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def eliminar_producto(self, id):
        for producto in self.productos:
            if producto.get_id() == id:
                self.productos.remove(producto)
                break

    def actualizar_cantidad(self, id, cantidad):
        for producto in self.productos:
            if producto.get_id() == id:
                producto.set_cantidad(cantidad)
                break

    def actualizar_precio(self, id, precio):
        for producto in self.productos:
            if producto.get_id() == id:
                producto.set_precio(precio)
                break

    def buscar_producto_por_nombre(self, nombre):
        productos_encontrados = []
        for producto in self.productos:
            if nombre.lower() in producto.get_nombre().lower():
                productos_encontrados.append(producto)
        return productos_encontrados

    def mostrar_productos(self):
        for producto in self.productos:
            print("ID:", producto.get_id())
            print("Nombre:", producto.get_nombre())
            print("Cantidad:", producto.get_cantidad())
            print("Precio:", producto.get_precio())
            print("------------------")


# Interfaz de Usuario en la Consola
inventario = Inventario()

while True:
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar cantidad de producto")
    print("4. Actualizar precio de producto")
    print("5. Buscar productos por nombre")
    print("6. Mostrar todos los productos")
    print("7. Salir")

    opcion = int(input("Ingresa una opción: "))
    print()

    if opcion == 1:
        id = int(input("Ingresa el ID del producto: "))
        nombre = input("Ingresa el nombre del producto: ")
        cantidad = int(input("Ingresa la cantidad del producto: "))
        precio = float(input("Ingresa el precio del producto: "))

        producto = Producto(id, nombre, cantidad, precio)
        inventario.agregar_producto(producto)
        print("Producto agregado correctamente.")

    elif opcion == 2:
        id = int(input("Ingresa el ID del producto a eliminar: "))
        inventario.eliminar_producto(id)
        print("Producto eliminado correctamente.")

    elif opcion == 3:
        id = int(input("Ingresa el ID del producto a actualizar: "))
        cantidad = int(input("Ingresa la nueva cantidad del producto: "))
        inventario.actualizar_cantidad(id, cantidad)
        print("Cantidad actualizada correctamente.")

    elif opcion == 4:
        id = int(input("Ingresa el ID del producto a actualizar: "))
        precio = float(input("Ingresa el nuevo precio del producto: "))
        inventario.actualizar_precio(id, precio)
        print("Precio actualizado correctamente.")

    elif opcion == 5:
        nombre = input("Ingresa el nombre del producto a buscar: ")
        productos_encontrados = inventario.buscar_producto_por_nombre(nombre)
        if len(productos_encontrados) > 0:
            print("Productos encontrados:")
            for producto in productos_encontrados:
                print("ID:", producto.get_id())
                print("Nombre:", producto.get_nombre())
                print("Cantidad:", producto.get_cantidad())
                print("Precio:", producto.get_precio())
                print("------------------")
        else:
            print("No se encontraron productos con ese nombre.")

    elif opcion == 6:
        inventario.mostrar_productos()

    elif opcion == 7:
        break

    print()