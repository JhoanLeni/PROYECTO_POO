from models.producto import Productos
mis_productos = Productos()

def productos():
    while True:
        print("1. Agregar producto")
        print("2. Consultar producto")
        print("3. Modificar producto")
        print("4. Borrar producto")
        print("5. Listar productos\n")
        print("0. Salir")
        opcion = int(input("Que deseas hacer? "))
        if opcion==1:
            id = input("Identificación: ")
            resultado = mis_productos.buscar(id)
            if resultado["id"]=="No encontrado":
                nom = input("Nombre: ")
                pre = float(input("Precio: "))
                stock = float(input("Stock: "))
                un_producto = {"id": id, "nombre":nom, "precio":pre,"stock":stock}
                mis_productos.agregar(un_producto)
            else:
                print(f"El id {id}, ya existe!")
        elif opcion==2:
            id = input("Identificación: ")
            resultado = mis_productos.buscar(id)
            if resultado["id"]!="No encontrado":
                print(resultado)
            else:
                print(f"El id {id}, NO existe!")
        elif opcion==3:
            id = input("Identificación del producto a modificar: ")
            resultado = mis_productos.buscar(id)
            if resultado["id"]!="No encontrado":
                nom = input("Nuevo nombre: ")
                pre = float(input("Nuevo precio: "))
                stock = float(input("Nuevo stock: "))
                un_producto = {"id": id, "nombre":nom, "precio":pre,"stock":stock}
                mis_productos.modificar(un_producto)
            else:
                print(f"El id {id}, NO existe!")
        elif opcion==4:
            id = input("Identificación del producto a borrar: ")
            resultado = mis_productos.buscar(id)
            if resultado["id"]!="No encontrado":
                mis_productos.borrar(id)
            else:
                print(f"El id {id}, NO existe!")
        elif opcion==5:
            print("LISTADO DE PRODUCTOS")
            mis_productos.listar()
        elif opcion==0:
            break
        else:
            print("OPCIÓN ERRADA!!!")
        
      