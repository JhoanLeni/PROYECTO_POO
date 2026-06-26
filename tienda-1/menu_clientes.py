from models.cliente import Clientes
mis_clientes = Clientes()

def clientes():
    while True:
        print("1. Agregar cliente")
        print("2. Consultar cliente")
        print("3. Modificar cliente")
        print("4. Borrar cliente")
        print("5. Listar clientes\n")
        print("0. Salir")
        opcion = int(input("Que deseas hacer? "))
        if opcion==1:
            id = input("Identificación: ")
            resultado = mis_clientes.buscar(id)
            if resultado["id"]=="No encontrado":
                nom = input("Nombre: ")
                saldo = float(input("Saldo: "))
                tope = float(input("Tope de crédito: "))
                un_cliente = {"id": id, "nombre":nom, "saldo":saldo,"tope_credito":tope}
                mis_clientes.agregar(un_cliente)
            else:
                print(f"El id {id}, ya existe!")
        elif opcion==2:
            id = input("Identificación: ")
            resultado = mis_clientes.buscar(id)
            if resultado["id"]!="No encontrado":
                print(resultado)
            else:
                print(f"El id {id}, NO existe!")
        elif opcion==3:
            id = input("Identificación del cliente a modificar: ")
            resultado = mis_clientes.buscar(id)
            if resultado["id"]!="No encontrado":
                nom = input("Nuevo nombre: ")
                saldo = float(input("Nuevo saldo: "))
                tope = float(input("Nuevo tope de crédito: "))
                un_cliente = {"id": id, "nombre":nom, "saldo":saldo,"tope_credito":tope}
                mis_clientes.modificar(un_cliente)
            else:
                print(f"El id {id}, NO existe!")
        elif opcion==4:
            id = input("Identificación del cliente a borrar: ")
            resultado = mis_clientes.buscar(id)
            if resultado["id"]!="No encontrado":
                mis_clientes.borrar(id)
            else:
                print(f"El id {id}, NO existe!")
        elif opcion==5:
            print("LISTADO DE CLIENTES")
            mis_clientes.listar()
        elif opcion==0:
            break
        else:
            print("OPCIÓN ERRADA!!!")
        
