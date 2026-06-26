import tkinter as tk
from tkinter import messagebox, ttk
import json
from models.cliente import Clientes

class Ventana_clientes:
    def __init__(self, master=None):
        self.mis_clientes = Clientes()
        self.ventana = tk.Toplevel(master)
        self.ventana.title("Gestión de Clientes")
        self.ventana.geometry("700x500")
        self.ventana.protocol("WM_DELETE_WINDOW",self.cerrar_venta)
        self.frame_entrada = tk.Frame(self.ventana,padx=10,pady=10)
        self.frame_botones = tk.Frame(self.ventana,padx=10,pady=10)
        self.frame_salida = tk.Frame(self.ventana,padx=10,pady=10)
        self.crear_entrada()
        self.frame_entrada.pack()
        self.crear_botones()
        self.frame_botones.pack()
        self.crear_salida()
        self.frame_salida.pack()
        
    def __del__(self):
        self.mis_clientes = None
        
    def crear_entrada(self):
        tk.Label(self.frame_entrada, text="Id:", width=10).grid(row=0,column=0, padx=10, pady=5, sticky="w")
        self.entrada_id = tk.Entry(self.frame_entrada, width=30)
        self.entrada_id.grid(row=0, column=1, padx=10, pady=5)
        tk.Label(self.frame_entrada, text="Nombre:", width=10).grid(row=1,column=0, pady=5, sticky="w")
        self.entrada_nombre = tk.Entry(self.frame_entrada, width=30)
        self.entrada_nombre.grid(row=1, column=1, pady=5)
        tk.Label(self.frame_entrada, text="Saldo:", width=10).grid(row=2,column=0, pady=5, sticky="w")
        self.entrada_saldo = tk.Entry(self.frame_entrada, width=30)
        self.entrada_saldo.grid(row=2, column=1, pady=5)
        tk.Label(self.frame_entrada, text="Tope crédito:", width=10).grid(row=3,column=0, pady=5, sticky="w")
        self.entrada_tope = tk.Entry(self.frame_entrada, width=30)
        self.entrada_tope.grid(row=3, column=1, pady=5)
    
    def crear_botones(self):
        estilo = ttk.Style()
        estilo.configure('TButton', font=('Helvetica', 10), padding=5)
        ttk.Button(self.frame_botones, text="Agregar", command=self.agregar_cliente).grid(row=0,column=0,padx=5)
        ttk.Button(self.frame_botones, text="Buscar", command=self.buscar_cliente).grid(row=0,column=1,padx=5)
        ttk.Button(self.frame_botones, text="Modificar", command=self.modificar_cliente).grid(row=0,column=2,padx=5)
        ttk.Button(self.frame_botones, text="Borrar", command=self.borrar_cliente).grid(row=0,column=3,padx=5)
        ttk.Button(self.frame_botones, text="Listar", command=self.listar_cliente).grid(row=0,column=4,padx=5)
        ttk.Button(self.frame_botones, text="Limpiar", command=self.limpiar_cliente).grid(row=0,column=5,padx=5)

    def crear_salida(self):
        self.salida_texto = tk.Text(self.frame_salida, wrap="word", state="disabled")
        self.salida_texto.pack(expand=True, fill="both")
    
    def mostrar_mensaje(self, mensaje):
        self.salida_texto.config(state="normal")
        self.salida_texto.delete("1.0", tk.END)
        self.salida_texto.insert(tk.END, mensaje)
        self.salida_texto.config(state="disabled")

    def cerrar_venta(self):
        self.mis_clientes = None
        self.ventana.destroy()
    
    def obtener_datos(self):
        id = self.entrada_id.get()
        nombre = self.entrada_nombre.get()
        try:
            tope = float(self.entrada_tope.get())
        except ValueError:
            messagebox.showerror("Error", "El tope de crédito debe ser un número!")
            return None
        try:
            saldo = float(self.entrada_saldo.get())
        except ValueError:
            messagebox.showerror("Error", "El saldo debe ser un número!")
            return None
        return {"id": id, "nombre": nombre, "saldo":saldo, "tope_credito": tope}
        
    def agregar_cliente(self):
        cliente = self.obtener_datos()
        if cliente:
            resultado = self.mis_clientes.buscar(cliente["id"])
            if resultado["id"]=="No encontrado":
                self.mis_clientes.agregar(cliente)
                self.mostrar_mensaje("Cliente agregado con éxito!")
                self.limpiar_cliente()
            else:
                self.mostrar_mensaje("Id de cliente ya existe!")

    def buscar_cliente(self):
        id = self.entrada_id.get()
        if id!="":
            resultado = self.mis_clientes.buscar(id)
            if resultado["id"]=="No encontrado":
                self.mostrar_mensaje("Id de cliente no existe!")
            else:
                self.limpiar_cliente()
                self.entrada_id.insert(0,resultado["id"])                     
                self.entrada_nombre.insert(0,resultado["nombre"])     
                self.entrada_saldo.insert(0,resultado["saldo"])     
                self.entrada_tope.insert(0,resultado["tope_credito"])     

    def modificar_cliente(self):
        cliente = self.obtener_datos()
        self.buscar_cliente()
        self.mis_clientes.modificar(cliente)
        
    def borrar_cliente(self):
        id = self.entrada_id.get()
        self.buscar_cliente()
        self.mis_clientes.borrar(id)

    def listar_cliente(self):
        listado = self.mis_clientes.listar()
        lista = ""
        for un_cliente in listado:
            lista = lista + str(un_cliente) + "\n"
        self.mostrar_mensaje(lista)
        
    def limpiar_cliente(self):
        self.entrada_id.delete(0,tk.END)
        self.entrada_nombre.delete(0,tk.END)
        self.entrada_tope.delete(0,tk.END)
        self.entrada_saldo.delete(0,tk.END)
        self.mostrar_mensaje("")
    