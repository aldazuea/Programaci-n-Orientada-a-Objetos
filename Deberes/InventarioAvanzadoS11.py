if opcion == 1:
    id = int(input("Ingrese el ID del producto: "))
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad del producto: "))
    precio = float(input("Ingrese el precio del producto: "))
    producto = Producto(id, nombre, cantidad, precio)
    inventario.agregar_producto(producto)

elif opcion == 2:
    id = int(input("Ingrese el ID del producto a eliminar: "))
    inventario.eliminar_producto(id)

elif opcion == 3:
    id = int(input("Ingrese el ID del producto a actualizar cantidad: "))
    cantidad = int(input("Ingrese la nueva cantidad: "))
    inventario.actualizar_cantidad(id, cantidad)

elif opcion == 4:
    id = int(input("Ingrese el ID del producto a actualizar precio: "))
    precio = float(input("Ingrese el nuevo precio: "))
    inventario.actualizar_precio(id, precio)

elif opcion == 5:
    nombre = input("Ingrese el nombre del producto a buscar: ")
    inventario.buscar_producto_por_nombre(nombre)

elif opcion == 6:
    inventario.mostrar_inventario()

elif opcion == 7:
    guardar_inventario(inventario)
    print("Inventario guardado exitosamente!")

elif opcion == 8:
    inventario = cargar_inventario()
    print("Inventario cargado exitosamente!")

elif opcion == 9:
    break

else:
    print("Opción inválida. Inténtelo de nuevo.")
