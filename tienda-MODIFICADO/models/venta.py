
import json

class Ventas:
    def __init__(self):
        try:
            with open("ventas.json","r", encoding="utf-8") as archivo_ventas:
                self.listado_ven = json.load(archivo_ventas)
        except FileNotFoundError:
            self.listado_ven = []
        try:
            with open("detalles.json","r", encoding="utf-8") as archivo_detalles:
                self.listado_det = json.load(archivo_detalles)
        except FileNotFoundError:
            self.listado_det = []

    def buscar(self, num):
        encontrado = {"num":"No encontrado"}
        for una_venta in self.listado_ven:
            if una_venta["num"]==num:
                encontrado = una_venta
                break
        return encontrado
    
    def agregar(self, nueva_venta):
        self.listado_ven.append(nueva_venta)
        try:
            with open("ventas.json", "w", encoding="utf-8") as archivo_ventas:
                json.dump(self.listado_ven, archivo_ventas, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Error al guardar el archivo: {e}")

    def listar(self):
        return self.listado_ven
        
        