from sistema import Sistema
from datetime import datetime
from clientes import ClienteParticular, Empresa
from pieza import Pieza
from maquina import Maquina
from pedido import Pedido
from reposicion import Reposicion
from requerimiento import Requerimiento

sistema = Sistema() #Es necesario para poder llamar al sistema

A=0
while A!=3:
    print("MENU")
    print("          ")
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

        sistema.registrar_pieza(descripcion, costo_USD, lote, cantidad_stock)

    elif A == 1 and B == 2:

        descripcion = input("Ingrese la descripción de la máquina: ")
        requisito = input("¿Desea ingresar un requisito de pieza? (Si/No) ")

        maquina_nueva = sistema.registrar_maquina(descripcion)
        
        lista_piezas = []
        for p in sistema.lista_pieza:
            lista_piezas.append(p)

        while requisito == "Si" or requisito == "si":
            for p in sistema.lista_pieza:
                print(p.codigo, p.descripcion)
            elijo_pieza = input("Elija una pieza como requisito de la maquina (ingrese el codigo): ")
            for pieza in lista_piezas:
                if elijo_pieza == pieza.codigo:
                    cantidad = input("Ingrese la cantidad de la pieza requerida: ")
                    maquina_nueva.agregar_requerimiento(pieza, cantidad)
                    lista_piezas.remove(pieza)

            requisito = input("¿Desea ingresar un nuevo reqisito de pieza? (Si/No): ")

        maquina_nueva.costo_produccion = maquina_nueva.costo()

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

            sistema.registrar_cliente_particular(telefono, correo, cedula, nombre_completo)

        elif opcion == 2:

            telefono = int(input("Ingrese su teléfono: "))
            correo = input("Ingrese su correo electrónico: ")
            rut = int(input("Ingrese su número de rut: "))
            nombre = input("Ingrese el nombre de su emoresa: ")
            web = input("Ingrese su sitio web: ")

            sistema.registrar_empresa(telefono, correo, rut, nombre, web)

    elif A == 1 and B == 4:

        #Lista auxiliar
        lista_id = []

        for c in sistema.lista_clientes:
        #Isinstance para saber el id dependiendo si es particular o empresa
            if isinstance(c, ClienteParticular):
                lista_id.append(c.id, c.nombre_completo)
            elif isinstance(c, Empresa):
                lista_id.append(c.id, c.nombre)

        print (lista_id)

        elijo_cliente = input("Ingrese el id del cliente: ") 

        for c in sistema.lista_clientes:
            if c.id == elijo_cliente:
                cliente_pedido = c
                break #para que una vez que lo encuentre no siga el bucle

        lista_codigo_maquina = []
        for d in sistema.lista_maquina:
            lista_codigo_maquina.append(d.codigo, d.descripcion)

        print (lista_codigo_maquina)

        elijo_maquina = input("Ingrese el codigo de la maquina: ")

        for d in sistema.lista_maquina:
            if d.codigo == elijo_maquina:
                maquina_pedido = d
                break

        pedido_realizado = sistema.registrar_pedido(cliente_pedido, maquina_pedido)

        for requerimiento in pedido_realizado.maquina.requerimientos:
            if requerimiento.cantidad_requerida <= requerimiento.pieza.cantidad_stock:
                pedido_realizado.estado = "Entregado"
                pedido_realizado.fecha_entregado = pedido_realizado.fecha_realizado
            else:
                pedido_realizado.estado = "Pendiente"

        for c in sistema.lista_clientes:
            if isinstance(c, ClienteParticular):
                costo_pedido = maquina_pedido.costo_produccion * 1.5
            elif isinstance(c, Empresa):
                costo_pedido = (maquina_pedido.costo_produccion * 1.5) * 0.8

        pedido_realizado.precio_pedido = costo_pedido

        if pedido_realizado.estado == "Entregado":
            for p in sistema.lista_pieza:
                if pedido_realizado.maquina.requerimientos.pieza.codigo == p.codigo:
                    p.cantidad_stock = p.cantidad_stock - pedido_realizado.maquina.requerimientos.cantidad_requerida

    elif A == 1 and B == 5:

        for p in sistema.lista_pieza:
            print(p.codigo, p.descripcion, "El tamaño del lote es: ", p.lote)

        elijo_reposicion = input("Elija una pieza para reponer (ingrese el codigo): ")
        cantidad_reposicion = input("Elija cuantos lotes desea reponer: ")

        for e in sistema.lista_pieza:
            if e.codigo == elijo_reposicion:
                pieza_elegida = e 
                e.cantidad_stock += cantidad_reposicion * e.lote
                break
        
        nueva_reposicion = sistema.registrar_reposicion(pieza_elegida, cantidad_reposicion)

        print(nueva_reposicion.costo_USD)
        print(pieza_elegida.cantidad_stock)

    #DESPUES DE LA REPOSICION VERIFICAR SI HAY DISPONIBILIDAD PARA PEDIDOS PENDIENTES
        for p in sistema.lista_pedido:
            if p.estado == "Pendiente":
                puede_entregarse = True
                for i in p.maquina.requerimientos:
                    if i.cantidad_requerida > i.pieza.cantidad_stock:
                        puede_entregarse = False
                        break
                if puede_entregarse==True:       
                    p.estado="Entregado"
                    for s in sistema.lista_pieza:
                        for requerimientos in p.maquina.requerimientos:
                            if requerimientos.pieza.codigo == s.codigo:
                                s.cantidad_stock = s.cantidad_stock - requerimientos.cantidad_requerida

    # elif A == 1 and B == 6:

    #     print("Ha salido del programa.")

    # else: #Acá va el error si el usario ingresa un valor mayor a seis o negativo.