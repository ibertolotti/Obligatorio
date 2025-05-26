from Entities.sistema import Sistema
from Entities.clientes import Cliente, ClienteParticular, Empresa
from Entities.pieza import Pieza
from Entities.maquina import Maquina
from Entities.pedido import Pedido
from Entities.reposicion import Reposicion
from Entities.requerimiento import Requerimiento

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

    Sistema.registrar_pieza(descripcion, costo_USD, lote)

# elif A == 1 and B == 2:

#     descripcion = input("Ingrese la descripción de la máquina: ")

#     print("")

# elif A == 1 and B == 3: