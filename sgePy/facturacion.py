from registro import clientes, listar_clientes
from inventario import inventario, listar_productos

facturas = []  # Lista para almacenar facturas

def crear_factura():
    if not clientes:
        print("⚠️ No hay clientes registrados.\n")
        return

    if not inventario:
        print("⚠️ No hay productos en el inventario.\n")
        return

    listar_clientes()
    cliente_idx = int(input("Seleccione un cliente (número): ")) - 1
    if cliente_idx < 0 or cliente_idx >= len(clientes):
        print("⚠️ Selección inválida.\n")
        return
    
    cliente = clientes[cliente_idx]
    items = []

    while True:
        listar_productos()
        codigo = input("Ingrese el código del producto a facturar (o '0' para terminar): ")
        if codigo == "0":
            break
        
        producto = next((p for p in inventario if p["codigo"] == codigo), None)
        if not producto:
            print("⚠️ Producto no encontrado.\n")
            continue

        cantidad = int(input(f"Cantidad de {producto['nombre']} a comprar: "))
        if cantidad > producto["cantidad"]:
            print("⚠️ Stock insuficiente.\n")
            continue

        producto["cantidad"] -= cantidad  # Restar del inventario
        items.append({"nombre": producto["nombre"], "cantidad": cantidad, "precio": producto["precio"]})

    if not items:
        print("⚠️ Factura vacía, no se generó.\n")
        return

    factura = {"cliente": cliente, "items": items}
    facturas.append(factura)

    print("\n🧾 Factura generada con éxito:")
    print(f"Cliente: {cliente['nombre']} - {cliente['telefono']}")
    total = sum(item["cantidad"] * item["precio"] for item in items)
    for item in items:
        print(f"{item['cantidad']}x {item['nombre']} - ${item['precio']} c/u")
    print(f"Total: ${total}\n")
