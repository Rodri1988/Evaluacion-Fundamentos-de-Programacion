import json
import datetime

ventas = []

pizza_info = {
    "cuatro_quesos_pequeña": {"precio": 6000, "tamaño": "pequeña"},
    "cuatro_quesos_mediana": {"precio": 9000, "tamaño": "mediana"},
    "cuatro_quesos_familiar": {"precio": 12000, "tamaño": "familiar"},
    "hawaiana_pequeña": {"precio": 6000, "tamaño": "pequeña"},
    "hawaiana_mediana": {"precio": 9000, "tamaño": "mediana"},
    "hawaiana_familiar": {"precio": 12000, "tamaño": "familiar"},
    "napolitana_pequeña": {"precio": 5500, "tamaño": "pequeña"},
    "napolitana_mediana": {"precio": 8500, "tamaño": "mediana"},
    "napolitana_familiar": {"precio": 11000, "tamaño": "familiar"},
    "pepperoni_pequeña": {"precio": 7000, "tamaño": "pequeña"},
    "pepperoni_mediana": {"precio": 10000, "tamaño": "mediana"},
    "pepperoni_familiar": {"precio": 13000, "tamaño": "familiar"},
}

descuentos = {
    "diurno": 0.88,
    "vespertino": 0.86,
    "admin": 0.90,
}

def menu():
    print("\nMENÚ PIZZA: ")
    print("1. Registrar venta")
    print("2. Mostrar todas las ventas")
    print("3. Buscar venta por cliente")
    print("4. Guardar ventas en archivo")
    print("5. Cargar ventas desde un archivo")
    print("6. Generar Boleta")
    print("7. Anular venta")
    print("8. Salir del programa")
    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
        registrar_venta()
        return menu()
    elif opcion == "2":
        mostrar_ventas()
        return menu()
    elif opcion == "3":
        buscar_venta()
        return menu()
    elif opcion == "4":
        guardar_ventas()
        return menu()
    elif opcion == "5":
        cargar_ventas()
        return menu()
    elif opcion == "6":
        generar_boleta()
        return menu()
    elif opcion == "7":
        print("Adios!")
    else:
        print("Opción no válida. Por favor, intente de nuevo.")
        return menu()

def registrar_venta():
    cliente = input("Ingrese nombre del cliente: ").lower()
    tipo_cliente = input("Ingrese tipo de cliente (diurno / vespertino / admin): ").lower()
    nombre_pizza = input("Ingrese el tipo de pizza (cuatro_quesos, hawaiana, napolitana, pepperoni) : ").lower()
    tamaño_pizza = input("Ingrese el tamaño de la pizza (pequeña, mediana, familiar): ").lower()
    cantidad = int(input("¿Cuántas pizzas desea?: "))

    if tipo_cliente not in descuentos:
        print("Tipo de cliente no válido.")
        return

    pizza_seleccionada = f"{nombre_pizza}_{tamaño_pizza}"
    if pizza_seleccionada not in pizza_info:
        print("Pizza no encontrada en la base de datos.")
        return

    info_pizza = pizza_info[pizza_seleccionada]
    precio_unitario = info_pizza["precio"]
    descuento = descuentos[tipo_cliente]
    precio_total = precio_unitario * cantidad
    precio_final = precio_total * descuento

    venta = {
        "cliente": cliente,
        "tipo_cliente": tipo_cliente,
        "nombre_pizza": pizza_seleccionada,
        "tamaño": tamaño_pizza,
        "cantidad": cantidad,
        "precio_total": precio_total,
        "precio_final": precio_final
    }

    ventas.append(venta)
    print("\nVenta registrada con éxito!")

def mostrar_ventas():
    if ventas:
        for venta in ventas:
            print(venta)
    else:
        print("\nNo se han registrado ventas.")

def buscar_venta():
    cliente = input("\nIngrese el nombre del cliente: ")
    encontrado = False
    for venta in ventas:
        if venta["cliente"] == cliente:
            print(venta)
            encontrado = True
    if not encontrado:
        print("\nCliente no encontrado.")

def guardar_ventas():
    with open('data_ventas.json', 'w') as archivo:
        json.dump(ventas, archivo)
    print("\nArchivo creado con éxito.")

def cargar_ventas():
    global ventas
    with open('data_ventas.json', 'r') as archivo:
        ventas = json.load(archivo)
    print("\nVentas cargadas con éxito.")

def generar_boleta():
    cliente = input("\nIngrese nombre del cliente: ")
    encontrado = False
    for venta in ventas:
        if venta["cliente"] == cliente:
            encontrado = True

            print("\n\t\t***** PIZZA *****")
            print("-------------------------------------------")
            print(f"Cliente: {venta['cliente']}")
            print(f"Fecha: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print("-------------------------------------------")
            print("Detalles de la compra:")
            print(f"- Pizza: {venta['nombre_pizza']('_', ' ')}")
            print(f"- Tamaño: {venta['tamaño']}")
            print(f"- Cantidad: {venta['cantidad']} unidad(es)")
            print("-------------------------------------------")
            print(f"Total: ${venta['precio_total']}")
            print(f"Descuento: ${venta['precio_total'] - venta['precio_final']}")
            print(f"Total a pagar: ${venta['precio_final']}")
            print("-------------------------------------------")
            print("¡Gracias por su compra!")
            print("-------------------------------------------")
            break
    if not encontrado:
        print("\nCliente no encontrado.")

menu()
