from registro import registrar_cliente
from inventario import agregar_producto, listar_productos
from facturacion import crear_factura

def menu():
    while True:
        print("\n📌 MENÚ PRINCIPAL")
        print("1. Registrar Cliente")
        print("2. Agregar Producto al Inventario")
        print("3. Listar Productos")
        print("4. Crear Factura")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")
        print()

        if opcion == "1":
            registrar_cliente()
        elif opcion == "2":
            agregar_producto()
        elif opcion == "3":
            listar_productos()
        elif opcion == "4":
            crear_factura()
        elif opcion == "5":
            print("👋 Saliendo del programa...")
            break
        else:
            print("⚠️ Opción no válida, intente de nuevo.\n")

# 🔥 Iniciar el menú
menu()
