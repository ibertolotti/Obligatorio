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
            print("\nMENÚ")
            print("          ")
            print ("1. Registrar")
            print ("2. Listar")
            print ("3. Salir del sistema")
            print ("          ")

            A = int(input("Seleccione una opción: "))
            break

        except ValueError:
            print("ERROR: ingrese una de las opciones del menú")

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
                    print("ERROR: ingrese una de las opciones del menú")

            if B == 1:
                while True:
                    try:
                        while True:
                            descripcion = input("Ingrese la descripción de la pieza: ")

                            if descripcion != "":
                                break
                            else:
                                print("\nDescripción inválida\n")

                        while True:
                            try:
                                costo_USD = float(input("Ingrese el costo de la pieza en dólares: "))
                                break
                            except ValueError:
                                print("\nVerifique que el dato ingresado sea numérico\n")
                            except ExceptionTipoDeDato:
                                print("\nHa sido ingresado un dato inválido, intente nuevamente\n")

                        while True:
                            try:
                                lote = int(input("Ingrese el tamaño del lote: "))
                                break
                            except ValueError:
                                print("\nVerifique que el dato ingresado sea numérico\n")
                            except ExceptionTipoDeDato:
                                print("\nHa sido ingresado un dato inválido, intente nuevamente\n")

                        while True:
                            try:
                                cantidad_stock = int(input("Si se tiene, ingrese la cantidad de stock de la pieza: "))
                                break
                            except ValueError:
                                print("\nVerifique que el dato ingresado sea numérico\n")
                            except ExceptionTipoDeDato:
                                print("\nHa sido ingresado un dato inválido, intente nuevamente\n")
                        
                        sistema.registrar_pieza(descripcion, costo_USD, lote, cantidad_stock)
                        break

                    except ExceptionPiezaYaExiste:
                        print("\nLa pieza ya existe, ingrese una nueva descripción\n")

                print("\nSe ha registrado la pieza con éxito")

                Registrar = False

            elif B == 2:
                while True:
                    try:
                        if sistema.lista_pieza == []:
                            print("\nERROR al crear la máquina")
                            print("Debe registrar piezas antes de registrar una máquina")
                            Registrar = False
                            break

                        lista_piezas_auxiliar = []
                        for p in sistema.lista_pieza:
                            lista_piezas_auxiliar.append(p)

                        while True:
                            descripcion = input("Ingrese la descripción de la máquina: ")

                            if descripcion != "":
                                break
                            else:
                                print("\nDescripción inválida\n")

                        requisito = "si"
                        
                        maquina_nueva = sistema.registrar_maquina(descripcion)

                        while requisito == "si" or requisito == "sí":
                            if lista_piezas_auxiliar == []:
                                print("\nERROR al crear la maquina")
                                print("Debe registrar más piezas antes de agregar nuevos requerimientos")
                                sistema.lista_maquina.remove(maquina_nueva)
                                Registrar = False
                                break

                            print("\nPiezas:")
                            for p in lista_piezas_auxiliar:
                                print(p.codigo, p.descripcion)
                            
                            while True:
                                while True:
                                    try:
                                        elijo_pieza = int(input("\nElija una pieza como requisito de la máquina (ingrese el código): "))
                                        break
                                    except ValueError:
                                        print("\nERROR: Ingrese el codigo de una pieza de la lista")
                                
                                pieza_existe = False
                                for a in lista_piezas_auxiliar:
                                    if elijo_pieza == a.codigo:
                                        pieza_existe = True
                                
                                if pieza_existe == True:
                                    break
                                else:
                                    print("\nERROR: ingrese un código de la lista de piezas")
                            
                            for pieza in lista_piezas_auxiliar:
                                if elijo_pieza == pieza.codigo:
                                    while True:
                                        try:
                                            cantidad = int(input("\nIngrese la cantidad de la pieza requerida: "))
                                            break
                                        except ValueError:
                                            print("\nEste valor es inválido")

                                    maquina_nueva.agregar_requerimiento(pieza, cantidad)
                                    lista_piezas_auxiliar.remove(pieza)
                            
                            while True:
                                requisito = input("\n¿Desea ingresar otro requisito? (si/no): ").strip().lower() #strip saca los espacios al principio o final y lower hace todo minuscula

                                if requisito == "si" or requisito == "sí" or requisito == "no":
                                    break
                                else:
                                    print("\nERROR: ingrese sí/no")

                            print("\nSe ha registrado la maquina con éxito")

                        maquina_nueva.costo_produccion = maquina_nueva.costo()

                        maquina_nueva.cambiar_disponibilidad()

                        break

                    except ValueError:
                        print("\nEste valor es inválido")
                    except ExceptionMaquinaYaExiste:
                        print("\nLa máquina ya existe, ingrese una nueva descripción\n")

                Registrar = False

            elif B == 3:
                while True:
                    try:
                        print("Tipo de cliente: ")
                        print ("1. Cliente Particular")
                        print ("2. Empresa")
                        print ("          ")

                        opcion = int(input("Seleccione una opción: "))

                        if opcion != 1 and opcion != 2:
                            print("\nElija una opción válida\n")
                        
                        else:
                            break

                    except ValueError:
                        print("\nEste dato es inválido\n")

                if opcion == 1:
                    while True:
                        try:
                            while True:
                                try:
                                    telefono = input("\nIngrese su número de teléfono: ")
                                    if not telefono.isdigit():
                                        raise ValueError
                                    if len(telefono)!= 9: 
                                        raise ExceptionTelefono()
                                    if not telefono.startswith("09"): 
                                        raise ExceptionTelefono()
                                    break
                                
                                except ExceptionTelefono:
                                    print("\nEste número de teléfono es inválido")
                                except ValueError:
                                    print("\nInformación inválida, revise los datos ingresados\n")

                            while True:
                                try:  
                                    correo = input("Ingrese su correo electrónico: ")
                                    break
                                
                                except ExceptionCorreoArroba:
                                    print("\nEl correo ingresado es inválido\n")
                                
                            while True:
                                try:
                                    cedula = input("Ingrese su cédula (sin guión): ")
                                    break
                                
                                except ExceptionTipoDeDato:
                                    print("\nLa cédula ingresada es inválida\n")
                                except ValueError:
                                    print("\nInformación inválida, revise los datos ingresados\n")

                            while True:
                                nombre_completo = input("Ingrese su nombre completo: ")

                                if nombre_completo != "":
                                    break
                                else:
                                    print("\nDescripción inválida\n")

                            sistema.registrar_cliente_particular(telefono, correo, cedula, nombre_completo)
                            break
                        # except ExceptionTelefono:
                        #     print("\nEste número de teléfono es inválido\n")
                        except ExceptionClienteYaExiste:
                            print("\nEste cliente ya existe, ingrese los datos nuevamente\n")
                        # except ExceptionTipoDeDato:
                        #     print("\nLa cédula ingresada es inválida\n")
                        except ValueError:
                            print("\nInformación inválida, revise los datos ingresados\n")
                        # except ExceptionCorreoArroba:
                        #     print("\nEl correo ingresado es inválido\n")

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
                            print("\nEsta empresa ya existe, ingrese los datos nuevamente\n")
                        except ExceptionTelefono:
                            print("\nEste número de teléfono es inválido\n")
                        except ExceptionTipoDeDato:
                            print("\nEl rut ingresado es inválido\n")
                        except ValueError:
                            print("\nInformación inválida, revise los datos ingresados\n")
                        except ExceptionCorreoArroba:
                            print("\nEl correo ingresado es inválido\n")

                print("\nSe ha registrado el cliente con éxito")
                
                Registrar = False
                        
            elif B == 4:
                while True:
                    try:
                        if sistema.lista_clientes == [] or sistema.lista_maquina ==[]:
                            print("ERROR: no se pudo registrar el pedido")
                            print("Debe registrar un cliente y/o una máquina antes de registrar un pedido ")
                            Registrar = False 
                            break

                        lista_id = []

                        for c in sistema.lista_clientes:
                        #Isinstance para saber el id dependiendo si es particular o empresa
                            if isinstance(c, ClienteParticular):
                                lista_id.append((c.id, c.nombre_completo))
                            elif isinstance(c, Empresa):
                                lista_id.append((c.id, c.nombre))
                        
                        print("Lista de Clientes: ")
                        for a in lista_id:
                            print (a)

                        while True:
                            elijo_cliente = int(input("Ingrese el id del cliente: "))

                            cliente_existe = False
                            for a in sistema.lista_clientes:
                                if elijo_cliente == a.id:
                                    cliente_existe = True
                            
                            if cliente_existe == True:
                                break
                            else:
                                print("\nERROR: ingrese un código de la lista de clientes")

                        lista_codigo_maquina = []
                        for d in sistema.lista_maquina:
                            lista_codigo_maquina.append((d.codigo, d.descripcion))

                        print("Lista de máquinas:")
                        for a in lista_codigo_maquina:
                            print (a)

                        while True:
                            elijo_maquina = int(input("Ingrese el código de la máquina: "))

                            maquina_existe = False
                            for a in sistema.lista_maquina:
                                if elijo_cliente == a.codigo:
                                    maquina_existe = True
                            
                            if maquina_existe == True:
                                break
                            else:
                                print("\nERROR: ingrese un código de la lista de máquinas")
                        
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

                        print("\nSe ha registrado el pedido con éxito")
                        break
                    
                    except ExceptionClienteNoExiste:
                        print("\nEl cliente seleccionado no existe, intente nuevamente\n")
                    except ExceptionMaquinaNoExiste:
                        print("\nLa máquina seleccionada no existe, intente nuevamente\n")
                    except ValueError:
                        print("\nInformacion invalida, revise los datos ingresados\n")

                Registrar = False

            elif B == 5:
                while True:
                    try:
                        if sistema.lista_pieza == []:
                            print("\nNo hay piezas registradas")
                            Registrar = False
                            break
                        else:
                            print("Lista de piezas (código/descripcion/lote):")
                            for p in sistema.lista_pieza:
                                print(p.codigo,".", p.descripcion, ", el tamaño del lote es: ", p.lote)

                        while True:
                            elijo_reposicion = int(input("\nElija una pieza para reponer (ingrese el código): "))

                            existencia = False
                            for a in sistema.lista_pieza:
                                if elijo_reposicion == a.codigo:
                                    existencia = True
                            
                            if existencia == True:
                                break
                            else:
                                print("\nERROR: ingrese un código de la lista de piezas\n")
                        
                        
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
                        
                        for m in sistema.lista_maquina:
                            m.cambiar_disponibilidad()

                        break

                    except ExceptionPiezaNoExiste:
                        print("\nLa pieza seleccionada no existe, intente nuevamente\n")
                    except ValueError:
                        print("\nEste dato es inválido\n")

                print("\nSe ha registrado la reposición con éxito")
                print("El costo en dolares de la reposicion es de (USD): ", nueva_reposicion.costo_USD)
                print("La cantidad actualizada de stock de", nueva_reposicion.pieza.descripcion, "es: ", nueva_reposicion.pieza.cantidad_stock)

                Registrar = False

            elif B == 6:
                break
                
            else:
                print("\nEsa opción no es válida\n")
    
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

                    C = int(input("\nSeleccione una opción: "))
                    break

                except ValueError:
                    print("ERROR: ingrese una de las opciones del menu")

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
                    try:
                        if sistema.lista_pedido == []:
                            print("\nNo se han realizado pedidos")
                            bucle = False
                            break

                        filtrar = input("¿Desea filtrar los pedidos por estado de entrega? (Si/No): ")

                        if filtrar == "si" or filtrar=="SI" or filtrar=="Si":
                            print("1.Pendientes")
                            print("2.Entregados")
                            estado = int(input("Seleccione una opcion: "))
                            bucle = False

                            if estado == 1:
                                for a in sistema.lista_pedido:
                                    if a.estado == "Pendiente":
                                        if isinstance (a, ClienteParticular):
                                            print("\n LISTA DE PEDIDOS PENDIENTES:")
                                            print(a.cliente.nombre_completo, a.maquina.descripcion, a.fecha_realizado, a.precio_pedido)
                                        if isinstance (a, Empresa):
                                            print("\n LISTA DE PEDIDOS PENDIENTES:")
                                            print(a.cliente.nombre, a.maquina.descripcion, a.fecha_realizado, a.precio_pedido)
                                        
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

                    except ValueError:
                        print("ERROR: ingrese una opción válida")

                Listar = False

            elif C == 3:   
                if sistema.lista_maquina == []:
                    print("No hay maquinas registradas")
                else:
                    print("\nLISTA MÁQUINAS")
                    print("CÓDIGO -", "DESCRIPCIÓN -", "COSTO PRODUCCIÓN -", "DISPONIBILIDAD")

                    for a in sistema.lista_maquina:
                        if a.disponibilidad == True:
                            print(a.codigo, a.descripcion, a.costo_produccion, "Disponible")
                        elif a.disponibilidad == False:
                            print(a.codigo, a.descripcion, a.costo_produccion, "No disponible")
                
                Listar = False

            elif C == 4:
                if sistema.lista_pieza == []:
                    print("No se ha registrado ninguna pieza")
                else:
                    print("\nLISTA PIEZAS")
                    print("CÓDIGO -", "DESCRIPCIÓN -", "COSTO(USD) -", "TAMAÑO DEL LOTE -", "CANTIDAD DE STOCK DISPONIBLE -", "CANTIDAD DE STOCK FALTANTE -", "LOTES FALTANTES")

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