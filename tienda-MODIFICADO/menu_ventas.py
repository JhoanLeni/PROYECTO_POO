from models.venta import Ventas
from models.cliente import Clientes
from models.producto import Productos
las_ventas = Ventas()
los_clientes = Clientes()
mis_productos = Productos()

def ventas():
    while True:
        print("1. Agregar venta")
        print("2. Consultar venta")
        print("3. Listar ventas\n")
        print("0. Salir")
        opcion = int(input("Que deseas hacer? "))
        if opcion==1:
            num = input("Número de factura: ")
            resultado_ven = las_ventas.buscar(num)
            if resultado_ven["num"]=="No encontrado":
                id_cli = input("Id Cliente: ")
                resultado_cli = los_clientes.buscar(id_cli)
                if resultado_cli["id"]!="No encontrado":
                    print(f"Nombre cliente: {resultado_cli["nombre"]}")
                    fecha = input("Fecha (mm/dd/aaaa): ")
                    total_fac = 0
                    detalles = []
                    while True:
                        while True:
                            id_pro = input("Id producto: ")
                            resultado_pro = mis_productos.buscar(id_pro)
                            if resultado_pro["id"]!="No encontrado":
                                print(f"Nombre: {resultado_pro["nombre"]}, Stock: {resultado_pro["stock"]}")
                                while True:
                                    cantidad = int(input("Cantidad: "))
                                    if cantidad<=resultado_pro["stock"]:
                                        break
                                    else:
                                        print("No hay suficiente stock")
                                subtotal = cantidad*resultado_pro["precio"]
                                print(f"Subtotal: ${subtotal}")
                                total_fac += subtotal
                                resultado_pro["stock"] -= cantidad
                                mis_productos.modificar(resultado_pro)
                                detalles.append({"num":num, "id":id_pro, "cantidad":cantidad,"subtotal":subtotal})
                                break
                            else:
                                opcion = input("No existe, corrige (S/N): ")
                                if opcion=="S":
                                    continue
                                else:
                                    break
                        mas = input("Más productos? (S/N): ")
                        if mas =="N":
                            break
                    print(f"TOTAL FACTURA: ${total_fac}")
                    nueva_factura = {"num":num, "id_cli":id_cli,"fecha":fecha,"total":total_fac,"detalle":detalles}
                    las_ventas.agregar(nueva_factura)
        elif opcion==0:
            break
        else:
            print("OPCIÓN ERRADA!!!")
  
