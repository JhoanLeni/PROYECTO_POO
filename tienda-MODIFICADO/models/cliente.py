"""
Se trata de escribir un programa con un CRUD para clientes.
Cada cliente debe tener los siguientes datos:
- identificación (string)
- nombre (string)
- saldo (float)
- tope de crédito (float)
"""
import json

class Clientes:
    def __init__(self):
        try:
            with open("clientes.json","r", encoding="utf-8") as archivo_clientes:
                self.listado_cli = json.load(archivo_clientes)
        except FileNotFoundError:
            self.listado_cli = []
    
    def __del__(self, open=open):
        with open("clientes.json","w", encoding="utf-8") as archivo_clientes:
            json.dump(self.listado_cli, archivo_clientes, indent=4, ensure_ascii=False)
    
    def agregar(self, un_cliente): # se recibe un json "un_cliente"
            self.listado_cli.append(un_cliente)
        
    def buscar(self, id):
        encontrado = {"id":"No encontrado"}
        for un_cliente in self.listado_cli:
            if un_cliente["id"]==id:
                encontrado = un_cliente
                break
        return encontrado

    def modificar(self, nuevo_cliente):
        for i in range(len(self.listado_cli)):
            if self.listado_cli[i]["id"]==nuevo_cliente["id"]:
                self.listado_cli[i]["nombre"]=nuevo_cliente["nombre"]
                self.listado_cli[i]["saldo"]=nuevo_cliente["saldo"]
                self.listado_cli[i]["tope_credito"]=nuevo_cliente["tope_credito"]

    def borrar(self, id):
        for i in range(len(self.listado_cli)):
            if self.listado_cli[i]["id"]==id:
                self.listado_cli.pop(i)
                break

    def listar(self):
        return self.listado_cli