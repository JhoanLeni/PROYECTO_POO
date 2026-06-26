import tkinter as tk
from tkinter import ttk
from ventana_clientes import Ventana_clientes
from ventana_productos import Ventana_productos
from ventana_ventas import Ventana_ventas 

class VentanaPrincipal:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sistema de Gestión Comercial")
        self.root.geometry("400x400")
        self.estilo = ttk.Style()
        self.estilo.configure('Main.TButton', font=('Helvetica', 12, 'bold'), padding=10)
        frame_principal = tk.Frame(self.root, padx=20, pady=20)
        frame_principal.pack(expand=True, fill="both")
        lbl_titulo = tk.Label(frame_principal, text="Menú Principal", font=("Helvetica", 16, "bold"), pady=10)
        lbl_titulo.pack()
        btn_clientes = ttk.Button(
            frame_principal, 
            text="Gestión de Clientes", 
            style='Main.TButton',
            command=self.abrir_clientes
        )
        btn_clientes.pack(pady=10, fill="x")
        btn_productos = ttk.Button(
            frame_principal, 
            text="Gestión de Productos", 
            style='Main.TButton',
            command=self.abrir_productos
        )
        btn_productos.pack(pady=10, fill="x")
        btn_ventas = ttk.Button(
            frame_principal, 
            text="Gestión de Ventas", 
            style='Main.TButton',
            command=self.abrir_ventas
        )
        btn_ventas.pack(pady=10, fill="x")
        btn_salir = ttk.Button(frame_principal, text="Salir de la Aplicación", command=self.root.quit)
        btn_salir.pack(pady=20)
        self.root.mainloop()

    def abrir_clientes(self):
        Ventana_clientes(master=self.root)

    def abrir_productos(self):
        Ventana_productos(master=self.root)

    def abrir_ventas(self):
        Ventana_ventas(master=self.root)

if __name__ == "__main__":
    app = VentanaPrincipal()