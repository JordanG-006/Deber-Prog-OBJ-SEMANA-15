import tkinter as tk
from tkinter import ttk, messagebox
from servicios.restaurante_servicio import RestauranteServicio

class MainView:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Restaurante - Semana 15")
        self.root.geometry("650x550")
        
        self.servicio = RestauranteServicio()
        self.crear_interfaz()

    def crear_interfaz(self):
        # Frame del Logo (Obligatorio en la rúbrica usar carpeta assets)
        frame_logo = tk.Frame(self.root)
        frame_logo.pack(pady=10)
        try:
            self.img_logo = tk.PhotoImage(file="assets/logo.png")
            lbl_logo = tk.Label(frame_logo, image=self.img_logo)
            lbl_logo.pack()
        except Exception:
            lbl_logo = tk.Label(frame_logo, text="[Logo de assets/logo.png no encontrado]", fg="red")
            lbl_logo.pack()

        # Frame de Registro de Ventas
        frame_ventas = tk.LabelFrame(self.root, text="Nueva Venta", padx=10, pady=10)
        frame_ventas.pack(pady=10, fill="x", padx=20)

        tk.Label(frame_ventas, text="Cédula Usuario:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_usuario = tk.Entry(frame_ventas, width=30)
        self.entry_usuario.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_ventas, text="Código Producto:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_producto = tk.Entry(frame_ventas, width=30)
        self.entry_producto.grid(row=1, column=1, padx=5, pady=5)

        # *** FUNDAMENTOS DE EVENTOS: Uso de command= para asociar el callback ***
        self.btn_vender = tk.Button(frame_ventas, text="Registrar Venta", bg="#4CAF50", fg="white", 
                                    command=self.callback_registrar_venta)
        self.btn_vender.grid(row=2, column=0, columnspan=2, pady=15)

        # Frame del Historial (Treeview)
        frame_historial = tk.LabelFrame(self.root, text="Historial de Ventas")
        frame_historial.pack(fill="both", expand=True, padx=20, pady=10)

        self.tree = ttk.Treeview(frame_historial, columns=("ID", "Usuario", "Producto", "Fecha"), show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Usuario", text="Cédula")
        self.tree.heading("Producto", text="Cód. Producto")
        self.tree.heading("Fecha", text="Fecha de Venta")
        
        self.tree.column("ID", width=50, anchor="center")
        self.tree.column("Usuario", width=120, anchor="center")
        self.tree.column("Producto", width=120, anchor="center")
        
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.actualizar_tabla()

    def callback_registrar_venta(self):
        """Callback ejecutado por el evento del botón"""
        cedula = self.entry_usuario.get().strip()
        codigo = self.entry_producto.get().strip()

        if not cedula or not codigo:
            messagebox.showwarning("Campos incompletos", "Por favor ingrese la cédula y el código del producto.")
            return

        # Delegar la operación al servicio (no manipular JSON aquí)
        exito, mensaje = self.servicio.registrar_venta(cedula, codigo)
        
        if exito:
            messagebox.showinfo("Éxito", mensaje)
            self.entry_usuario.delete(0, tk.END)
            self.entry_producto.delete(0, tk.END)
            # Actualización de la vista
            self.actualizar_tabla()
        else:
            messagebox.showerror("Error", mensaje)

    def actualizar_tabla(self):
        """Limpia y recarga el Treeview con los datos actuales"""
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        for venta in self.servicio.obtener_ventas():
            self.tree.insert("", tk.END, values=(
                venta["id_venta"], 
                venta["cedula_usuario"], 
                venta["codigo_producto"], 
                venta["fecha"]
            ))
