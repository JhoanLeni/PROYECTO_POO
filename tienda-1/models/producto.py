"""
Se trata de escribir un programa con un CRUD para productos.
Cada producto debe tener los siguientes datos:
- codigo (string)
- nombre (string)
- precio (float)
- stock (int)
"""
import json

class Productos:
    def __init__(self):
        try:
            with open("productos.json","r", encoding="utf-8") as archivo_productos:
                self.listado_pro = json.load(archivo_productos)
        except FileNotFoundError:
            self.listado_pro = []
    
    def __del__(self):
        with open("productos.json","w", encoding="utf-8") as archivo_productos:
            json.dump(self.listado_pro, archivo_productos, indent=4, ensure_ascii=False)
    
    def agregar(self, un_producto): # se recibe un json "un_producto"
            self.listado_pro.append(un_producto)
        
    def buscar(self, id):
        encontrado = {"id":"No encontrado"}
        for un_producto in self.listado_pro:
            if un_producto["id"]==id:
                encontrado = un_producto
                break
        return encontrado

    def modificar(self, nuevo_producto):
        for i in range(len(self.listado_pro)):
            if self.listado_pro[i]["id"]==nuevo_producto["id"]:
                self.listado_pro[i]["nombre"]=nuevo_producto["nombre"]
                self.listado_pro[i]["precio"]=nuevo_producto["precio"]
                self.listado_pro[i]["stock"]=nuevo_producto["stock"]

    def borrar(self, id):
        for i in range(len(self.listado_pro)):
            if self.listado_pro[i]["id"]==id:
                self.listado_pro.pop(i)
                break

    def listar(self):
        return self.listado_pro