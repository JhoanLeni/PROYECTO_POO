import tkinter as tk
from tkinter import messagebox, ttk
from models.venta import Ventas 

class Ventana_ventas:
    def __init__(self, master=None):
        self.mis_ventas = Ventas()  # Modelo de ventas correcto
        self.ventana = tk.Toplevel(master)
        self.ventana.title("Gestión de Ventas")
        self.ventana.geometry("700x500")
        self.ventana.grab_set() 
        
        self.frame_entrada = tk.Frame(self.ventana, padx=10, pady=10)
        self.frame_botones = tk.Frame(self.ventana, padx=10, pady=10)
        self.frame_salida = tk.Frame(self.ventana, padx=10, pady=10)
        
        self.crear_entrada()
        self.frame_entrada.pack()
        self.crear_botones()
        self.frame_botones.pack()
        self.crear_salida()
        self.frame_salida.pack()
        
    def crear_entrada(self):
        tk.Label(self.frame_entrada, text="Num Venta:", width=12).grid(row=0, column=0, padx=10, pady=5, sticky="w")
        # CORRECCIÓN: Se define como self.entrada_num para que coincida con obtener_datos
        self.entrada_num = tk.Entry(self.frame_entrada, width=30)
        self.entrada_num.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(self.frame_entrada, text="Id Cliente:", width=12).grid(row=1, column=0, pady=5, sticky="w")
        self.entrada_cliente = tk.Entry(self.frame_entrada, width=30)
        self.entrada_cliente.grid(row=1, column=1, pady=5)
        
        tk.Label(self.frame_entrada, text="Id Producto:", width=12).grid(row=2, column=0, pady=5, sticky="w")
        self.entrada_producto = tk.Entry(self.frame_entrada, width=30)
        self.entrada_producto.grid(row=2, column=1, pady=5)
        
        tk.Label(self.frame_entrada, text="Cantidad:", width=12).grid(row=3, column=0, pady=5, sticky="w")
        self.entrada_cantidad = tk.Entry(self.frame_entrada, width=30)
        self.entrada_cantidad.grid(row=3, column=1, pady=5)
    
    def crear_botones(self):
        estilo = ttk.Style()
        estilo.configure('TButton', font=('Helvetica', 10), padding=5)
        ttk.Button(self.frame_botones, text="Registrar", command=self.agregar_venta).grid(row=0, column=0, padx=5)
        ttk.Button(self.frame_botones, text="Buscar", command=self.buscar_venta).grid(row=0, column=1, padx=5)
        ttk.Button(self.frame_botones, text="Listar", command=self.listar_ventas).grid(row=0, column=2, padx=5)
        ttk.Button(self.frame_botones, text="Limpiar", command=self.limpiar_venta).grid(row=0, column=3, padx=5)

    def crear_salida(self):
        self.salida_texto = tk.Text(self.frame_salida, wrap="word", state="disabled", height=12, width=75)
        self.salida_texto.pack(expand=True, fill="both")
    
    def mostrar_mensaje(self, mensaje):
        self.salida_texto.config(state="normal")
        self.salida_texto.delete("1.0", tk.END)
        self.salida_texto.insert(tk.END, mensaje)
        self.salida_texto.config(state="disabled")
    
    def obtener_datos(self):
        num_venta = self.entrada_num.get().strip()
        id_cliente = self.entrada_cliente.get().strip()
        id_producto = self.entrada_producto.get().strip()
        cantidad = self.entrada_cantidad.get().strip()
        
        if not num_venta or not id_cliente or not id_producto or not cantidad:
            messagebox.showerror("Error", "Todos los campos son obligatorios!")
            return None
        
        try:
            cantidad = int(cantidad)
        except ValueError:
            messagebox.showerror("Error", "La cantidad debe ser un número entero!")
            return None
            
        return {"num": num_venta, "cliente_id": id_cliente, "producto_id": id_producto, "cantidad": cantidad}
        
    def agregar_venta(self):
        venta = self.obtener_datos()
        if venta:
            resultado = self.mis_ventas.buscar(venta["num"])
            if resultado["num"] == "No encontrado":
                self.mis_ventas.agregar(venta)
                self.mostrar_mensaje("Venta registrada con éxito!")
                self.limpiar_venta()
            else:
                self.mostrar_mensaje("El Num de la venta ya existe!")

    def buscar_venta(self):
        num_venta = self.entrada_num.get().strip()
        if num_venta != "":
            resultado = self.mis_ventas.buscar(num_venta)
            if resultado["num"] == "No encontrado":
                self.mostrar_mensaje("Num de venta no existe!")
            else:
                self.limpiar_venta()
                self.entrada_num.insert(0, resultado["num"])                     
                self.entrada_cliente.insert(0, resultado["cliente_id"])     
                self.entrada_producto.insert(0, resultado["producto_id"])     
                self.entrada_cantidad.insert(0, resultado["cantidad"])     
                self.mostrar_mensaje(f"Venta encontrada con éxito.")
        else:
            messagebox.showerror("Error", "Ingresa un Num de venta para buscar!")

    def listar_ventas(self):
        listado = self.mis_ventas.listar()
        if not listado:
            self.mostrar_mensaje("No hay ventas registradas.")
            return
        lista = ""
        for una_venta in listado:
            lista += f"Venta Num: {una_venta['num']} | Cliente ID: {una_venta['cliente_id']} | Producto ID: {una_venta['producto_id']} | Cantidad: {una_venta['cantidad']}\n"
        self.mostrar_mensaje(lista)
        
    def limpiar_venta(self):
        self.entrada_num.delete(0, tk.END)
        self.entrada_cliente.delete(0, tk.END)
        self.entrada_producto.delete(0, tk.END)
        self.entrada_cantidad.delete(0, tk.END)
        self.mostrar_mensaje("")