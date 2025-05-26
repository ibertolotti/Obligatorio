from Entities.sistema import Sistema

# sistema = Sistema() #el de taler dijo que es necesario para poder llamar al sistema

print ("1. Registrar")
print ("2. Listar")
print ("3. Salir del sistema")
print ("          ")

A = int(input("Seleccione una opción: "))

if A == 1:
    print ("          ")
    print ("    1. Pieza")
    print ("    2. Máquina")
    print ("    3. Cliente")
    print ("    4. Pedido")
    print ("    5. Reposición")
    print ("    6. Salir")
    print ("          ")

    B = int(input("Seleccione una opción: "))

elif A == 2:
    print ("          ")
    print ("    1. Cliente")
    print ("    2. Pedidos")
    print ("    3. Máquinas")
    print ("    4. Piezas")
    print ("    5. Contabilidad")
    print ("    6. Salir")
    print ("          ")

    B = int(input("Seleccione una opción: "))

elif A == 3:
    print ("          ")
    print("Ha salido del programa")

else:
    print ("          ")
    print("Esa opción no es válida")
    A = int(input("Seleccione otra opción: "))

if A == 1 and B == 1:

    descripcion = input("Ingrese la descripción de la pieza: ")
    costo_USD = float(input("Ingrese el costo de la pieza en dólares: "))
    lote = int(input("Ingrese el tamaño del lote: "))
    cantidad_stock = int(input("Si se tiene, ingrese la cantidad de stock de la pieza: "))

    Sistema.registrar_pieza(descripcion, costo_USD, lote, cantidad_stock)

elif A == 1 and B == 2:

    descripcion = input("Ingrese la descripción de la máquina: ")
    requisito = input("¿Desea ingresar un reqisito de pieza? (Si/No) ")
    lista_requisitos = []

    lista_piezas = []
    for p in Sistema.lista_pieza:
        lista_piezas.append(p)

    while requisito == "Si" or requisito == "si":
        for p in Sistema.lista_pieza:
            print(lista_piezas.codigo(), lista_piezas.descripcion())
        elijo_pieza = input("Elija una pieza como requisito de la maquina (ingrese el codigo): ")
        for pieza in lista_piezas:
            if elijo_pieza == pieza.codigo():
                lista_requisitos.append(lista_piezas)
                lista_piezas.remove(pieza)

        requisito = input("¿Desea ingresar un reqisito de pieza? (Si/No) ")

    Sistema.registrar_maquina(descripcion, lista_requisitos)

elif A == 1 and B == 3:

    print ("1. Cliente Particular")
    print ("2. Empresa")
    print ("          ")

    opcion = input("Seleccione una opción: ")

    if opcion == 1:

        telefono = int(input("Ingrese su teléfono: "))
        correo = input("Ingrese su correo electrónico: ")
        cedula = int(input("Ingrese su cédula: "))
        nombre_completo = input("Ingrese su nombre completo: ")

        Sistema.registrar_cliente_particular(telefono, correo, cedula, nombre_completo)

    elif opcion == 2:

        telefono = int(input("Ingrese su teléfono: "))
        correo = input("Ingrese su correo electrónico: ")
        rut = int(input("Ingrese su número de rut: "))
        nombre = input("Ingrese el nombre de su emoresa: ")
        web = input("Ingrese su sitio web: ")

        Sistema.registrar_empresa(telefono, correo, rut, nombre, web)

# elif A == 1 and B == 4:

#     lista_id = []
#     for c in Sistema.lista_clientes:
#         lista_id.append(c.id())

#     print (lista_id)

#     elijo_cliente = input("Elija un cliente en particular: ") 

#     lista_codigo_maquina = []
#     for d in Sistema.lista_maquina:
#         lista_codigo_maquina.append(d.codigo())

#     print (lista_codigo_maquina)

#     elijo_maquina = input("Elija una maquina en particular: ")

#     if Pieza.cantidad_stock()

# elif A == 1 and B == 5:

# elif A == 1 and B == 6:

#     print("Ha salido del programa.")

# else: #Acá va el error si el usario ingresa un valor mayor a seis o negativo.