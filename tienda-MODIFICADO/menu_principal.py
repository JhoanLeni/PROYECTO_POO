from menu_clientes import clientes
from menu_productos import productos
from menu_ventas import ventas

while True:
    print("MENU PRINCIPAL")
    print("1. Clientes")
    print("2. Productos")
    print("3. Ventas\n")
    print("0. Salir")
    opcion = int(input("Que deseas hacer? "))
    if opcion==1:
        clientes()
    elif opcion==2:
        productos()
    elif opcion==3:
        ventas()
    elif opcion==0:
            break
    else:
        print("OPCIÓN ERRADA!!!")
        
        