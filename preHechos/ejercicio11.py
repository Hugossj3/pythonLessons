# definir una función que reciba una lista de productos y un producto, y agregue el producto a la lista
def agregar_producto(productos, producto):
 productos.append(producto)
 print(f"Producto {producto} agregado a la lista.")
# llama a la función agregar_producto con los siguientes argumentos 
productos = ["manzana", "banana"]
agregar_producto(productos, "naranja")

# imprime la lista productos
print(productos)
