clientes = []  # Lista para almacenar clientes

def registrar_cliente():
    nombre = input("Nombre del cliente: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")

    cliente = {"nombre": nombre, "telefono": telefono, "email": email}
    clientes.append(cliente)

    print("✅ Cliente registrado con éxito.\n")

def listar_clientes():
    if not clientes:
        print("⚠️ No hay clientes registrados.\n")
        return
    
    print("\n📋 Lista de Clientes:")
    for i, cliente in enumerate(clientes):
        print(f"{i+1}. {cliente['nombre']} - {cliente['telefono']}")
    print()
