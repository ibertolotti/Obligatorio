import math
from sistema import Sistema
from datetime import datetime
from clientes import ClienteParticular, Empresa
from pieza import Pieza
from maquina import Maquina
from pedido import Pedido
from reposicion import Reposicion
from requerimiento import Requerimiento
from exceptionClienteYaExiste import ExceptionClienteYaExiste
from exceptionTipoDeDato import ExceptionTipoDeDato
from exceptionPiezaYaExiste import ExceptionPiezaYaExiste
from exceptionMaquinaYaExiste import ExceptionMaquinaYaExiste
from exceptionClienteNoExiste import ExceptionClienteNoExiste
from exceptionMaquinaNoExiste import ExceptionMaquinaNoExiste
from exceptionPiezaNoExiste import ExceptionPiezaNoExiste
from exceptionTelefono import ExceptionTelefono
from exceptionCorreoArroba import ExceptionCorreoArroba

sistema = Sistema() #Es necesario para poder llamar al sistema

Encendido = True
Registrar = True 
Listar = True

while Encendido == True:
    Registrar = True 
    Listar = True
    while True:
        try:
            print("       ")
            print("MENÚ")
            print("          ")
            print ("1. Registrar")
            print ("2. Listar")
            print ("3. Salir del sistema")
            print ("          ")

            A = int(input("Seleccione una opción: "))
            break

        except ValueError:
            print("Ingrese una de las opciones del menu")

    if A == 1:

        while Registrar == True:
            while True:
                try:
                    print ("\nREGISTRAR")
                    print ("          ")
                    print ("    1. Pieza")
                    print ("    2. Máquina")
                    print ("    3. Cliente")
                    print ("    4. Pedido")
                    print ("    5. Reposición")
                    print ("    6. Salir")
                    print ("          ")

                    B = int(input("Seleccione una opción: "))
                    print ("          ")
                    break

                except ValueError:
                    print("Ingrese una de las opciones del menu")

            if B == 1:
                while True:
                    try:
                        descripcion = input("Ingrese la descripción de la pieza: ")
                        costo_USD = float(input("Ingrese el costo de la pieza en dólares: "))
                        lote = int(input("Ingrese el tamaño del lote: "))
                        cantidad_stock = int(input("Si se tiene, ingrese la cantidad de stock de la pieza: "))
                        sistema.registrar_pieza(descripcion, costo_USD, lote, cantidad_stock)
                        break
                    except ValueError:
                        print("Este valor es inválido\n")
                    except ExceptionPiezaYaExiste:
                        print("La pieza ya existe, ingrese una nueva descripción\n")
                    except ExceptionTipoDeDato:
                        print("Ha sido ingresado un dato inválido, intente nuevamente\n")

                print("Se ha registrado la pieza con éxito")

                Registrar = False

            elif B == 2:
                while True:
                    try:
                        descripcion = input("Ingrese la descripción de la máquina: ")
                        requisito = input("¿Desea ingresar un requisito de pieza? (Si/No) ")

                        maquina_nueva = sistema.registrar_maquina(descripcion)
                        
                        lista_piezas_auxiliar = []
                        for p in sistema.lista_pieza:
                            lista_piezas_auxiliar.append(p)

                        while requisito == "Si" or requisito == "si" or requisito == "SI":
                            for p in lista_piezas_auxiliar:
                                print(p.codigo, p.descripcion)
                            elijo_pieza = int(input("Elija una pieza como requisito de la máquina (ingrese el código): "))
                            
                            for pieza in lista_piezas_auxiliar:
                                if elijo_pieza == pieza.codigo:
                                    cantidad = int(input("Ingrese la cantidad de la pieza requerida: "))
                                    maquina_nueva.agregar_requerimiento(pieza, cantidad)
                                    lista_piezas_auxiliar.remove(pieza)

                            requisito = input("¿Desea ingresar un nuevo requisito de pieza? (Si/No): ")

                        maquina_nueva.costo_produccion = maquina_nueva.costo()
                        break

                    except ValueError:
                        print("Este valor es inválido\n")
                    except ExceptionMaquinaYaExiste:
                        print("La máquina ya existe, ingrese una nueva descripción\n")

                print("Se ha registrado la maquina con éxito")

                Registrar = False

            elif B == 3:
                while True:
                    try:
                        print ("1. Cliente Particular")
                        print ("2. Empresa")
                        print ("          ")

                        opcion = int(input("Seleccione una opción: "))

                        if opcion != 1 and opcion != 2:
                            print("Elija una opción válida\n")
                        
                        else:
                            break

                    except ValueError:
                        print("Este dato es inválido\n")

                if opcion == 1:
                    while True:
                        try:
                            telefono = input("Ingrese su número de celular: ")
                            correo = input("Ingrese su correo electrónico: ")
                            cedula = input("Ingrese su cédula (sin guión): ")
                            nombre_completo = input("Ingrese su nombre completo: ")
                            sistema.registrar_cliente_particular(telefono, correo, cedula, nombre_completo)
                            break

                        except ExceptionTelefono:
                            print("Este número de celular es inválido\n")
                        except ExceptionClienteYaExiste:
                            print("Este cliente ya existe, ingrese los datos nuevamente\n")
                        except ExceptionTipoDeDato:
                            print("La cédula ingresada es inválida\n")
                        except ValueError:
                            print("Informacion invalida, revise los datos ingresados\n")
                        except ExceptionCorreoArroba:
                            print("El correo ingresado es inválido\n")

                elif opcion == 2:
                    while True:
                        try:
                            telefono = input("Ingrese su teléfono: ")
                            correo = input("Ingrese su correo electrónico: ")
                            rut = input("Ingrese su número de rut: ")
                            nombre = input("Ingrese el nombre de su empresa: ")
                            web = input("Ingrese su sitio web: ")

                            sistema.registrar_empresa(telefono, correo, rut, nombre, web)
                            break

                        except ExceptionClienteYaExiste:
                            print("Esta empresa ya existe, ingrese los datos nuevamente\n")
                        except ExceptionTipoDeDato:
                            print("El rut ingresado es inválido\n")
                        except ValueError:
                            print("Informacion invalida, revise los datos ingresados\n")
                        except ExceptionCorreoArroba:
                            print("El correo ingresado es inválido\n")

                print("Se ha registrado el cliente con éxito")
                
                Registrar = False
                        
            elif B == 4:
                while True:
                    try:
                        #Lista auxiliar
                        lista_id = []

                        for c in sistema.lista_clientes:
                        #Isinstance para saber el id dependiendo si es particular o empres
                            if isinstance(c, ClienteParticular):
                                lista_id.append((c.id, c.nombre_completo))
                            elif isinstance(c, Empresa):
                                lista_id.append((c.id, c.nombre))

                        print (lista_id)

                        elijo_cliente = int(input("Ingrese el id del cliente: "))

                        lista_codigo_maquina = []
                        for d in sistema.lista_maquina:
                            lista_codigo_maquina.append((d.codigo, d.descripcion))

                        print (lista_codigo_maquina)

                        elijo_maquina = int(input("Ingrese el código de la máquina: "))

                        pedido_realizado = sistema.registrar_pedido(elijo_cliente, elijo_maquina)

                        for requerimiento in pedido_realizado.maquina.requerimientos:
                            if requerimiento.cantidad_requerida <= requerimiento.pieza.cantidad_stock:
                                pedido_realizado.estado = "Entregado"
                                pedido_realizado.fecha_entregado = pedido_realizado.fecha_realizado
                            else:
                                pedido_realizado.estado = "Pendiente"

                        for c in sistema.lista_clientes:
                            if isinstance(c, ClienteParticular):
                                costo_pedido = pedido_realizado.maquina.costo_produccion * 1.5
                            elif isinstance(c, Empresa):
                                costo_pedido = (pedido_realizado.maquina.costo_produccion * 1.5) * 0.8

                        pedido_realizado.precio_pedido = costo_pedido

                        if pedido_realizado.estado == "Entregado":
                            for p in sistema.lista_pieza:
                                for j in pedido_realizado.maquina.requerimientos:
                                    if j.pieza.codigo ==  p.codigo:
                                        p.cantidad_stock = p.cantidad_stock - j.cantidad_requerida
                        break
                    
                    except ExceptionClienteNoExiste:
                        print("El cliente seleccionado no existe, intente nuevamente\n")
                    except ExceptionMaquinaNoExiste:
                        print("La máquina seleccionada no existe, intente nuevamente\n")

                print("Se ha registrado el pedido con éxito")

                Registrar = False

            elif B == 5:
                while True:
                    try:
                        for p in sistema.lista_pieza:
                            print(p.codigo, p.descripcion, "El tamaño del lote es: ", p.lote)

                        elijo_reposicion = int(input("Elija una pieza para reponer (ingrese el código): "))
                        cantidad_reposicion = int(input("Elija cuantos lotes desea reponer: "))

                        nueva_reposicion = sistema.registrar_reposicion(elijo_reposicion, cantidad_reposicion)                        

                    #Después de la reposición verifica si hay disponibilidad para pedidos pendientes
                        for p in sistema.lista_pedido:
                            if p.estado == "Pendiente":
                                puede_entregarse = True
                                for i in p.maquina.requerimientos:
                                    if i.cantidad_requerida > i.pieza.cantidad_stock:
                                        puede_entregarse = False
                                        break

                                if puede_entregarse == True:       
                                    p.estado="Entregado"
                                    for r in p.maquina.requerimientos:
                                        r.pieza.cantidad_stock -= r.cantidad_requerida

                        print("             ")
                        print("El costo en dolares de la reposicion es de: ", nueva_reposicion.costo_USD)
                        print("La cantidad actualizada de stock de", nueva_reposicion.pieza.descripcion, "es: ", nueva_reposicion.pieza.cantidad_stock)
                        break

                    except ExceptionPiezaNoExiste:
                        print("La pieza seleccionada no existe, intente nuevamente\n")
                    except ValueError:
                        print("Este dato es inválido\n")

                print("Se ha registrado la reposición con éxito")

                Registrar = False

            elif B == 6:
                break
                

            else:
                print ("          ")
                print("Esa opción no es válida")
                print ("          ")
    
    elif A == 2:

        while Listar == True:
            while True:
                try:
                    print ("\nLISTAR")
                    print ("          ")
                    print ("    1. Cliente")
                    print ("    2. Pedidos")
                    print ("    3. Máquinas")
                    print ("    4. Piezas")
                    print ("    5. Contabilidad")
                    print ("    6. Salir")
                    print ("          ")

                    C = int(input("Seleccione una opción: "))
                    break

                except ValueError:
                    print("Ingrese una de las opciones del menu")

            if C == 1:

                if sistema.lista_clientes == []:
                    print("No hay clientes registrados")

                else:
                    print("\nLISTA CLIENTES: ")
                    for a in sistema.lista_clientes:
                        if isinstance(a, ClienteParticular):
                            tipo = "Cliente Particular"
                            print(tipo, a.telefono, a.correo, a.cedula, a.nombre_completo)
                        elif isinstance(a, Empresa):
                            tipo = "Empresa"
                            print(tipo, a.telefono, a.correo, a.rut, a.nombre, a.web)

                Listar = False

            elif C == 2:
                bucle = True

                while bucle == True:
                    filtrar = input("¿Desea filtrar los pedidos por estado de entrega? (Si/No): ")

                    if filtrar == "si" or filtrar=="SI" or filtrar=="Si":
                        print("1.Pendientes")
                        print("2.Entregados")
                        estado = int(input("Seleccione una opcion: "))
                        bucle = False

                        if estado == 1:
                            for a in sistema.lista_pedido:
                                if a.estado == "Pendiente":
                                    print("\n LISTA DE PEDIDOS PENDIENTES:")
                                    print(a.cliente, a.maquina, a.fecha_realizado, a.precio_pedido)
                                    
                        else:
                            for a in sistema.lista_pedido:
                                if a.estado == "Entregado":
                                    print("\nLISTA DE PEDIDOS ENTREGADOS:")
                                    print(a.cliente, a.maquina, a.fecha_realizado, a.fecha_entregado, a.precio_pedido)

                    elif filtrar == "no" or filtrar == "NO" or filtrar == "No":
                        print("\nLISTA DE PEDIDOS:")
                        bucle = False

                        for a in sistema.lista_pedido:
                            if a.estado == "Pendiente":
                                if isinstance(a.cliente, ClienteParticular):
                                    print(a.cliente.nombre_completo, a.maquina.descripcion, a.fecha_realizado, a.precio_pedido)
                                elif isinstance(a.cliente, Empresa):
                                    print(a.cliente.nombre, a.maquina.descripcion, a.fecha_realizado, a.precio_pedido)
                            elif a.estado == "Entregado":
                                if isinstance(a.cliente, ClienteParticular):
                                    print(a.cliente.nombre_completo, a.maquina.descripcion, a.fecha_realizado, a.fecha_entregado, a.precio_pedido)
                                elif isinstance(a.cliente, Empresa):
                                    print(a.cliente.nombre, a.maquina.descripcion, a.fecha_realizado, a.fecha_entregado, a.precio_pedido)
                                
                    else:
                        print("Ingrese una opción válida\n")
                        bucle = True

                Listar = False

            elif C == 3:   
                print("\nLISTA MÁQUINAS")
                print("CÓDIGO", "DESCRIPCIÓN", "REQUERIMIENTOS", "COSTO PRODUCCIÓN", "DISPONIBILIDAD")

                for a in sistema.lista_maquina:
                    print(a.codigo, a.descripcion, a.requerimientos, a.costo_produccion, a.disponibilidad)
                Listar = False

            elif C == 4:
                print("\nLISTA PIEZAS")
                print("CÓDIGO", "DESCRIPCIÓN", "COSTO(USD)", "TAMAÑO DEL LOTE", "CANTIDAD DE STOCK DISPONIBLE", "CANTIDAD DE STOCK FALTANTE", "LOTES FALTANTES")

                for a in sistema.lista_pieza:
                    stock_faltante = 0
                    lotes_faltantes = 0
                    for p in sistema.lista_pedido:
                        for r in p.maquina.requerimientos:
                            if a.codigo == r.pieza.codigo:
                                if p.estado == "Pendiente":
                                    stock_faltante += r.cantidad_requerida
                    if stock_faltante != 0:
                        stock_faltante -= a.cantidad_stock
                        lotes_faltantes = math.ceil(stock_faltante/a.lote)
                        print(a.codigo, a.descripcion, a.costo_USD, a.lote, a.cantidad_stock, stock_faltante, lotes_faltantes)
                    else:
                        print(a.codigo, a.descripcion, a.costo_USD, a.lote, a.cantidad_stock, stock_faltante, lotes_faltantes)

                Listar = False

            elif C == 5:
                print("\nCONTABILIDAD")

                costo_total_produccion=0
                for c in sistema.lista_pedido:
                    if c.estado == "Entregado":
                        costo_total_produccion+=c.maquina.costo_produccion
                print("El costo total de produccion es: ", costo_total_produccion)

                ingreso_total = 0
                for c in sistema.lista_pedido:
                    if c.estado == "Entregado":
                        ingreso_total += c.precio_pedido
                print("El ingreso total es: ", ingreso_total)    

                ganancia_total = ingreso_total - costo_total_produccion
                print("La ganancia total es: ", ganancia_total)

                impuesto_ganancia= ganancia_total*0.25
                print("El impuesto a la ganancia es: ", impuesto_ganancia)
                
                ganancia_final= ganancia_total - impuesto_ganancia
                print("La ganancia final es: ", ganancia_final)

                Listar = False

            elif C == 6:
                break

            else:
                print ("          ")
                print("Esa opción no es válida")
                print ("          ")

    elif A == 3:
        print ("          ")
        print("Ha salido del programa")

        Encendido = False

    else:
        print ("          ")
        print("Esa opción no es válida")
        print ("          ")