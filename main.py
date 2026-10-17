expedientes = []

def registrar_expediente():
    print("\n--- 1. REGISTRAR NUEVO EXPEDIENTE ---")
    codigo = input("Ingrese el código único: ").strip()
    if not codigo:
        print("Error: El código no puede estar vacío.")
        return
        
    for exp in expedientes:
        if exp["codigo"] == codigo:
            print(f"Error: Ya existe un expediente con el código '{codigo}'.")
            return
            
    solicitante = input("Ingrese el solicitante ficticio/anonimizado: ").strip()
    if not solicitante:
        print("Error: El solicitante es obligatorio.")
        return
        
    tipo_documento = input("Ingrese el tipo de documento o trámite: ").strip()
    if not tipo_documento:
        print("Error: El tipo de documento es obligatorio.")
        return
        
    asunto = input("Ingrese el asunto: ").strip()
    if not asunto:
        print("Error: El asunto es obligatorio.")
        return
        
    fecha = input("Ingrese la fecha de recepción (DD/MM/AAAA): ").strip()
    if not fecha:
        print("Error: La fecha de recepción es obligatoria.")
        return
        
    estado = input("Ingrese el estado inicial: ").strip()
    if not estado:
        print("Error: El estado inicial es obligatorio.")
        return
        
    expedientes.append({
        "codigo": codigo,
        "solicitante": solicitante,
        "tipo_documento": tipo_documento,
        "asunto": asunto,
        "fecha": fecha,
        "estado": estado
    })
    print("¡Expediente registrado con éxito!")

def listar_expedientes():
    print("\n--- 2. LISTADO DE EXPEDIENTES ---")
    if not expedientes:
        print("No hay expedientes registrados en el sistema.")
        return
        
    for i, exp in enumerate(expedientes, 1):
        print(f"\nExpediente #{i}")
        print(f"  Código: {exp['codigo']}")
        print(f"  Solicitante: {exp['solicitante']}")
        print(f"  Tipo Documento: {exp['tipo_documento']}")
        print(f"  Asunto: {exp['asunto']}")
        print(f"  Fecha: {exp['fecha']}")
        print(f"  Estado: {exp['estado']}")

def buscar_expediente():
    print("\n--- 3. BUSCAR EXPEDIENTE POR CÓDIGO ---")
    if not expedientes:
        print("No hay expedientes registrados.")
        return
        
    codigo_buscar = input("Ingrese el código del expediente a buscar: ").strip()
    encontrado = False
    for exp in expedientes:
        if exp["codigo"] == codigo_buscar:
            print("\n¡Expediente Encontrado!")
            print(f"  Código: {exp['codigo']}")
            print(f"  Solicitante: {exp['solicitante']}")
            print(f"  Tipo Documento: {exp['tipo_documento']}")
            print(f"  Asunto: {exp['asunto']}")
            print(f"  Fecha: {exp['fecha']}")
            print(f"  Estado: {exp['estado']}")
            encontrado = True
            break
            
    if not encontrado:
        print(f"No se encontró ningún expediente con el código '{codigo_buscar}'.")

def ordenar_burbuja():
    print("\n--- 4. ORDENAR EXPEDIENTES POR CÓDIGO (MÉTODO BURBUJA) ---")
    if not expedientes:
        print("No hay expedientes para ordenar.")
        return
        
    n = len(expedientes)
    # Algoritmo de burbuja clásico sin usar funciones automáticas de ordenamiento
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if expedientes[j]["codigo"] > expedientes[j + 1]["codigo"]:
                expedientes[j], expedientes[j + 1] = expedientes[j + 1], expedientes[j]
                
    print("¡Expedientes ordenados alfabéticamente por código con éxito!")
    listar_expedientes()

def menu():
    while True:
        print("\n=================================")
        print("   SISTEMA MESA DE PARTES   ")
        print("=================================")
        print("1. Registrar expediente")
        print("2. Listar expedientes")
        print("3. Buscar expediente por código")
        print("4. Ordenar expedientes (Burbuja)")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            registrar_expediente()
        elif opcion == "2":
            listar_expedientes()
        elif opcion == "3":
            buscar_expediente()
        elif opcion == "4":
            ordenar_burbuja()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()