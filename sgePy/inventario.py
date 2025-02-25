inventario = []  # Lista para almacenar productos

def agregar_producto():
    codigo = input("Código del producto: ")
    nombre = input("Nombre del producto: ")
    cantidad = int(input("Cantidad en stock: "))
    precio = float(input("Precio unitario: "))

    producto = {"codigo": codigo, "nombre": nombre, "cantidad": cantidad, "precio": precio}
    inventario.append(producto)

    print("✅ Producto agregado al inventario.\n")

def listar_productos():
    if not inventario:
        print("⚠️ No hay productos en el inventario.\n")
        return

    print("\n📦 Inventario de Productos:")
    for producto in inventario:
        print(f"{producto['codigo']} - {producto['nombre']} | Stock: {producto['cantidad']} | Precio: ${producto['precio']}")
    print()
