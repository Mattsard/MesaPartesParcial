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

def menu():
    while True:
        print("\n=================================")
        print("   SISTEMA MESA DE PARTES   ")
        print("=================================")
        print("1. Registrar expediente")
        print("2. Ver expedientes en memoria (Prueba)")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            registrar_expediente()
        elif opcion == "2":
            print("\nExpedientes en memoria:", expedientes)
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()